# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 21:42:33 2016

@author: you
"""

n, a = input().split()
n = int(n)
a = int(a)
x = input().split()
for k in range(len(x)):
    x[k] = int(x[k])

ans = 0
cnt = 0

for i in range(n):
    ans = x[i]
    j = i+1
    for j in range(n) :
        if ans == a:
            cnt += 1
            ans = x[j]
        elif (ans-a) * (x[j] - a) > 0:
            continue
        else :
            ans += x[j]

print(cnt)