# -*- coding: utf-8 -*-
"""
Created on Wed May 15 01:10:36 2019

@author: 井上菌
"""

x = float(input("请输入x的值："))
if x > 1:
    y = 3*x-5
elif x < -1:
    y = 5*x+3
else:
    y = x + 2

print("y的值是：%f"% y)