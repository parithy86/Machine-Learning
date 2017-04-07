# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 19:58:19 2017

@author: parithy
"""
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandas_datareader.data as web
from matplotlib import style

style.use('ggplot')
ls_key = 'Adj Close'
ls_key2= 'stock price'
stock = ['FIT' ,'CSCO' ,'TTM' , 'BNCN']
stock_price_dict =np.array([['2015-12-02', 'CSCO', 30.59],['2015-12-02', 'TTM', 33.98],['2015-12-02', 'FIT', 7.55],['2015-12-02', 'BNCN', 32.00]])

#print (stock_price_dict)
#stock_price = [7.55,30.59,33.98,32.00]
#num_of_stock=[5,1,1,2]

start = dt.datetime(2010,1,1)
end=dt.datetime.now()
#end = dt.datetime(2017,2,28)

f=web.DataReader(stock,'yahoo', start, end)
print(type(f))
cleandata=f.ix[ls_key]
#print(type(cleandata))

df=pd.DataFrame(cleandata)
df1=df.tail(1)
print(df1)


#d= {'BNCN' : 30.24,'CSCO' : 20.20 ,'TTM' :12.00 }
#print(pd.Series(d))
d = {'BNCN' : pd.Series([32.00], index=[pd.to_datetime('2015-12-02')]),'CSCO' : pd.Series([30.59], index=[pd.to_datetime('2015-12-02')]),
     'TTM' : pd.Series([33.98], index=[pd.to_datetime('2015-12-02')]),'FIT' : pd.Series([7.55], index=[pd.to_datetime('2015-12-02')])}
     
df2=pd.DataFrame(d)

#df2=pd.DataFrame(stock_price_dict,columns=['Date1', 'stock_name', 'stock price'])
#
#df2=df2.set_index('Date1')
#
##print(df2.iloc[:0,2])
##df3=(df2.T)
#print(df2)
##
#
##
##print(df1)
#df5=(df4.tail(1))
#print(df1)
#print(df5)
#
df3=pd.concat([df1,df2])
###print(df6)
##
print(df3)
#plt.figure()
#df3.plot()
df3.plot.bar()
##print(df6)
#
#plt.scatter(df1,df2)
plt.show()