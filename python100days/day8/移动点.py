# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 23:17:25 2019

@author: 井上菌
"""

from math import sqrt

class Point(object):
    
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        
    def move_to(self,x,y):
        self.x = x
        self.y = y
        
    def move_by(self,dx,dy):
        self.x += dx
        self.y += dy
        
    def dis(self,other):
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx**2 + dy**2)
    
    def __str__(self):
#        return '(%s, %s)' % (str(self.x), str(self.y))
        return '(%d, %d)' % (self.x, self.y)
    
def main():
    p1=Point(3,5)
    p2=Point()
    print(p1)
    print(p2)
    p2.move_by(-1,2)
    print(p2)
    print(p1.dis(p2))
    
    
if __name__ == '__main__':
    main()
    