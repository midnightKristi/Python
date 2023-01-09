# Kristi LaVigne
# CSCI 236
# 03/06/2021
# Program 02 - DNA
# hours: 3
# Grade Version - N/A
# major problems: none
# status of the program - compiles and runs
# ____________________________________________________________

# This program performs web scraping to get and save images from a website
# This program requests the image urls, saves the images, and opens the images
# The website used is the Klei game Don't Starve, which has neat artwork

import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO


# making the request
def getdata(url):
    r = requests.get(url)
    return r.text


# Going to the Don't Starve Wiki and scrapping for the images
# Saving the images and opening them
htmldata = getdata("https://dontstarve.fandom.com/wiki/Don%27t_Starve_Wiki")
soup = BeautifulSoup(htmldata, 'html.parser')
for item in soup.find_all('img'):
    if 'https' in item['src']:
        image_url = item['src']
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))
        img.show()

# Listing the urls for all the images on this webpage
for item in soup.find_all('img'):
    if 'https' in item['src']:
        image_url = item['src']
        print(item['src'])
