#!/usr/bin/python3 
"""This python script is to extract the successful codes from your hackerRank.com json file and separate them to distinct files where each file contains one program and categorized to folders according to the programming language, You may need to add the extension of your programing language if you aren't using (cpp / python3 / python2 /python)
You have to put the script and the unzipped json file in the same directory
You may need to remove the first line if you aren`t a linux user or edit if you installed python 3 in a different directory
The code overwrites duplicates since later codes are more optimized and improved 
spaces are replaced with underscores to name the file
folder is named after the programming language"""

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
