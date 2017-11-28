# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 21:23:20 2016

@author: you
"""

str = input()
list = []

for w in range(len(str)):
    if ord(str[w]) in list :
        list.remove(ord(str[w]))
    else :
        list.append(ord(str[w]))

if len(list) == 0 :
    print('Yes')
else :
    print("No")
