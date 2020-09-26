#!/usr/bin/python3 

fh=open("romeo.txt")
temp=[]
lst=[]

for line in fh:
     temp=line.split()
     temp.sort()
     for a in temp:
         if a not in lst:
            lst.append(a)

print(lst)
