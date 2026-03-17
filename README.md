# Python ETL Pipeline for E-Commerce Data

## 📌 Deskripsi Proyek
Proyek ini adalah implementasi **ETL (Extract, Transform, Load) Pipeline** otomatis menggunakan Python. Program ini dirancang untuk melakukan *web scraping* data produk dari situs e-commerce (Fashion Studio), membersihkan dan mentransformasi data mentah tersebut agar siap dianalisis, lalu menyimpannya ke dalam format CSV. 

Proyek ini mendemonstrasikan kemampuan pengumpulan data dari web, manipulasi data menggunakan Pandas, dan penulisan kode modular yang terstruktur.

## ⚙️ Alur Kerja Pipeline (ETL Process)
1. **Extract:** Mengambil data mentah HTML dari target URL (`https://fashion-studio.dicoding.dev/`) menggunakan library `requests` dan `BeautifulSoup4`. Pipeline ini dikonfigurasi untuk memproses hingga 50 halaman sekaligus.
2. **Transform:** Memproses data mentah menggunakan `Pandas` dengan langkah-langkah:
   - Menghapus data kosong (Null) dan duplikat.
   - Menyaring data yang tidak valid (misal: "Unknown Product" atau "Not Rated").
   - Membersihkan format string (menghapus teks berlebih pada kolom Size, Gender, dan Colors).
   - Mengonversi format harga ($) menjadi tipe data numerik dan mengonversinya ke mata uang IDR.
3. **Load:** Mengekspor data yang telah bersih dan terstruktur ke dalam file `products.csv`.

## 🛠️ Teknologi & Library
- **Bahasa Pemrograman:** Python 3
- **Web Scraping:** `requests`, `beautifulsoup4`
- **Data Manipulation:** `pandas`
- **Unit Testing:** `pytest`, `pytest-cov`

## 🚀 Cara Menjalankan Proyek Secara Lokal

**1. Clone Repository:**
\`\`\`bash
git clone https://github.com/indraarya77/etl-pipeline-ecommerce.git
cd etl-pipeline-ecommerce
\`\`\`

**2. Instalasi Dependencies:**
Pastikan kamu memiliki Python yang terinstal, lalu jalankan perintah ini untuk menginstal semua library yang dibutuhkan:
\`\`\`bash
pip install -r requirements.txt
\`\`\`

**3. Jalankan Pipeline:**
Eksekusi file utama untuk memulai proses ETL:
\`\`\`bash
python main.py
\`\`\`
Setelah proses selesai, akan muncul pesan `--- ETL Pipeline Selesai dengan Sukses ---` dan file `products.csv` akan otomatis dibuat di dalam folder proyek.