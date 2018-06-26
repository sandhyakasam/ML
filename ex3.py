# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 09:53:07 2018

@author: user
"""

def check_validity(password):
    ''' Return True if input pw is valid, and return False if invalid.'''
    if isinstance(password, str) \
            or not all(isinstance(c, str) for c in password):
        return False
    if len(password) < 6:
        return False
        password = set(password)
    checks = [
        set(str.ascii_lowercase),
        set(str.ascii_uppercase),
        set(str.digits),
        {'$', '#', '@'},
    ]
    for check in checks:
        if not check & password:
            return False
    return True
pwd=input("input ur pwd:")
check_validity(pwd)
#######
fname = input("Enter file name: ") #enter the path of the text file (path\txtfilename.txt)
num = 0  
with open(fname, 'r') as f: #
    for line in f:
        words = line.split()
        num += len(words)
print("Number of words:")
print(num)   
######## 
fname = input("Enter file name: ") 
places = ['Berlin', 'Cape Town', 'Sydney', 'Moscow']
fh=open('fname', 'w')   
    for listitem in places:
        filehandle.write('%s\n' % listitem)