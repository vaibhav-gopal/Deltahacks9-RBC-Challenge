from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pathlib import Path
import pandas as pd
import folium
import os

#Web Scraping shit —————————————————————————
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.selenium.dev/selenium/web/web-form.html")




#Map shit ——————————————————————————————
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
