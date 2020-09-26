#!/usr/bin/python3 

fh=open("from.txt")
count=0
for line in fh :
     line.rstrip()
     if not line.startswith("From") or line.startswith("From:"):continue
     count+=1
     words=line.split()
     print(words[1])
