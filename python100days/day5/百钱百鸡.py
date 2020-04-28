# -*- coding: utf-8 -*-
"""
Created on Sun May 26 14:20:38 2019

@author: 井上菌
"""

for x in range(0,33):
    for y in range(0,20):
        z = 100 - x - y
        if 9*x + 15*y + z ==300:
            print("母鸡有%d只，公鸡有%d只，小鸡有%d只"%(x,y,z))