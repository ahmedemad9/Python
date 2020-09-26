#!/usr/bin/python3 
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

choice = int(input("Choice? "))
if choice == 1 :
    url = "http://py4e-data.dr-chuck.net/comments_42.xml"
else:
    url = "http://py4e-data.dr-chuck.net/comments_872487.xml"

tree = ET.fromstring(urllib.request.urlopen(url).read().decode())

results = tree.findall('.//count')
total=0

for no in results:
    total+=int(no.text)
print(total) 
