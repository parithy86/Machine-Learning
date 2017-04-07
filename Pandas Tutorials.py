# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 20:17:02 2017

@author: parithy
"""
python
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

#web_stats = {'Day':[1,2,3,4,5,6],
#             'visitors':[43,53,56,23,23,60],
#             'Bounce_rate':[65,67,80,69,98,12]}
#             
#df = pd.DataFrame(web_stats)

df = pd.read_csv('C:\\Users\\parithy\\Desktop\\ZILL-Z85027_LPC.csv', index_col =0)

print(df.head())

#df.set_index('Date' , inplace=True)
#
#print(df.head())

df.columns = ['Phoenix HPI']
print(df.head())