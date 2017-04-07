# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 20:38:27 2017

@author: parithy
"""
from sklearn import tree
feature =[[140,0],[130,0],[150,1], [170,1]]
lables =['apple','apple','orange','orange']

clf=tree.DecisionTreeClassifier()
clf =clf.fit(feature, lables) 
print (clf.predict([[140,1]]))