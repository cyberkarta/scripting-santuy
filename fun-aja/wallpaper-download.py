# Download Wallpaper dari https://windows10spotlight.com
# Install beautifulsoup dan lxml terlebih dahulu:
#   pip install beautifulsoup4
#   pip install lxml

import argparse
import requests
from bs4 import BeautifulSoup

url = 'https://windows10spotlight.com/page/1'
source = requests.get(url).text
soup = BeautifulSoup(source,'lxml')

# Get images link
def getImages():
  imgLink = []
  link = soup.body.findAll('img', class_="wp-post-image")
  for i in link :
      i = i.get('srcset').split(' ')
      imgLink.append(i[4])
  return imgLink

# Get the titles
def getTitles():
  titles = []
  title = soup.body.findAll('span', class_="hidden")
  for t in title:
    t = titles.append(t.contents)
  return titles

# Download images
def downloadImages(links=getImages(), titles=getTitles()):
  pointer = 0
  for link in links:
    img_data = requests.get(link).content
    title = titles[pointer][0]+'.jpg'
    with open('tmp\\'+title, 'wb') as handler:
      handler.write(img_data)
    print(titles[pointer][0], "success")
    pointer+=1
    

# print(getTitles(), '\n', getImages())
downloadImages()
