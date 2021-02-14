#!/usr/bin/python3 

import csv
import numpy as np
import pandas as pd
import matplotlib as plt
from sklearn.impute import SimpleImputer as sip
from sklearn.preprocessing import OneHotEncoder as ohe, LabelEncoder as le, StandardScaler as ss
from sklearn.compose import ColumnTransformer as ct
from sklearn.model_selection import train_test_split as tts

#read file and split to dependant and independant
dataset = pd.read_csv('Data.csv')
x = dataset.iloc[:,0:-1].values
y = dataset.iloc[:,3].values

#fill nan values by mean
x[: , 1: ]= sip(missing_values=np.nan,strategy='mean').fit_transform(x[: , 1: ])

#check dataset
print("dataset:\n" , dataset)

#encode x to zeroes and ones
x = ct([('Country', ohe(), [0])], remainder = 'passthrough').fit_transform(x)

#encode y to zeroes and ones
y=le().fit_transform(y)

#count nan
"""total = dataset.isnull().sum().sort_values(ascending=False)
percent = (dataset.isnull().sum()/dataset.isnull().count()).sort_values(ascending=False)*100
missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
missing_data.head(20)
print("total :\n",missing_data)
"""

#take some values as training and predict output of some test cases
x_train , x_test , y_train , y_test = tts(x,y,test_size=0.2,random_state=0)

print("x:\n" ,x)

print("x_train before scaling:\n" , x_train)

print("x_test before scaling:\n" , x_test)

#scale x and y to make them meaningful in calculations
SS=ss()
x_train = SS.fit_transform(x_train)
x_test = SS.transform(x_test)

print("x_train after sclaing:\n" , x_train)

print("x_test after scaling:\n" , x_test)

print("y:\n" ,y)

print("y_train:\n" ,y_train)

print("y_test:\n" ,y_test)

X_set,y_set=x_train,y_train
X1,X2=np.meshgrid(np.arange(start=X_set[:,0].min()-1,stop=X_set[:,0].max()+1,step=0.01),np.arange(start=X_set[:,1].min()-1,stop=X_set[:,1].max()+1,step=0.01))
plt.contourf(X1,X2,classifier.predict(np.array([X1.ravel(),X2.ravel()]).T).reshape(X1.shape),alpha=0.75,cmap=ListedColormap(('red','green')))
plt.xlim(X1.min(),X1.max())
plt.ylim(X2.min(),X2.max())
for i,j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set==j,0],X_set[y_set==j,1],c=ListedColormap(('red','green'))(i))
    plt.show()
