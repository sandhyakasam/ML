# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 10:56:40 2018

@author: user
"""
from sklearn.linear_model import Ridge
import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split
from sklearn import preprocessing
import matplotlib.pyplot as plt
df=pd.read_csv('D:\/GOOGaug31.csv')
df = df[['Open','High','Low','Close','Volume']]
forecast_out = int(5) # predicting 1 days into future
df['Prediction'] = df[['Close']].shift(-1) #  label column with data shifted 1 units up

X = np.array(df.drop(['Prediction'], 1))
X = preprocessing.scale(X)

X_forecast = X[-forecast_out:] # set X_forecast equal to last 1
X = X[:-forecast_out]

y = np.array(df['Prediction'])
y = y[:-forecast_out]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3)
###################
ls =linear_model.Lasso(alpha=0.5) #alpha can be fine tuned
clf=ls.fit(X_train, y_train)
confidencels = clf.score(X_test, y_test)
print("#######################   LASSO RGRSN   #####################")
print("confidence: ", confidencels)
predicted1 = ls.predict(X_test)
forecast_predictionl = clf.predict(X_forecast)
print(forecast_predictionl)
print ('Mean Square Error Lasso')
mse_lasso = mean_squared_error(y_test, predicted1)  
print (mse_lasso)

###################
rd = Ridge(alpha=1)
clf=rd.fit(X_train, y_train)
confidenceri = clf.score(X_test, y_test)
print("#######################   RIDGE RGRSN   #####################")
print("confidence: ", confidenceri)
predicted2 = rd.predict(X_test)
forecast_predictionr = clf.predict(X_forecast)
print(forecast_predictionr)
print ('Mean Square Error Ridge')
mse_ridge = mean_squared_error(y_test, predicted2)  
print (mse_ridge)
####################
LR = LinearRegression()
clf=LR.fit(X_train, y_train)
confidencelr = clf.score(X_test, y_test)
print("#######################   LR RGRSN     ######################")
print("confidence: ", confidencelr)
predicted3 = LR.predict(X_test)
forecast_predictionlr = clf.predict(X_forecast)
print(forecast_predictionlr)
print ('Mean Square Error Linear Reg')
mse_lr = mean_squared_error(y_test, predicted3)  
print (mse_lr)  
#plt.plot(X_train,y_train,color='cyan')
#plt.scatter(X_test,LR.predict(X_test),color='red',linewidth=3)
#plt.xlabel('Open Price')
#plt.ylabel('Close Price')
#plt.show()

