#!/usr/bin/python3 
import csv
import numpy as np
import pandas as pd
import matplotlib as plt
from sklearn.impute import SimpleImputer as sip
from sklearn.preprocessing import OneHotEncoder as ohe, LabelEncoder as le, StandardScaler as ss
from sklearn.compose import ColumnTransformer as ct
from sklearn.model_selection import train_test_split as tts
from sklearn.linear_model import LinearRegression 
import statsmodels.regression.linear_model as lm

#read file and split to dependant and independant
dataset = pd.read_csv('50_Startups.csv')
x = dataset.iloc[:,0:-1].values
y = dataset.iloc[:,4].values
"""
#fill nan values by mean
x[: , 1: ]= sip(missing_values=np.nan,strategy='mean').fit_transform(x[: , 1: ])
"""
#check dataset
print("dataset:\n" , dataset)

#encode x to zeroes and ones
x = ct([('Country', ohe(), [3])], remainder = 'passthrough').fit_transform(x).astype('int')
"""
#encode y to zeroes and ones
y=le().fit_transform(y)
"""

#remove variable trap
x=x[:,1:]

#take some values as training and predict output of some test cases
x_train , x_test , y_train , y_test = tts(x,y,test_size=0.2,random_state=0)

print("x:\n" ,x)

print("x_train before scaling:\n" , x_train)

print("x_test before scaling:\n" , x_test)

#scale x and y to make them meaningful in calculations
"""SS=ss()
x_train = SS.fit_transform(x_train)
x_test = SS.transform(x_test)"""

regressor=LinearRegression()
regressor.fit(x_train,y_train)
y_pred = regressor.predict(x_test)
print("y_pred: \n",y_pred)

x=np.append(np.ones((50,1),dtype=np.int) , values=x , axis=1)
print("x after append:\n",x)


x_opt = x[:,[0,3,5]]
regressor_ols = lm.OLS(endog=y , exog = x_opt).fit()
summary=regressor_ols.summary()
print("summary:\n",summary)
#print("x_train after sclaing:\n" , x_train)

#print("x_test after scaling:\n" , x_test)

"""print("y:\n" ,y)

print("y_train:\n" ,y_train)

print("y_test:\n" ,y_test)"""
