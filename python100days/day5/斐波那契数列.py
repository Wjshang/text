# -*- coding: utf-8 -*-
"""
Created on Sun May 26 14:32:21 2019

@author: 井上菌
"""

a = 0
b = 1
for c in range(0,20):
    (a, b) = (b, a + b)
    print(a)