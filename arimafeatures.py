# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 11:09:21 2018

@author: user
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import acf, pacf
import statsmodels.tsa.stattools as ts
from statsmodels.tsa.arima_model import ARIMA
#from datetime import datetime
df = pd.read_csv('D:\lnrreg\/ARTL.csv')
def arima(feature):
    price=feature
    plt.plot(price)
    lnprice=np.log(price)
    lnprice
    plt.plot(lnprice)
    plt.show()
    acf_1 =  acf(lnprice)[1:20]
    plt.plot(acf_1)
    plt.show()
    test_df = pd.DataFrame([acf_1]).T
    test_df.columns = ['Pandas Autocorrelation']
    test_df.index += 1
    test_df.plot(kind='bar')
    pacf_1 =  pacf(lnprice)[1:20]
    plt.plot(pacf_1)
    plt.show()
    test_df = pd.DataFrame([pacf_1]).T
    test_df.columns = ['Pandas Partial Autocorrelation']
    test_df.index += 1
    test_df.plot(kind='bar')
    result = ts.adfuller(lnprice, 1)
    result
    lnprice_diff=lnprice-lnprice.shift()
    diff=lnprice_diff.dropna()
    acf_1_diff =  acf(diff)[1:20]
    test_df = pd.DataFrame([acf_1_diff]).T
    test_df.columns = ['First Difference Autocorrelation']
    test_df.index += 1
    test_df.plot(kind='bar')
    pacf_1_diff =  pacf(diff)[1:20]
    plt.plot(pacf_1_diff)
    plt.show()
###########
    price_matrix=lnprice.as_matrix()
    model = ARIMA(price_matrix, order=(1,1,1))
    model_fit = model.fit(disp=0)
    print(model_fit.summary())
#plt.title('RSS: %.4f'% sum((model.fit-price)**2))
#    predictions=model_fit.predict(254,304, typ='levels')
#    predictions
#    predictionsadjusted=np.exp(predictions)
#    predictionsadjusted
    forecast=model_fit.forecast(steps=10)[0]
    fore=np.exp(forecast)
    forecast_ARIMA = pd.DataFrame(fore, copy=True)
    print(forecast_ARIMA.head())
    z = fore.tolist()
    price1 = pd.concat([pd.Series(price),pd.Series(z)], ignore_index = True, copy = True)
    print(price1.tail())
    #%matplotlib inline
    fig, ax = plt.subplots(1, 1)
    price1.plot(ax=ax,color='k',label='actual')
    price1.iloc[65:].plot(ax=ax,color='r',label='forecasted')
    plt.xlabel('index') 
    plt.title('actual & forecasted open')
    plt.legend()
    dff = pd.read_csv('D:\lnrreg\/artl15.csv')
    dff['Open']
    plt.plot(dff['Open'])
    plt.plot(forecast_ARIMA)
#arima(df['Volume'])
arima(df['Open'])
#arima(df['Close'])
#arima(df['Adj Close'])
#arima(df['High'])
#arima(df['Low'])
