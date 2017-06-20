#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 20:52:38 2017

@author: mmonforte
"""

def fib(n):
    global numFibCalls
    numFibCalls += 1
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n-1) + fib(n-2)
    

def fib_efficient(n, d):
    global numFibCalls
    numFibCalls += 1
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
        return ans


fibArg = 34
numFibCalls = 0

print('')
print('Fibonacci total: ', fib(fibArg))
print('Number of calls needed to complete: ', numFibCalls)

numFibCalls = 0
d = {1:1, 2:2}

print('')
print('Fibonacci total: ', fib_efficient(fibArg, d))
print('Number of calls needed to complete: ', numFibCalls)