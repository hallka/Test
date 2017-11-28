# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 21:22:58 2016

@author: you
"""

n, x = input().split()
n = int(n)
x = int(x)
a = list(map(int, input().split()))

t = []
for i in range(len(a)):
    t.append(a[i])

i = 0
for i in range(len(a)):
    if a[i-1] + x < a[i] :
        a[i] = a[i-1] + x
i = 0
for i in range(len(a)):
    if a[i-1] + x < a[i] :
        a[i] = a[i-1] + x

cnt = 0
tmp = 0
ans = 0

i = 0
for i in range(len(a)):
    if a[i] != t[i] :
        tmp += 1
    else :
        if tmp > cnt :
            cnt = tmp
        tmp = 0
i = 0
for i in range(len(a)):
    if a[i] != t[i] :
        tmp += 1
    else :
        ans += a[i]
        if tmp > cnt :
            cnt = tmp
        tmp = 0
        
print(ans + cnt*x)