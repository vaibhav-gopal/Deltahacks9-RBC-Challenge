import requests
from bs4 import BeautifulSoup
from osm_runner import Runner

# from arcgis.features import FeatureLayer, GeoAccessor, GeoSeriesAccessor
# from arcgis.geoenrichment import enrich
# from arcgis import dissolve_boundaries
# from arcgis.geometry import project
# from arcgis.gis import GIS

url = 'https://www.kijiji.ca/b-apartments-condos/hamilton/c37l80014'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

rentals = soup.find_all(class_='info-container')
for rental in rentals:
    title = rental.find(class_='title').get_text().strip()
    price = rental.find(class_='price').get_text().strip()
    print(title + ' | ' + price)

# gis = GIS('home')