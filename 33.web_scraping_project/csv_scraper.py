import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice
from csv import DictWriter

base_url = "https://quotes.toscrape.com"

def scrape_quotes():
    all_quotes = []
    url = "/page/1/"
    while url:
        res = requests.get(f"{base_url}{url}")
        print(url)
        soup = BeautifulSoup(res.text, "html.parser")
        quotes = soup.select(".quote")

        for quote in quotes:
            all_quotes.append({
                "text": quote.find(class_="text").get_text(),
                "author": quote.find(class_="author").get_text(),
                "bio-link": quote.find("a")["href"]
            })
            next_btn = soup.find(class_="next")
            url = next_btn.find("a")["href"] if next_btn else None
    return all_quotes



def write_quotes(quotes):
    with open("quotes.csv", "w") as file:
        headers = ["text", "author", "bio-link"]
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()
        for quote in quotes:
            csv_writer.writerow(quote)

quotes = scrape_quotes()
write_quotes(quotes)
