import requests

from bs4 import BeautifulSoup

url = 'https://www.flipkart.com/search?q=shoes&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

brands = soup.find_all(class_='_2WkVRV')

#for brand in brands:
    #print(brand.text)
    
prices = soup.find_all(class_='_30jeq3')

#for price in prices:
    #print(price.text)
    
items = soup.find_all(class_='_1xHGtK _373qXS')

for item in items:
    brands = item.find(class_='_2WkVRV')
    prices = item.find(class_='_30jeq3')
    print(brands.text, prices.text)
   
    