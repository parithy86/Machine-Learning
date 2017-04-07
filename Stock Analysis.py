# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 19:12:41 2017

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
stock_price_dict = {'CSCO': 30.59,'TTM':33.98,'FIT':7.55, 'BNCN': 32.00}




def get_latest_price(stock):
    start = dt.datetime(2017,1,1)
    end=dt.datetime.now()
    f=web.DataReader(stock,'yahoo', start, end)
    cleandata=f.ix[ls_key]
    df=pd.DataFrame(cleandata)
    df3=df.tail(1)
#    df3=df3.T
#    df3=df3.ix[0:,0]  
    print(df3)
    return df3
    
    
def get_purchase_price(stock_price_dict):
    date=pd.date_range(dt.datetime(2017,1,1) ,dt.datetime.now() )
    df2=pd.DataFrame(stock_price_dict,index=date)
    df2=df2.tail(1)
    return df2

if __name__ == "__main__" :
    stock = ['FIT' ,'CSCO' ,'TTM' , 'BNCN']
    get_latest_price(stock)
    
    get_purchase_price(stock_price_dict)
    df4=df3.join(df2)
    print(df4.dropna())
    
    
    
#    print(pd.concat([df1,df3]))

    
     