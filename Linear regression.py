# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 12:02:30 2017

@author: parithy
"""

from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

#xs= np.array([1,2,3,4,5,6],dtype=np.float64)
#ys= np.array([5,4,6,5,6,7],dtype=np.float64)
xs= np.array([80],dtype=np.float64)
ys= np.array([500],dtype=np.float64)
def best_fit_slope(xs,ys):
    m =( ((mean(xs) * mean(ys)) - mean(xs * ys)) / 
            ((mean(xs)**2) - (mean(xs**2))) )
    
    b = (mean(ys) - (m * mean(xs)))
    
#    a= mean(xs) * mean(ys)
#    b=mean(xs*ys)
#    c= mean(xs)**2
#    d=mean(xs**2)
#    
#    slope = (a-b)/(c-d)
    return m ,b

m,b = best_fit_slope(xs,ys)
print(m)
regression_line = [ (m*x) + b for x in xs]
                   
plt.scatter(xs,ys)
plt.plot(xs , regression_line)
plt.show()
                   

#print(regression_line)



#
#plt.plot(xs,ys)
#plt.show()
