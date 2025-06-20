# 📚 Book Catalog Scraper

A simple Python script that scrapes book data from [books.toscrape.com](https://books.toscrape.com), a demo website for practicing web scraping.

## 🧾 Features

- Parses all pages of the catalog
- Extracts:
  - 📖 Book Title
  - 💷 Price
  - ✅ Availability
  - ⭐ Star Rating
  - 🔗 Product Link
- Saves the data into a clean CSV file
- Uses a structured `Product` dataclass

## 🛠 Technologies Used

- Python 3
- `requests`
- `BeautifulSoup`
- `csv`
- `dataclasses`
- `urllib.parse` (`urljoin`)

## 📁 Project Structure
book-catalog-scraper/
├── main.py # Main script with parser logic
├── model.py # Product dataclass
├── books.csv # Output file (generated after run)
└── README.md


## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/MegirX/book-catalog-scraper.git
   cd book-catalog-scraper
2.Install dependencies (optional if not installed):
    -pip install requests beautifulsoup4

3.Run the script:
python main.py

Output will be saved as books.csv in the project directory.
✅ Want to collaborate or see more? [Check my GitHub profile](https://github.com/MegirX)
