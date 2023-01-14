import requests
from bs4 import BeautifulSoup
import googlemaps
from datetime import datetime

key = 'AIzaSyCOvffCldigqFeMlG5wSfd12lLbeM6LqN0'

url = 'https://www.example.com/rentals'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

rentals = soup.find_all(class_='rental-listing')
for rental in rentals:
    title = rental.find(class_='title').get_text()
    location = rental.find(class_='location').get_text()
    price = rental.find(class_='price').get_text()
    print(title + ' | ' + location + ' | ' + price)

gmaps = googlemaps.Client(key=key)

# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions(
    "Sydney Town Hall",
    "Parramatta, NSW",
    mode="transit",
    departure_time=now)

# Validate an address with address validation
addressvalidation_result =  gmaps.addressvalidation(
    ['1600 Amphitheatre Pk'], 
    regionCode='US',
    locality='Mountain View', 
    enableUspsCass=True)