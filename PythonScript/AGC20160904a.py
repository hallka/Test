# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 21:05:54 2016

@author: you
"""

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

n = [a,b,c]

n.sort(reverse=True)

x = n[1] * n[2]

for i in range(3):
    if n[i] % 2 == 0:
        x = 0

print(x)
