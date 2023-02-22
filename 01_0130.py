import requests
from bs4 import BeautifulSoup
#https://jsonplaceholder.typicode.com/todos/1

resource = requests.get("http://www.sdh.hs.kr/")
html = resource.text

soup = BeautifulSoup(html, "html.parser")
#print(soup)

images = soup.find_all("a", "img-box")

for i in images:
    if(i.find(attrs={"alt":"ko-text"})):
        print(i["href"])