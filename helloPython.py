#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test.py


'''
这是多行注释，使用单引号。
这是多行注释，使用单引号。
这是多行注释，使用单引号。
'''




class Test:
    def __init__(self):
        self.var = 0
        self._var = 1
        self.var_ = 2
        self._var_ = 3
        self.__var = 4
        self.var__ = 5
        self.__var__ = 6


t = Test()

print(t.var)

print(t._var)
print(t.var_)
print(t._var_)


"""
这是多行注释，使用双引号。
这是多行注释，使用双引号。
这是多行注释，使用双引号。
"""



print(t._Test__var)
print(t.var__)
print(t.__var__)
