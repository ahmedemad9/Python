#!/usr/bin/python3 
import re 

choice=int(input("enter choice"))

if choice == 1:
     fname="regex_sum_42.txt"
else :
     fname="regex_sum_872483.txt"

fh=open(fname)
oneLine=fh.read()
print(oneLine)
y=re.findall('[0-9]+',oneLine)
print("length of list=",len(y))
for i in range(0,len(y)):
     y[i]=int(y[i])
print(y)
print("sum of elements= ",sum(y))
