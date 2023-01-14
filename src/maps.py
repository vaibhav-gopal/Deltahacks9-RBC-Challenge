import requests
from bs4 import BeautifulSoup
from pathlib import Path
import pandas as pd
import folium
import os

url = 'https://www.kijiji.ca/b-apartments-condos/hamilton/c37l80014'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

rentals = soup.find_all(class_='info-container')
for rental in rentals:
    title = rental.find(class_='title').get_text().strip()
    price = rental.find(class_='price').get_text().strip()
    print(title + ' | ' + price)

source_path = Path(__file__).resolve().parent
path = source_path/'location.csv'
houses = pd.read_csv(path)

center = [-0.023559, 37.9061928]
map_kenya = folium.Map(location=center, zoom_start=8)
for index, house in houses.iterrows():
    location = [house['latitude'], house['longitude']]
    folium.Marker(location, popup = f'Name:{house["store"]}\n Revenue($):{house["revenue"]}').add_to(map_kenya)

if __name__ == '__main__':
    # save map to html file
    map_kenya.save('index.html')
    html_path = source_path.parent/'index.html'
    os.startfile(html_path)