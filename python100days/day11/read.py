# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 10:34:19 2019

@author: 井上菌
"""

#import time
def main():
    with open("致橡树.txt","r",encoding='utf-8') as f:
        print(f.read())
        
    with open(r"致橡树") as f:
        for line in f:
            print(line,end='')
           # time.sleep(0.5)
           
    print()
    
    with open("致橡树.txt") as f:
        lines = f.readlines()
    print(lines)
    

if __name__ == '__main__':
    main()