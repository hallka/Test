# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 21:09:30 2016

@author: you
"""

n = int(input())
k = int(input())
x = int(input())
y = int(input())

price = 0

for i in range(n):
    if i < k :
        price += x
    else :
        price += y

print(price)