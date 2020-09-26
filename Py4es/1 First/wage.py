#!/usr/bin/python3 
hrs=input("Enter Hours:")
rate = input("Enter rate:")

if float(hrs)<=40 :
     wage=float(hrs)*float(rate)
            
elif float(hrs)>40 :
     wage=(1.5*(float(hrs)-40)+float(hrs))*float(rate)
                
     print(wage)
