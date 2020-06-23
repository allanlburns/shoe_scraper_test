# Scraping Rithmschool Blog
# https://www.rithmschool.com/blog
import requests
from bs4 import BeautifulSoup
from csv import writer

def product_info(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "html.parser")
    # prod_info = soup.find(class_="yada_wrap")
    prod_info = soup.select(".yada_wrap")
    prod_name = soup.find(class_="product-single__title").get_text()
    price = soup.find(class_="money").get_text()
    sku = soup.find(class_="variant-sku").get_text()
    sku = sku.replace("-", "")


    # print(prod_info)
    print(f"Product Name: {prod_name}")
    print(f"Price: {price}")
    print(f"SKU: {sku}")

product_info("https://undefeated.com/collections/all/products/yeezy-boost-350-v2-citrin?variant=31506303975497")
