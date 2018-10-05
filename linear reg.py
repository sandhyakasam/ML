# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 07:20:02 2018

@author: user
"""
##############lr using sklearn
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
from sklearn import preprocessing,cross_validation
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import cross_val_score
from sklearn.preprocessing import StandardScaler
df=pd.read_csv("E:\/AMZN.csv")
print(df)
x=df[['Open','Close','High','Low']]
y=df['Open']

x=preprocessing.scale(x)
y=preprocessing.scale(y)
#x=x.values.reshape(len(x),1)
#y=y.values.reshape(len(y),1)
x_train,x_test,y_train,y_test=cross_validation.train_test_split(x,y,test_size=0.2,
                                                   random_state=0)
#scalerX = StandardScaler().fit(x_train)
#y_train = np.asanyarray(y_train)
#y_train = y_train.apply(lambda x: pd.to_numeric(x,errors='ignore'))
#scalery = StandardScaler().fit(y_train)
#x_train = scalerX.transform(x_train)
#y_train = scalery.transform(y_train)
#x_test = scalerX.transform(x_test)
#y_test = scalery.transform(y_test)

regr = LinearRegression()
regr.fit(x_train,y_train) #train the model using train sets
y_pred=regr.predict(np.array([[1903,1886.52,1905,1883.55],[1898.5,1896.2,1925,1893.67]]).reshape(2,4))
y_new_inverse = scalery.inverse_transform(y_pred)
predictions = regr.predict(x_test)
pl.scatter(x_test,y_test,color='cyan')
pl.plot(x_test,regr.predict(x_test),color='red',linewidth=3)
pl.xlabel('Open Price')
pl.ylabel('Close Price')
pl.show()
print('predictions using lr in sklearn '+'\n',predictions)
Score=regr.score(x,y)
print('Score=',Score)
#print('Cofficients'+'\n',regr.coef_)

