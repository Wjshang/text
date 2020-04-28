# -*- coding: utf-8 -*-
"""
Created on Sun May 26 12:24:42 2019

@author: 井上菌
"""

for n in range(100,1000):
    if ((n//100)**3 + (n//10%10)**3 + (n%10)**3) == n:
        print(n)