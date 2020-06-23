# Scraping Rithmschool Blog
# https://www.rithmschool.com/blog
import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get("https://undefeated.com/collections/all/products/yeezy-boost-350-v2-citrin?variant=31506303975497")
soup = BeautifulSoup(response.text, "html.parser")
# prod_info = soup.find(class_="yada_wrap")
prod_info = soup.select(".yada_wrap")
# price = soup.find(class_="yada_wrap")[class_="money"]


print(prod_info)
# print(price)
