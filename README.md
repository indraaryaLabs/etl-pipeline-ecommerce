# E-commerce ETL Pipeline

A small Python ETL pipeline that scrapes product listings from a demo fashion store, cleans them with pandas, and writes an analysis-ready CSV. Built as the final submission for a Dicoding data-processing course.

## What it does

1. **Extract** — fetches 50 catalogue pages from `https://fashion-studio.dicoding.dev/` with `requests` + BeautifulSoup, with a 1-second delay between pages so the server isn't hammered, and stamps each record with the scrape time.
2. **Transform** — drops nulls and duplicates, removes invalid rows (`Unknown Product`, unrated items), strips label text from the size/gender/colors fields, converts USD prices to numbers and then to IDR (fixed rate of 16,000).
3. **Load** — saves the cleaned table to `products.csv` (867 products in the last run).

Each step lives in its own module under `utils/` and has unit tests under `tests/`.

## Run it

```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

## Tests

```bash
python -m pytest tests
coverage run -m pytest tests && coverage report -m
```

## Structure

```
main.py             # runs extract -> transform -> load
utils/extract.py    # scraping and page parsing
utils/transform.py  # cleaning and type conversion
utils/load.py       # CSV export
tests/              # unit tests for each step
```
