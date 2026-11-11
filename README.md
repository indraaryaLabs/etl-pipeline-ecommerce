# etl-pipeline-ecommerce

A Python ETL pipeline that scrapes a demo fashion e-commerce catalog, cleans and standardizes the data with pandas, and loads it into an analysis-ready destination. Built as the final submission for a Dicoding data-processing course — and structured like a production pipeline: one module per stage, with unit tests for each.

## ✨ Features

- **Extract** — fetches 50 catalog pages from the demo store with `requests` + BeautifulSoup, pacing requests with a delay between pages and stamping every record with its scrape timestamp
- **Transform** — cleans the raw scrape with pandas: drops nulls and duplicates, removes invalid rows (`Unknown Product`, unrated items), strips label text from size/gender/color fields, and converts USD prices to numeric IDR values
- **Load** — writes the clean dataset to `products.csv` by default, with additional ready-made loaders for **PostgreSQL** (`sqlalchemy` + `psycopg2`) and **Google Sheets** (service-account credentials via the Google API client)
- **Tested** — pytest unit tests cover each stage (`extract`, `transform`, `load`) and can be run with coverage reporting

## 🏗️ Project structure

```
.
├── main.py               # pipeline entry point: extract → transform → load
├── utils/
│   ├── extract.py        # page fetching and HTML parsing
│   ├── transform.py      # cleaning, validation, and type conversion
│   └── load.py           # CSV / PostgreSQL / Google Sheets loaders
├── tests/
│   ├── test_extract.py
│   ├── test_transform.py
│   └── test_load.py
├── products.csv          # output from the last pipeline run
├── requirements.txt
└── submission.txt        # course submission notes
```

## 🛠️ Tech stack

| Stage | Technology |
| --- | --- |
| Extract | requests, beautifulsoup4 |
| Transform | pandas |
| Load | CSV, sqlalchemy + psycopg2 (PostgreSQL), google-api-python-client (Sheets) |
| Testing | pytest, pytest-cov / coverage |

## 🚀 Getting started

**Prerequisites:** Python 3.10+

```bash
git clone https://github.com/indraaryaLabs/etl-pipeline-ecommerce.git
cd etl-pipeline-ecommerce

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

pip install -r requirements.txt
python main.py
```

The default run performs extract → transform → load and writes **`products.csv`** in the project root. By default the pipeline stops at CSV — PostgreSQL and Google Sheets loaders are available in `utils/load.py` if you want a database or spreadsheet destination (Google Sheets requires a `google-sheets-api.json` service-account key).

## 🧪 Testing

```bash
python -m pytest tests

# with coverage
coverage run -m pytest tests
coverage report -m
```

## 📄 License

Released under the [MIT License](LICENSE).
