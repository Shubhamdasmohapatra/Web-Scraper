import requests
from bs4 import BeautifulSoup

url = 'https://myanimelist.net/topanime.php?type=airing'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

items = soup.find_all(class_ = 'detail')
scores = soup.find_all(class_='score ac fs14')

anime_list, rating_list = [],[]

for item in items:
    anime = item.find('a').get_text()
    anime_list.append(anime)

for score in scores:
    rating = score.find('span').get_text()
    rating_list.append(rating)
    
for x in range(len(anime_list)):
    print(f'{anime_list[x]}, {rating_list[x]}')
