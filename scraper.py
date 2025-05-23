# scraper.py
import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_dummy_emails():
    url = "https://www.lipsum.com/feed/html"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find_all('p')

    messages = [p.get_text() for p in paragraphs[:10]]
    df = pd.DataFrame({
        'label': ['ham'] * len(messages),
        'message': messages
    })
    df.to_csv("scraped_emails.csv", index=False)
    print("Scraped dummy messages saved to 'scraped_emails.csv'")

if __name__ == "__main__":
    scrape_dummy_emails()
