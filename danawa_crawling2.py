import requests
from bs4 import BeautifulSoup
import time

headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}
query = "RTX 3090"
url = "https://search.danawa.com/dsearch.php?query=" + query

html = requests.get(url, headers=headers).text
soup = BeautifulSoup(html, "html.parser")
productList = soup.select(".prod_item")
for product in productList:
    product.select(".prod_name").text
