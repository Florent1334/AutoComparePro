from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

def scrape_lbc(model, mileage, year):
    url = f"https://www.leboncoin.fr/recherche?category=2&text={model}&mileage={mileage}&year={year}"
    r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(r.text, "html.parser")

    annonces = []
    for item in soup.select("a[data-qa-id='aditem_container']"):
        title = item.select_one("p[data-qa-id='aditem_title']").text.strip()
        price = item.select_one("span[data-qa-id='aditem_price']").text.strip()
        annonces.append({"title": title, "price": price})
    return annonces

def scrape_lacentrale(model, mileage, year):
    url = f"https://www.lacentrale.fr
