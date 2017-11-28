# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 02:57:44 2016

@author: you
"""

def fibo(n):
    if n==1 or n==0:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)


for a in range(0,10):
    if fibo(a)%15==0:
        print("FizzBuzz")
    elif fibo(a)%5==0:
        print("Buzz")
    elif fibo(a)%3==0:
        print("Fizz")
    else :
        print(fibo(a))
