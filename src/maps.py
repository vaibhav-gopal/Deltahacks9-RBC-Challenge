from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement

from webdriver_manager.chrome import ChromeDriverManager
import geocoder
import time

#Web Scraping shit —————————————————————————
chrome_options = Options()
chrome_options.add_argument("--headless")
usrLoc = geocoder.ip('me').latlng
try:
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
except:
    print("Chrome driver is already in use")

class googleMaps:
    url = "https://www.google.com/maps/search/"
    zoomLevel = 12
    articlePath = "//div[@role='article']//a"
    locationPath = "//button[@data-item-id='address']"
    closeListingPath = "//button[@aria-label='Close']"
    locations = []

google = googleMaps()
tempEl= []

def gotoAndWait(elementOrUrl, path):
    if (isinstance(elementOrUrl, WebElement)):
        elementOrUrl.click()
    else:
        driver.get(elementOrUrl)
    time.sleep(0.5)
    wait = WebDriverWait(driver, 10)
    try:
        element = wait.until(EC.presence_of_element_located((By.XPATH, path)))
        if element.is_displayed():
            print('Element is present')
        else:
            print('Element is present but not visible')
    except TimeoutException:
        print("Timeout Exception: Element not found")

def waitUntilClick(path):
    time.sleep(0.5)
    wait = WebDriverWait(driver, 10)
    try:
        element = wait.until(EC.presence_of_element_located((By.XPATH, path)))
        if element.is_displayed():
            driver.find_element(By.XPATH, path).click()
            print('Element is present')
        else:
            print('Element is present but not visible')
    except TimeoutException:
        print("Timeout Exception: Element not found")

def waitUntil(path):
    time.sleep(0.5)
    wait = WebDriverWait(driver, 10)
    try:
        element = wait.until(EC.presence_of_element_located((By.XPATH, path)))
        if element.is_displayed():
            print('Element is present')
        else:
            print('Element is present but not visible')
    except TimeoutException:
        print("Timeout Exception: Element not found")

def searchParametersGoogle():
    search = input("What keyword:")
    search.strip().replace(" ", "+").lower()
    print(usrLoc)
    return search + "/@" + str(usrLoc[0]) + "," + str(usrLoc[1]) + ',' + str(google.zoomLevel) + "z"

def searchGoogle():
    gotoAndWait(google.url + searchParametersGoogle(), google.articlePath)
    listings = driver.find_elements(By.XPATH, google.articlePath)
    for listing in listings:
        print(listing)
        gotoAndWait(listing, google.locationPath)
        google.locations.append(driver.find_element(By.XPATH, google.locationPath).get_attribute("aria-label"))
        waitUntilClick(google.closeListingPath)
        waitUntil(google.articlePath)
    print(google.locations)
    driver.quit()

searchGoogle()