# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 09:45:46 2018

@author: user
"""
str = input("Enter a word:")
lstr=str.lower()#converts given string to lowercase
newstr=""
for x in range(len(lstr)):
    if lstr[x]=='b':
        newstr+='v'#if the contains b then append the null string with v in place of b
        continue
    elif lstr[x]=='v':
        newstr+='b'#if the contains b then append the null string with v in place of b
        continue
    else:
        newstr+=lstr[x]
print(newstr)