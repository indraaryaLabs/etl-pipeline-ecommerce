import pandas as pd

def transform_data(raw_data):
    try:
        df = pd.DataFrame(raw_data)
        
        # 1. Hapus nilai Null dan Duplikat
        df.dropna(inplace=True)
        df.drop_duplicates(inplace=True)
        
        # 2. Hapus data invalid
        df = df[df['Title'] != 'Unknown Product']
        df = df[~df['Rating'].isin(['Invalid Rating / 5', 'Not Rated'])]
        df = df[df['Price'] != 'Price Unavailable']
        
        # 3. Konversi dan bersihkan kolom Price (Asumsi format awal: "$102.15")
        df['Price'] = df['Price'].astype(str).str.replace('$', '', regex=False)
        df['Price'] = df['Price'].astype(float) * 16000
        
        # 4. Konversi kolom Rating ("4.8 / 5" menjadi 4.8)
        df['Rating'] = df['Rating'].astype(str).str.replace(' / 5', '', regex=False).astype(float)
        
        # 5. Konversi kolom Colors ("3 Colors" menjadi 3)
        df['Colors'] = df['Colors'].astype(str).str.replace(' Colors', '', regex=False).str.replace(' Color', '', regex=False).astype(int)
        
        # 6. Bersihkan teks pada Size dan Gender
        df['Size'] = df['Size'].astype(str).str.replace('Size: ', '', regex=False)
        df['Gender'] = df['Gender'].astype(str).str.replace('Gender: ', '', regex=False)
        
        # Reset index agar rapi
        df.reset_index(drop=True, inplace=True)
        
        print(f"Transformasi berhasil. Tersisa {len(df)} baris data bersih.")
        return df

    except Exception as e:
        print(f"An error occurred during transformation: {e}")
        return None