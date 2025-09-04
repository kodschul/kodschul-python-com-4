import requests
from bs4 import BeautifulSoup
import pandas as pd 

def scrape_page(page=1):
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"
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
    return products


all_products= list()
pages_to_scrape = 10
current_page = 1


while current_page <= pages_to_scrape:
    print(f"Scraping page:  {current_page}/{pages_to_scrape}")
    page_products = scrape_page(current_page)
    all_products += page_products
    current_page += 1
    

product_df = pd.DataFrame(all_products)
product_df.to_csv("books.csv")

print(product_df)