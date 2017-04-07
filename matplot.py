# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 21:08:14 2017

@author: parithy
"""

import matplotlib.pyplot as plt

##x=[1,2,3]
##y=[5,10,8]
#
##x2 =[4,5,7]
##y2 =[20,21,25]
#population_ages = [22,55,62,45,21,22,34,42,42,4,99,102,110,120,121,122,130,111,115,112,80,75,65,54,44,43,42,48]
#
#bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]
#
##plt.bar(x,y ,label = 'first' , color='g')
##plt.bar(x2,y2,label= 'Second',  color='r')
#
#plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)

x = [1,2,3,4,5,6,7,8]
y = [5,2,4,2,1,4,5,2]

plt.scatter(x,y,label='Scatter', color='b' ,marker='x')

plt.xlabel('X-AXIS')
plt.ylabel('Y-AXIS')
plt.title('ILAM')
plt.legend()
plt.show()