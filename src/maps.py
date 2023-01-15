from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager
import geocoder
import time


from pathlib import Path
import pandas as pd
import folium
import os, subprocess

#Web Scraping shit —————————————————————————
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
url = "https://www.google.com/maps/search/"
usrLoc = geocoder.ip('me').latlng
zoomLevel = 12
articlePath="//div[@role='article']//a"
locationPath = "//button[@data-item-id='address']"
closeListingPath = "//button[@aria-label='Close']"
locations = []

def searchParameters():
    search = input("What keyword:")
    search.strip().replace(" ", "+").lower()
    print(usrLoc)
    return search + "/@" + str(usrLoc[0]) + "," + str(usrLoc[1]) + ',' + str(zoomLevel) + "z"

def search():
    driver.get(url + searchParameters())
    WebDriverWait(driver, timeout=5).until(lambda d: d.find_element(By.XPATH,articlePath).is_displayed())
    listings = driver.find_elements(By.XPATH, articlePath)
    print(listings)
    for listing in listings:
        listing.click()
        WebDriverWait(driver, timeout=5).until(lambda d: d.find_element(By.XPATH,locationPath).is_displayed())
        locations.append(driver.find_element(By.XPATH, locationPath).get_attribute("aria-label"))
        driver.find_element(By.XPATH, closeListingPath).click()
        driver.implicitly_wait(2)
    print(locations)
    driver.quit()

search()

#Map shit ——————————————————————————————
# source_path = Path(__file__).resolve().parent
# path = source_path/'location.csv'
# houses = pd.read_csv(path)

# center = [-0.023559, 37.9061928]
# map_kenya = folium.Map(location=center, zoom_start=8)
# for index, house in houses.iterrows():
#     location = [house['latitude'], house['longitude']]
#     folium.Marker(location, popup = f'Name:{house["store"]}\n Revenue($):{house["revenue"]}').add_to(map_kenya)

# if __name__ == '__main__':
#     # save map to html file
#     map_kenya.save('index.html')
#     html_path = source_path.parent/'index.html'
#     os.startfile(html_path)