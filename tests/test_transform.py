import pandas as pd
from utils.transform import transform_data

def test_transform_data_cleans_and_formats_correctly():
    raw_dummy = [
        {"Title": "T-shirt 2", "Price": "$102.15", "Rating": "3.9 / 5", "Colors": "3 Colors", "Size": "Size: M", "Gender": "Gender: Women", "Timestamp": "2026-03-16"},
        {"Title": "Unknown Product", "Price": "Price Unavailable", "Rating": "Invalid Rating / 5", "Colors": "5 Colors", "Size": "Size: M", "Gender": "Gender: Men", "Timestamp": "2026-03-16"}
    ]
    
    result_df = transform_data(raw_dummy)
    
    # Memastikan baris yang tidak valid ("Unknown Product") dihapus
    assert len(result_df) == 1
    
    # Memastikan konversi tipe data dan nilai berhasil (102.15 * 16000)
    assert result_df.iloc[0]['Price'] == 1634400.0
    assert result_df.iloc[0]['Rating'] == 3.9
    assert result_df.iloc[0]['Colors'] == 3
    assert result_df.iloc[0]['Size'] == "M"
    assert result_df.iloc[0]['Gender'] == "Women"