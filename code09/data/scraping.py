import requests
from bs4 import BeautifulSoup
import pandas as pd 

url = "https://books.toscrape.com"
response = requests.get(url, timeout=20000)
if response.status_code != 200: 
    print("Error while scraping")
    exit()

raw_html = response.text 

soup = BeautifulSoup(raw_html, 'html.parser')
product_soups = soup.find_all(class_="product_pod")

products = list()

for product_soup in product_soups: 
    name = product_soup.find("h3").text # type: ignore
    price = str( product_soup.find(class_="price_color").text ).replace("Â", "") # type: ignore
    
    product = {
        'name': name,
        'price': price
    }
    products.append(product)

product_df = pd.DataFrame(products)
product_df.to_csv("books.csv")

print(product_df)