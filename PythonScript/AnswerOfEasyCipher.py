# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 03:26:16 2016

@author: you
"""

dis = 13

str = input()

for s in range(len(str)):
    if ord(str[s]) >= 65 and ord(str[s]) <= 90:
        ans = ord(str[s]) - dis
        if ans < 65: ans = ord(str[s]) + dis
        print(chr(ans),end="")
    elif ord(str[s]) >= 97 and ord(str[s]) <= 122:
        ans = ord(str[s]) - dis
        if ans < 97 : ans = ord(str[s]) + dis
        print(chr(ans),end="")        