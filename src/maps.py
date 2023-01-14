import requests
from bs4 import BeautifulSoup

url = 'https://www.example.com/rentals'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

rentals = soup.find_all(class_='rental-listing')
for rental in rentals:
    title = rental.find(class_='title').get_text()
    location = rental.find(class_='location').get_text()
    price = rental.find(class_='price').get_text()
    print(title + ' | ' + location + ' | ' + price)