from utils.extract import extract_data
from utils.transform import transform_data
from utils.load import load_to_csv

def run_pipeline():
    print("--- Memulai ETL Pipeline ---")
    
    # URL target
    TARGET_URL = "https://fashion-studio.dicoding.dev/"
    
    # 1. EXTRACT
    print("\n[1/3] Memulai proses Extract...")
    raw_data = extract_data(TARGET_URL, total_pages=50)
    
    if raw_data:
        # 2. TRANSFORM
        print("\n[2/3] Memulai proses Transform...")
        clean_df = transform_data(raw_data)
        
        if clean_df is not None:
            # 3. LOAD
            print("\n[3/3] Memulai proses Load...")
            load_to_csv(clean_df, "products.csv")
            print("\n--- ETL Pipeline Selesai dengan Sukses ---")
        else:
            print("\nPipeline berhenti: Transformasi gagal.")
    else:
        print("\nPipeline berhenti: Ekstraksi gagal.")

if __name__ == "__main__":
    run_pipeline()