# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 21:42:33 2016

@author: you
"""

n = int(input())
a = list(map(int, input().split()))
colornum = 0
colorflag = [0,0,0,0,0,0,0,0]
rainbow = 0
maxvalue = 0
minvalue = 0
for i in range(n):
    if colorflag[0] == 0 and a[i] < 400:
        colornum = colornum + 1
        colorflag[0] = 1
    elif colorflag[1] == 0 and a[i] >= 400 and a[i] < 800:
        colornum = colornum + 1
        colorflag[1] = 1
    elif colorflag[2] == 0 and a[i] >= 800 and a[i] < 1200:
        colornum = colornum + 1
        colorflag[2] = 1
    elif colorflag[3] == 0 and a[i] >= 1200 and a[i] < 1600:
        colornum = colornum + 1
        colorflag[3] = 1
    elif colorflag[4] == 0 and a[i] >= 1600 and a[i] < 2000:
        colornum = colornum + 1
        colorflag[4] = 1
    elif colorflag[5] == 0 and a[i] >= 2000 and a[i] < 2400:
        colornum = colornum + 1
        colorflag[5] = 1
    elif colorflag[6] == 0 and a[i] >= 2400 and a[i] < 2800:
        colornum = colornum + 1
        colorflag[6] = 1
    elif colorflag[7] == 0 and a[i] >= 2800 and a[i] < 3200:
        colornum = colornum + 1
        colorflag[7] = 1
    elif a[i] >= 3200:
        rainbow = rainbow + 1
for j in range(8):
    if colorflag[j] == 1:
        minvalue = minvalue + 1
maxvalue = minvalue + rainbow
if minvalue == 0:
    minvalue = 1
    maxvalue = rainbow
print(minvalue,maxvalue)
