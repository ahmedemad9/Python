#!/usr/bin/python3 

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re 

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

choice=int(input("ur choice? "))
if choice == 1 :
     url = "http://py4e-data.dr-chuck.net/comments_42.html"
else:
     url = "http://py4e-data.dr-chuck.net/comments_872485.html"
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
y=[]
summa=0
# Retrieve all of the anchor tags
tags = soup('span')
#print(tags)
y=re.findall('[0-9]+',str(tags))
for tag in y:
     summa+=int(tag)
print(summa)
