# -*- coding: utf-8 -*-
"""
Created on Sun May 26 13:40:31 2019

@author: 井上菌
"""

for n in range(2,10000):
    counter = 0
    for a in range(1,n+1):
        if n % a == 0:
            counter = counter + a
        if (counter == n)  and (a > n//2):
            print(counter)
            break
         
   # print(counter)