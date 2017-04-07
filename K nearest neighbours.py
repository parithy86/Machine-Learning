# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 20:34:08 2017

@author: parithy
"""

import numpy as np
from sklearn import preprocessing,cross_validation, neighbors,svm

import pandas as pd

df=pd.read_csv('breast-cancer-wisconsin.data')
df.replace('?', -99999, inplace=True)
df.drop(['id'],1, inplace=True) 

X=np.array(df.drop(['class'],1))
y=np.array(df['class'])

X_train , X_test , y_train, y_test =cross_validation.train_test_split(X,y,test_size= 0.2)

clf=neighbors.KNeighborsClassifier()

clf.fit(X_train,y_train)
print(clf.score(X_test,y_test))

sample_data =np.array([[10,7,2,1,1,5,1,8,1],[4,1,2,90,1,2,1,5,1]])

sample_data =sample_data.reshape(len(sample_data),-1)

prediction =clf.predict(sample_data)
print(prediction)

clf=svm.SVC()

clf.fit(X_train,y_train)
print(clf.score(X_test,y_test))

#sample_data =np.array([[10,7,2,1,1,5,1,8,1],[4,1,2,90,1,2,1,5,1]])
#
#sample_data =sample_data.reshape(len(sample_data),-1)

prediction =clf.predict(sample_data)
print(prediction)