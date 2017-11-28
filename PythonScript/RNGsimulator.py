# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 04:11:00 2016

@author: you
"""

import time
import random

arrn = [[],[],[]]
arrt = [[],[],[]]

x,y,z,w = (50,60,70,80)

seedlcg = 1

def randxs(a,b):
    global x,y,z,w
    t = (x^(x<<1))
    x,y,z = y,z,w
    w = (w^(w>>3))^(t^(t>>10))
    return (a+w)%b

def randlcg():
    global seedlcg
    seedlcg = (13 * seedlcg + 1) % 101
    return seedlcg

def srandlcg(a):
    global seedlcg
    seedlcg = a

if __name__ == '__main__':

    for i in range(10):
        start = time.time()
    
        srandlcg(int(time.time()))
        for _ in range(10000):
            arrn[0].append(randlcg())            
    
        elapsed_time = time.time() - start
        arrt[0].append(elapsed_time)
        
    print(("elapsed_time(lcg):{0}".format(sum(arrt[0])/len(arrt[0]))) + "[sec]")    

    for i in range(10):
        start = time.time()
    
        for _ in range(10000):
            arrn[1].append(random.randint(0,100))            
    
        elapsed_time = time.time() - start
        arrt[1].append(elapsed_time)
        
    print(("elapsed_time(mt):{0}".format(sum(arrt[1])/len(arrt[1]))) + "[sec]")    

    for i in range(10):
        start = time.time()
    
        for _ in range(10000):
            arrn[2].append(randxs(0,100))            
    
        elapsed_time = time.time() - start
        arrt[2].append(elapsed_time)
        
    print(("elapsed_time(xs):{0}".format(sum(arrt[2])/len(arrt[2]))) + "[sec]")    
