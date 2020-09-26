#!/usr/bin/python3
import json
import urllib.request

choice=int(input("Choice? "))
if choice == 1 :
    url = "http://py4e-data.dr-chuck.net/comments_42.json"
else:
    url = "http://py4e-data.dr-chuck.net/comments_872488.json"

response = urllib.request.urlopen(url)

data = json.loads(response.read())
x=0
for i in range (0, len(data["comments"] )):
    x+=(data["comments"][i]["count"])
print(x)
