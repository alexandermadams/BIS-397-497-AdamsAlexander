# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 13:53:08 2020

HW Exercise 7.20
Alex Adams

"""

import numpy as np
import random

def avtl(length):
    objl = %timeit -o rl = [random.randrange(1,7) for i in range(0,length)];
    return objl.average

def avta(length):
    obja = %timeit -o ra = np.random.randint(1,7,length);
    return obja.average


tl = []
ta = []
for i in range(7):
    numvals = 10**i
    tl.append(avtl(numvals))
    ta.append(avta(numvals))

print('Length    ','List(s)      ','Array(s)     ')
for i in range(7):
    print(f'{10**i:<11.0f}{tl[i]:<10f} {ta[i]:<10f}')

