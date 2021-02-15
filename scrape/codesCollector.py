#!/usr/bin/python3 
import os
import json

def langToExt(lang):
    switcher={
        "c":"c",    
        "cpp":"cpp",
        "python3":"py",
        "python2":"py",
        "python":"py"
        #add more programming languages and their extensions here preceded by comma 
            }
    return switcher.get(lang,"nothing")

json_name=input("Enter hackerRank username: ")
parentFolder= os.getcwd()
openFile=open(json_name+"_data.json")
reader=json.load(openFile)

for i in reader['submissions']:
    if i["language"] not in os.listdir(parentFolder):
        os.chdir(parentFolder)
        os.mkdir(i["language"])
    os.chdir(parentFolder+"/"+i["language"])
    if i["score"]==1:
        opFile=open(i["challenge"].replace(" ","_").replace("-","_")+"."+langToExt(i["language"]),"w")
        opFile.write(i["code"])
        opFile.close()
print("Process done")
