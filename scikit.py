# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 22:55:46 2018

@author: user
"""
from sklearn import svm
from sklearn import datasets
from sklearn import preprocessing
iris=datasets.load_iris()
clf=svm.LinearSVC()
x=clf.fit(iris.data,iris.target)
clf.predict([[10.0,13.6,5.3,3.25]])
vlt=clf.coef_
print(vlt)
X =iris.data
Y =iris.data
std_scale = preprocessing.StandardScaler().fit(X)
X_train_std = std_scale.transform(X)
print(X_train_std)
X_test_std  = std_scale.transform(Y)
print(X_test_std)
# Python script for confusion matrix creation.
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as pl
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
actual = [1, 1, 0, 1, 0, 4, 1, 0, 8, 0]
predicted = [1, 0, 0, 2, 0, 0, 7, 1, 1, 0]
results = confusion_matrix(actual, predicted)
print ('Confusion Matrix :')
print(results)
print('Accuracy Score :',accuracy_score(actual, predicted))
print('Report : ')
print(classification_report(actual, predicted))
pl.matshow(results)
pl.title('Confusion matrix')
pl.colorbar()
pl.show()
########
from sklearn.model_selection import cross_val_predict
from sklearn import datasets
from sklearn.svm.classes import SVC
iris=datasets.load_iris()
clf = SVC()
res = cross_val_predict(clf,iris.data,iris.target, cv=7)
print(res)
print('kumari')