from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

x=1
fileName="souqProducts.csv"
f=open(fileName,"w")
headers="no. , product , price \n" 
f.write(headers)
pages=int(input("please enter number of pages you want to search in : "))
for y in range(0,pages):
    my_url='https://egypt.souq.com/eg-ar/phone/s/?as=1&section=2&page='+str(y+1)
    y+=1
    myclient=uReq(my_url)
    htmlpage= myclient.read()
    myclient.close()
    soupedpage=soup(htmlpage , "html.parser")
    containers = soupedpage.findAll("div",{"class":"column column-block block-list-large single-item"})
    for container in containers: 
        ##container = containers[x]
        title_get = container.findAll("div",{"class":"col col-info item-content"})
        price_get = container.findAll("div",{"class":"col col-buy"})
        prodName=title_get[0].a["title"]
        prodPrice=price_get[0].ul.li.div.div.h3.text.strip()
        print( x, ")" , prodName ,"\n", "price=" , prodPrice ,"\n \n")
        f.write ( str(x) + ")" + ","  + prodName.replace("،","|") + "," + prodPrice + "," + "\n")
        x+=1
f.close()
print("*****************done*****************")
    
