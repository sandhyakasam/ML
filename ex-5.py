# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 14:14:02 2018

@author: user
"""

import numpy as np
a = np.array([1.0,-2.5,3,4,5.6,-6.7])
print(a)
b= np.ceil(a)
print(b.astype(int))
c= np.floor(a)
print(c.astype(int))
d= np.trunc(a)
print(d.astype(int))
############2#########
import numpy as np
a = np.array([[11,2,6],
              [4,8,10],
              [90,18,17]])
a.mean(axis=1)
##########
a = np.array([[11,2,6],
              [4,8,10],
              [90,18,17]])
b = np.eye(3,dtype=complex)
print(np.dot(a,b))
###########
import numpy as np
c1 = (1,2,3)
c2 = (3,12,1)
summ = np.polyadd(c1,c2) 
print(summ)
########
import numpy as np
c1 = (1,12,3)
c2 = (3,2,11)
sub=np.polysub(c1,c2)
print(sub)
#######
import numpy as np
c1 = (10,25,3)
c2 = (30,2,1)
div=np.polydiv(c1,c2)
print(div)
#######
import numpy as np
c1 = (18,12,35)
c2 = (3,12,11)
mul=np.polymul(c1,c2)
print(mul)
##############
import numpy as np
print("sine: array of angles given in degrees")
print(np.sin(np.array((0., 30., 45., 60., 90.)) * np.pi / 180.))
print(np.cos(np.array((0., 30., 45., 60., 90.)) * np.pi / 180.))
print(np.tan(np.array((0., 30., 45., 60., 90.)) * np.pi / 180.))
############6
import numpy as np
import calendar
calendar.monthrange(2018,6)[1]  #(yr,mnth)[date]
###
import numpy as np
print("Number of days,setember, 2018: ")
print(np.datetime64('2018-10-01') - np.datetime64('2018-09-01'))