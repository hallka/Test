# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 14:05:32 2016

@author: you
"""
import time
x,y,z,w = (123456789,362436069,521288629,88675123)

arr = []

def randxs(a,b):
    global x,y,z,w
    t = (x^(x<<11))
    x,y,z = y,z,w
    w = (w^(w>>19))^(t^(t>>8))
    return (a+w)%b

def randxsa(a,b):
    global x,y,z,w
    t = (x^(x*2**1))
    x,y,z = y,z,w
    w = (w^(w/(2**3)))^(t^(t/(2**10)))
    return (a+w)%b

if __name__ == '__main__':
    start = time.time()

    for _ in range(1000):
        arr.append(randxs(0,100))

    elapsed_time = time.time() - start
        
    print(("elapsed_time(xs):{0}".format(elapsed_time)) + "[sec]")

    start = time.time()

    for _ in range(1000):
        arr.append(randxsa(0,100))

    elapsed_time = time.time() - start
        
    print(("elapsed_time(xs):{0}".format(elapsed_time)) + "[sec]")
