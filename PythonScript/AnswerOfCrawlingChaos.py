# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 06:26:23 2016

@author: you
"""

p = [70, 152, 195, 284, 475, 612, 791, 896, 810, 850, 737, 1332, 1469, 1120, 1470, 832, 1785, 2196, 1520, 1480, 1449]

for i in range(len(p)):
    print(chr(int(p[i] / (i+1))),end="")
