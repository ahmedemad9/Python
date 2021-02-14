#!/usr/bin/python3 

import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer as sip
from sklearn.preprocessing import OneHotEncoder, LabelEncoder , StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split

#read files
dataset = pd.read_csv('train.csv')
dataset_test=pd.read_csv('test.csv')


#fill nan values in train and test
#fill nan values by mean in train
dataset.iloc[: , 6:9 ]= sip(missing_values=np.nan,strategy='mean').fit_transform(dataset.iloc[: , 6:9 ])
dataset['Married'] = dataset['Married'].fillna(dataset['Married'].dropna().mode().values[0])
dataset['Gender'] = dataset['Gender'].fillna(dataset['Gender'].dropna().mode().values[0])
dataset['Loan_Amount_Term'] = dataset['Loan_Amount_Term'].fillna(dataset['Loan_Amount_Term'].dropna().mode().values[0])
dataset['Dependents'] = dataset['Dependents'].fillna(dataset['Dependents'].dropna().mode().values[0])
dataset['LoanAmount'] = dataset['LoanAmount'].fillna(dataset['LoanAmount'].dropna().mode().values[0])
dataset['Self_Employed'] = dataset['Self_Employed'].fillna(dataset['Self_Employed'].dropna().mode().values[0])
dataset['Credit_History'] = dataset['Credit_History'].fillna(dataset['Credit_History'].dropna().mode().values[0])
dataset['Property_Area'] = dataset['Property_Area'].fillna(dataset['Property_Area'].dropna().mode().values[0])

#fill nan values by mean in test
dataset_test.iloc[: , 6:9 ]= sip(missing_values=np.nan,strategy='mean').fit_transform(dataset_test.iloc[: , 6:9 ])
dataset_test['Married'] = dataset_test['Married'].fillna(dataset_test['Married'].dropna().mode().values[0])
dataset_test['Gender'] = dataset_test['Gender'].fillna(dataset_test['Gender'].dropna().mode().values[0])
dataset_test['Loan_Amount_Term'] = dataset_test['Loan_Amount_Term'].fillna(dataset_test['Loan_Amount_Term'].dropna().mode().values[0])
dataset_test['Dependents'] = dataset_test['Dependents'].fillna(dataset_test['Dependents'].dropna().mode().values[0])
dataset_test['LoanAmount'] = dataset_test['LoanAmount'].fillna(dataset_test['LoanAmount'].dropna().mode().values[0])
dataset_test['Self_Employed'] = dataset_test['Self_Employed'].fillna(dataset_test['Self_Employed'].dropna().mode().values[0])
dataset_test['Credit_History'] = dataset_test['Credit_History'].fillna(dataset_test['Credit_History'].dropna().mode().values[0])
dataset_test['Property_Area'] = dataset_test['Property_Area'].fillna(dataset_test['Property_Area'].dropna().mode().values[0])

code_numeric={'3+':3}
dataset = dataset.applymap(lambda s: code_numeric.get(s) if s in code_numeric else s)
dataset_test = dataset_test.applymap(lambda s: code_numeric.get(s) if s in code_numeric else s)

#fill x an y
#fill x and y in train
x = dataset.iloc[:,1:-1].values
y = dataset.iloc[:,-1].values
#fill x and y in test
x_test = dataset_test.iloc[:,1:].values


#encode x to zeroes and ones
#for train
labelencoder=LabelEncoder()
x[:,0]=labelencoder.fit_transform(x[:,0])
x[:,1]=labelencoder.fit_transform(x[:,1])
x[:,3]=labelencoder.fit_transform(x[:,3])
x[:,4]=labelencoder.fit_transform(x[:,4])
x= ColumnTransformer([("Property_Area", OneHotEncoder(), [-1])], remainder = 'passthrough').fit_transform(x)


#for test
labelencoder_test=LabelEncoder()
x_test[:,0]=labelencoder_test.fit_transform(x_test[:,0])
x_test[:,1]=labelencoder_test.fit_transform(x_test[:,1])
x_test[:,3]=labelencoder_test.fit_transform(x_test[:,3])
x_test[:,4]=labelencoder_test.fit_transform(x_test[:,4])
x_test= ColumnTransformer([("Property_Area", OneHotEncoder(), [-1])], remainder = 'passthrough').fit_transform(x_test)


#encode y to zeroes and ones
#encode y train to zeroes and ones
LE=LabelEncoder()
y=LE.fit_transform(y)

#take some values as training and predict output of some test cases
x_train , x_test_sv , y_train , y_test_sv = train_test_split(x,y,test_size=0.2)

#scale x and y to make them meaningful in calculations

SS=StandardScaler()
x_train = SS.fit_transform(x_train)
x_test_sv = SS.transform(x_test_sv)

from sklearn.metrics import confusion_matrix


from sklearn.svm import SVC
classifier=SVC(kernel='poly')
classifier.fit(x_train,y_train)
y_pred=classifier.predict(x_test_sv)

cm=confusion_matrix(y_test_sv , y_pred)
print("svc poly\n",cm)

from sklearn.linear_model import LogisticRegression
classifier=LogisticRegression()
classifier.fit(x_train,y_train)
y_pred=classifier.predict(x_test_sv)

cm=confusion_matrix(y_test_sv , y_pred)
print("LogisticRegression\n",cm)

from sklearn.neighbors import KNeighborsClassifier
classifier= KNeighborsClassifier(n_neighbors=15,metric='minkowski',p=2)
classifier.fit(x_train,y_train)
y_pred=classifier.predict(x_test_sv)

cm=confusion_matrix(y_test_sv , y_pred)
print("knn\n",cm)

from sklearn.ensemble import RandomForestClassifier
classifier=RandomForestClassifier(n_estimators=35,criterion='entropy')
classifier.fit(x_train,y_train)
y_pred=classifier.predict(x_test_sv)
cm=confusion_matrix(y_test_sv , y_pred)
print("RandomForestClassifier\n",cm)

