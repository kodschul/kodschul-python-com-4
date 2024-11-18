import requests
import pandas as pd

from bs4 import BeautifulSoup

res = requests.get("https://books.toscrape.com/")
soup = BeautifulSoup(res.text, "html.parser")
all_articles = soup.find_all("article")


products = []

for article in all_articles:
    name = article.find("h3").text
    price = article.find(attrs={'class': 'price_color'}).text

    products.append({
        'name': name,
        'price': price
    })


df = pd.DataFrame(products)

df.to_csv("books_prices.csv")
