import requests
import bs4
import re
import csv
from itertools import zip_longest
url=["https://elnour-tech.com/product-category/pc/ssd",
     "https://elnour-tech.com/product-category/pc/ssd/page/2/",
     "https://elnour-tech.com/product-category/pc/ssd/page/3/",
     "https://elnour-tech.com/product-category/pc/ssd/page/4/",
     "https://elnour-tech.com/product-category/pc/ssd/page/5/",
     "https://elnour-tech.com/product-category/pc/ssd/page/6/"]
for i in range (6):
    page=requests.get(url[i])
    name=[]
    price=[]
    soup=bs4.BeautifulSoup(page.content,"html.parser")
    SSDname=soup.find_all("h3", {"class": "wd-entities-title"})
    SSDprice=soup.find_all("div", {"class": "wrapp-product-price"})
    for i in range(len(SSDname)):
        name.append(SSDname[i].get_text())
        price.append(SSDprice[i].get_text())
    for j in range(len(SSDname)):
        print(name[j],price[j])
    #print("***********************************************************************************")
