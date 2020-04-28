# -*- coding: utf-8 -*-
"""
Created on Tue May 28 01:04:16 2019

@author: 井上菌
"""
'''
from module import foo
foo()


from module2 import foo
foo()'''

import module as m1
import module as m2

m1.foo()
m2.foo()