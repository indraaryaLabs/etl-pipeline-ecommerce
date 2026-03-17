import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time  # Tambahan modul untuk memberikan delay

def extract_data(base_url, total_pages=50):
    products = []
    
    try:
        for page in range(1, total_pages + 1):
            # Perbaikan logika penulisan URL sesuai instruksi reviewer
            if page == 1:
                url = base_url
            else:
                # Memastikan format menjadi https://fashion-studio.dicoding.dev/page2
                if base_url.endswith('/'):
                    url = f"{base_url}page{page}"
                else:
                    url = f"{base_url}/page{page}"
            
            response = requests.get(url)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            cards = soup.find_all('div', class_='collection-card')
            
            for card in cards:
                try:
                    title_elem = card.find('h3', class_='product-title')
                    price_elem = card.find('span', class_='price')
                    p_tags = card.find_all('p')
                    
                    title = title_elem.text.strip() if title_elem else None
                    price = price_elem.text.strip() if price_elem else None
                    
                    rating_raw = p_tags[0].text.strip() if len(p_tags) > 0 else None
                    colors_raw = p_tags[1].text.strip() if len(p_tags) > 1 else None
                    size_raw = p_tags[2].text.strip() if len(p_tags) > 2 else None
                    gender_raw = p_tags[3].text.strip() if len(p_tags) > 3 else None

                    rating = rating_raw.replace('Rating:', '').replace('⭐', '').strip() if rating_raw else None
                    
                    products.append({
                        "Title": title,
                        "Price": price,
                        "Rating": rating,
                        "Colors": colors_raw,
                        "Size": size_raw,
                        "Gender": gender_raw,
                        "Timestamp": datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')
                    })
                except Exception as e:
                    print(f"Error parsing a card on page {page}: {e}")
                    continue
            
            # Memberikan jeda 1 detik di setiap halaman untuk menghindari rate limit server
            time.sleep(1)
                    
        print(f"Berhasil mengekstrak {len(products)} data mentah.")
        return products
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching website: {e}")
        return None
    except Exception as e:
        print(f"An error occurred during extraction: {e}")
        return None