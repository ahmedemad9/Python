#!/usr/bin/python3 

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re 
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

choice=int(input("Choice? "))
if choice == 1 :
    url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
else:
    url = "http://py4e-data.dr-chuck.net/known_by_Milandra.html"
order=int(input("Order? ")) -1
depth=int(input("Depth? "))

for i in range (0,depth):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
    tag=tags[order] 
    url=tag.get('href', None) 
print(url)
y=re.findall('^__.+?.html',url)
print(y)
