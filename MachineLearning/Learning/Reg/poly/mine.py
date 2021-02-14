#!/usr/bin/python3 
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer as sip
from sklearn.preprocessing import OneHotEncoder as ohe, LabelEncoder as le, StandardScaler as ss,PolynomialFeatures as pf
from sklearn.compose import ColumnTransformer as ct
from sklearn.model_selection import train_test_split as tts
from sklearn.linear_model import LinearRegression as lg 
import statsmodels.regression.linear_model as lm

#read file and split to dependant and independant
dataset = pd.read_csv('Position_Salaries.csv')
x = dataset.iloc[:,1:2].values
y = dataset.iloc[:,2:].values
"""
#fill nan values by mean
x[: , 1: ]= sip(missing_values=np.nan,strategy='mean').fit_transform(x[: , 1: ])
"""
#check dataset
print("dataset:\n" , dataset)
"""
#encode x to zeroes and ones
x = ct([('Country', ohe(), [3])], remainder = 'passthrough').fit_transform(x).astype('int')

#encode y to zeroes and ones
y=le().fit_transform(y)
"""
"""
#remove variable trap
x=x[:,1:]
"""
"""
#take some values as training and predict output of some test cases
x_train , x_test , y_train , y_test = tts(x,y,test_size=0.2,random_state=0)
"""
print("x:\n" ,x)

#to make linear regression
lin_reg=lg()
lin_reg.fit(x,y)

#to make polynomial regression
poly_reg=pf(degree=7)
x_poly=poly_reg.fit_transform(x)

lin_reg_2=lg()
lin_reg_2.fit(x_poly,y)

plt.scatter(x,y,color='red')
plt.plot(x,lin_reg.predict(x),color ='black')

x_grid=np.arange(min(x),max(x),0.01)
x_grid=x_grid.reshape(len(x_grid),1)
plt.scatter(x,y,color='red')
plt.plot(x_grid,lin_reg_2.predict(poly_reg.fit_transform(x_grid)),color='blue')

print("salary of 6.5 years exp :",lin_reg_2.predict(poly_reg.fit_transform(np.array([6.5]).reshape(1,1))))
"""
print("x_train before scaling:\n" , x_train)

print("x_test before scaling:\n" , x_test)
"""
#scale x and y to make them meaningful in calculations
"""SS=ss()
x_train = SS.fit_transform(x_train)
x_test = SS.transform(x_test)"""

#print("x_train after sclaing:\n" , x_train)

#print("x_test after scaling:\n" , x_test)

print("y:\n" ,y)
"""
print("y_train:\n" ,y_train)

print("y_test:\n" ,y_test)"""
