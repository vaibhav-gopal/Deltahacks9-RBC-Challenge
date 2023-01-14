import requests
from bs4 import BeautifulSoup
from pathlib import Path
import pandas as pd
import folium

url = 'https://www.kijiji.ca/b-apartments-condos/hamilton/c37l80014'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

rentals = soup.find_all(class_='info-container')
for rental in rentals:
    title = rental.find(class_='title').get_text().strip()
    price = rental.find(class_='price').get_text().strip()
    # print(title + ' | ' + price)

path = Path(__file__).resolve().parent/'location.csv'
housing = pd.read_csv(path)

center = [-0.023559, 37.9061928]
map_kenya = folium.Map(location=center, zoom_start=8)
for index, franchise in housing.iterrows():
    location = [franchise['latitude'], franchise['longitude']]
    folium.Marker(location, popup = f'Name:{franchise["store"]}\n Revenue($):{franchise["revenue"]}').add_to(map_kenya)

# save map to html file
map_kenya.save('index.html')