# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 10:39:24 2019

@author: 井上菌
"""

class Test:

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    test = Test('hello')
    test._Test__bar()
    print(test._Test__foo)


if __name__ == "__main__":
    main()
