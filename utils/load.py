import pandas as pd
from sqlalchemy import create_engine
from google.oauth2 import service_account
from googleapiclient.discovery import build

def load_to_csv(df, filename="products.csv"):
    try:
        df.to_csv(filename, index=False)
        print(f"Data berhasil disimpan ke {filename}")
    except Exception as e:
        print(f"Gagal menyimpan ke CSV: {e}")

def load_to_postgres(df, db_url, table_name="fashion_products"):
    try:
        engine = create_engine(db_url)
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        print(f"Data berhasil disimpan ke database PostgreSQL tabel {table_name}")
    except Exception as e:
        print(f"Gagal menyimpan ke database: {e}")

def load_to_gsheets(df, spreadsheet_id, range_name="Sheet1!A1", credentials_file="google-sheets-api.json"):
    try:
        # Menyiapkan kredensial Google API
        scopes = ['https://www.googleapis.com/auth/spreadsheets']
        creds = service_account.Credentials.from_service_account_file(credentials_file, scopes=scopes)
        service = build('sheets', 'v4', credentials=creds)

        # Menyiapkan data untuk di-upload (termasuk header)
        values = [df.columns.values.tolist()] + df.values.tolist()
        body = {'values': values}

        # Mengirim data ke Google Sheets
        result = service.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id, range=range_name,
            valueInputOption="RAW", body=body
        ).execute()
        
        print(f"Data berhasil disimpan ke Google Sheets ({result.get('updatedCells')} sel diperbarui).")
    except Exception as e:
        print(f"Gagal menyimpan ke Google Sheets: {e}")