# -*- coding: utf-8 -*-
"""
Created on Tue May 21 20:53:01 2019

@author: 井上菌
"""

from math import sqrt

x = int(input("请输入一个数："))

n = int(sqrt(x)) + 1

counter = 1
for a in range(2,n):
    if x % a == 0:
        #print("%d不是素数"%x)
        break
    counter +=1
    
if counter == n-2:
    print("%d不是素数"%x)
else:
    print("%d是素数"%x)
    