
from datetime import datetime
import tkinter as tk
from tkinter import ttk
import requests
from bs4 import BeautifulSoup

window = tk.Tk()
window.geometry("1280x720")
height = window.winfo_screenheight()
width = window.winfo_screenwidth()
window.title("House Listings in Hamilton")

url = 'https://www.kijiji.ca/b-apartments-condos/hamilton/c37l80014'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

rentals = soup.find_all(class_='info-container')
canvas = tk.Canvas(window, bg="white", height=720, width=1280)
canvas.pack()
heading = "Housing Prices in Hamilton"
header = canvas.create_text(width/2-len(heading)/2, 15, text = heading, font=("Arial", 12, "bold"), tags = 'keep')

def sortListings(b):
    sortedList = []
    for i in b:
        curr = i[1]
        if(curr[len(curr)-1] == 'o'): # checks if its hours
            numb = int(curr[2]) # extract the number of hours ago
            if(curr[3].isnumeric()):
                numb = int(curr[2] + curr[3])
            sortedList.append((i[0], i[1], numb))
    sortedList.sort(key = lambda x: x[2])
    
    return sortedList

def sortDate():
    #sortedList = sorted(lst, key=lambda x: x[1])
    sorted = sortListings(lst)
    

    canvas.delete("!keep")
    currHeight = 25
    widthList = 250
    widthPrice = 500
    for i in range(len(sorted)):
        title = sorted[i][0]
        date = sorted[i][1]
        currHeight+=25
        canvas.create_text(widthList, currHeight, text=title)
        canvas.create_text(widthPrice, currHeight, text=date)
        if currHeight >= height:
            currHeight = 25
            widthList += 600
            widthPrice += 600
          

def sortPrices():
    canvas.delete("!keep")
    sortedPrices = sorted(listingDict.items(), key=lambda x: x[1])
    currHeight = 25
    widthList = 250
    widthPrice = 500

    for i in range(len(sortedPrices)):
        title = sortedPrices[i][0]
        price = str(sortedPrices[i][1])
        currHeight += 25
        canvas.create_text(widthList, currHeight, text=title)
        canvas.create_text(widthPrice, currHeight, text=price)
        if currHeight >= height:
            currHeight = 25
            widthList += 600
            widthPrice += 600
          

listingDict = {}
currHeight = 25
widthList = 250
widthPrice = 500
lst = []
for rental in rentals:
    datePosted = rental.find(class_='date-posted').get_text().strip()
    title = rental.find(class_='title').get_text().strip()
    price = rental.find(class_='price').get_text().strip().strip('$').replace(',', '')
    lst.append([title,datePosted])
    if price != ('Please Contact'):
        listingDict[title] = float(price)
        currHeight += 25
        canvas.create_text(widthList, currHeight, text=title)
        canvas.create_text(widthPrice, currHeight, text=price)
      
        if currHeight >= height:
            currHeight = 25
            widthList += 600
            widthPrice += 600


datePostedButton = ttk.Button(canvas, text='Sort by Date', command=sortDate)
priceButton = ttk.Button(canvas, text='Sort by Price', command=sortPrices)
exitButton = ttk.Button(canvas, text='Exit', command=window.destroy)
datePostedButton.place(x = 1100, y = 520)
priceButton.place(x = 1100, y = 550)
exitButton.place(x = 1100, y = 580)

window.mainloop()