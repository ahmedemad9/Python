#!/usr/bin/python3
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer as sip
from sklearn.preprocessing import OneHotEncoder as ohe, LabelEncoder as le, StandardScaler as ss
from sklearn.compose import ColumnTransformer as ct
from sklearn.model_selection import train_test_split as tts
from sklearn.linear_model import LinearRegression as lg

#read file and split to dependant and independant
dataset = pd.read_csv('Salary_Data.csv')
x = dataset.iloc[:,0:-1].values
y = dataset.iloc[:,1].values

#fill nan values by mean
"""x[: , 1: ]= sip(missing_values=np.nan,strategy='mean').fit_transform(x[: , 1: ])"""

#check dataset
print("dataset:\n" , dataset)

#encode x to zeroes and ones
"""x = ct([('Country', ohe(), [0])], remainder = 'passthrough').fit_transform(x)

#encode y to zeroes and ones
y=le().fit_transform(y)"""

#take some values as training and predict output of some test cases
x_train , x_test , y_train , y_test = tts(x,y,test_size=0.2,random_state=0)
LinReg=lg()
LinReg.fit(x_train,y_train)

y_predict=LinReg.predict(x_test)
y_predict_train=LinReg.predict(x_train)

plt.scatter(x_train,y_train,color='red')
plt.plot(x_train,y_predict_train,color='blue')
plt.plot(x_train,LinReg.predict(x_train),color='blue')
plt.show()

plt.scatter(x_test,y_test,color='black')
plt.plot(x_train,y_predict_train,color='orange')
plt.plot(x_train,LinReg.predict(x_train),color='blue')
plt.show()

print("x:\n" ,x)

print("x_train before scaling:\n" , x_train)

print("x_test before scaling:\n" , x_test)

#scale x and y to make them meaningful in calculations
"""SS=ss()
x_train = SS.fit_transform(x_train)
x_test = SS.transform(x_test)"""

print("x_train after sclaing:\n" , x_train)

print("x_test after scaling:\n" , x_test)

print("y:\n" ,y)

print("y_train:\n" ,y_train)

print("y_test:\n" ,y_test)

print("y_predict=\n",y_predict)
 

print("done")
