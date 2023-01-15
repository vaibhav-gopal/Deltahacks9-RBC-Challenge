from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import geocoder
import time

#Web Scraping shit —————————————————————————
chrome_options = Options()
chrome_options.headless = True
usrLoc = geocoder.ip('me').latlng
try:
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    driver.implicitly_wait(10)
except:
    print("Chrome driver is already in use")
actions = ActionChains(driver)

class googleMaps:
    url = "https://www.google.com/maps/search/"
    zoomLevel = 12
    articlePath = "//div[@role='article']//a"
    locationPath = "//button[@data-item-id='address']"
    closeListingPath = "//button[@aria-label='Close']"
    locations = []
    names = []

google = googleMaps()

def waitUntil(path):
    wait = WebDriverWait(driver, 10)
    try:
        element = wait.until(EC.presence_of_element_located((By.XPATH, path)))
        element = wait.until(EC.visibility_of_element_located((By.XPATH, path)))
    except TimeoutException:
        print("Timeout Exception: Element not found")
        driver.quit()

def gotoAndWait(elementOrUrl, path):
    if (isinstance(elementOrUrl, WebElement)):
        elementOrUrl.click()
    else:
        driver.get(elementOrUrl)
    waitUntil(path)

def waitUntilClick(path):
    waitUntil(path)
    driver.find_element(By.XPATH, path).click()

def waitFetchAttribute(path, attribute):
    waitUntil(path)
    return driver.find_element(By.XPATH, path).get_attribute(attribute)

def waitFetchMultiple(path):
    waitUntil(path)
    return driver.find_elements(By.XPATH, path)

def extractAttributes(lst, attribute):
    result = []
    for x in lst:
        result.append(x.get_attribute(attribute))
    return result

def searchParametersGoogle():
    search = input("What keyword:")
    search.strip().replace(" ", "+").lower()
    print("User IP:",usrLoc)
    return search + "/@" + str(usrLoc[0]) + "," + str(usrLoc[1]) + ',' + str(google.zoomLevel) + "z"

def searchGoogle():
    gotoAndWait(google.url + searchParametersGoogle(), google.articlePath)
    driver.set_window_size(1200, 720)
    listings = waitFetchMultiple(google.articlePath)
    google.names = extractAttributes(listings, "aria-label")
    print("Got all names and elements!!")
    for listing in listings:
        print("Fetching...")
        actions.move_to_element(listing).perform()
        gotoAndWait(listing, google.locationPath)
        google.locations.append(waitFetchAttribute(google.locationPath, "aria-label"))
        waitUntilClick(google.closeListingPath)
        waitUntil(google.articlePath)
    print(google.locations, google.names)
    driver.quit()

searchGoogle()