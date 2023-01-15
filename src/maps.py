from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pathlib import Path
import pandas as pd
import folium
import os, subprocess
from geopy.geocoders import Nominatim

g_code = Nominatim(user_agent='http')

def generate_map(places, names, init):
    center = init
    g_code = Nominatim(user_agent='http')
    map_ = folium.Map(location=center, zoom_start=8)

    for name, place in zip(names, places):
        spliced_p = place[9:].split(',')
        try:
            loc_details = dict(
                postalcode=spliced_p[-1][-8:],
                city=spliced_p[-2]
            )
            geolocation = g_code.geocode(loc_details)
            location = (geolocation.latitude, geolocation.longitude)
            folium.Marker(location, popup=name ).add_to(map_)
        except:
            # In the event that it fails
            continue
    map_.save('index.html')


def show_map():
    source_path = Path(__file__).resolve().parent
    html_path = source_path.parent/'index.html'
    try:
        # For windows
        os.startfile(html_path)
    except:
        # For linux/mac
        subprocess.call(['open', html_path])
    