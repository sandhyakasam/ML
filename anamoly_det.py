# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 11:18:01 2018

@author: user
"""
import matplotlib.pyplot as plt
import numpy as np
#%matplotlib inline
import pandas as pd
from scipy.stats import multivariate_normal
from sklearn.metrics import f1_score
df = pd.read_csv('D:\lnrreg\/MSFToneyr.csv',header=0)
dff=df.drop(['Date'], axis=1)

def feature_normalize(dataset):
    mu = np.mean(dataset,axis=0)
    sigma = np.std(dataset,axis=0)
    return (dataset - mu)/sigma

def estimateGaussian(dataset):
    mu = np.mean(dataset, axis=0)
    sigma = np.cov(dataset.T)
    return mu, sigma
    
def MultivariateGaussianDistribution(data,mu,sigma):
    p = multivariate_normal.pdf(data, mean=mu, cov=sigma)
    p_transformed = np.power(p,1/100) #transformed the probability scores by p^1/100 since the values are very low (up to e-150)
    return p_transformed
def selectThresholdByCV(probs,gt):
    best_epsilon = 0
    best_f1 = 0
    f = 0
    stepsize = (max(probs) - min(probs)) / 1000;
    epsilons = np.arange(min(probs),max(probs),stepsize)
    for epsilon in np.nditer(epsilons):
        predictions = (probs < epsilon)
        f = f1_score(gt, predictions, average = "binary")
        if f > best_f1:
            best_f1 = f
            best_epsilon = epsilon
    return best_f1, best_epsilon
n_training_samples = df.shape[0]
n_dim = df.shape
plt.figure()
plt.xlabel("date")
plt.ylabel("volume")
plt.plot(df.iloc[:,0],df.iloc[:,1],"bx")
plt.show()
mu, sigma = estimateGaussian(dff)
p = MultivariateGaussianDistribution(dff,mu,sigma)
#p_cv = multivariateGaussian(cv_data,mu,sigma)
fscore, ep = selectThresholdByCV(x_test,y_test)
ep=0.05
outliers = np.asarray(np.where(p < ep))
plt.figure() 
plt.plot(df.iloc[:,0],df.iloc[:,1],"bx") 
plt.plot(df[outliers,0],df[outliers,1],"ro") 
plt.show()