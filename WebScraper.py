import requests
from bs4 import BeautifulSoup

URL = 'https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniqBStoreParam1=val1&wid=11.productCard.PMU_V2'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='container')
products = results.find_all('div', class_='bhgxx2 col-12-12')
for product in products:
    name = product.find('div', class_='_3wU53n')
    price = product.find('div', class_='_1vC4OE _2rQ-NK')
    if None in (name, price):
        continue
    print(name.text.strip())
    print(price.text.strip())
    print()