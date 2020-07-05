import requests
from bs4 import BeautifulSoup
from csv import writer

def home_page_scanner(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    # product_links = soup.select(".grid-product__meta")
    products = soup.select(".grid-product__meta")

    for link in products:
        product_info("http://undefeated.com/products/" + link["href"].split("/")[-1])


        # Continue through AJAX loop

        # next = soup.find(id="#AjaxinatePagination")

        # if next:
        #     print(next)


def product_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    prod_name = soup.find(class_="product-single__title").get_text()
    price = soup.find(class_="money").get_text()
    # sku = soup.find(class_="variant-sku").get_text()
    # sku = sku.replace("-", "")


    # print(prod_info)
    print('\n')
    print('\n')
    print(f"Product Name: {prod_name}")
    print(f"Price: {price}")
    # print(f"SKU: {sku}")
    print('\n')
    print('\n')

# product_info("https://undefeated.com/collections/all/products/yeezy-boost-350-v2-citrin?variant=31506303975497")
#
# product_info("https://undefeated.com/collections/all/products/converse-x-pop-trading-co-jack-purcell-pro-ptc-hi-navy-citru?variant=31635394854985")


# Scraping Undefeated
home_page_scanner("https://undefeated.com/collections/all")

# Scraping Kith
# home_page_scanner("https://kith.com/collections/kith-summer-2020")

# Scraping Juice
# home_page_scanner("https://juicestoreusa.com/")

# Scraping Saint Alfred
# home_page_scanner("https://www.saintalfred.com/collections/brands")
