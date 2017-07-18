#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 22:43:22 2017

@author: mmonforte
"""

def genPrimes():
    primes = []
    last = 1
    
    while True:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            yield last