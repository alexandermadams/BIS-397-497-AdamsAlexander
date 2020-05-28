# -*- coding: utf-8 -*-
"""
Homework Problem 2.12
Alex Adams
Summer BIS497

"""
p = 1000
r = .07

for years in [10, 20, 30]:
    print(f' ${p:.2f} invested for {years} years at {r*100:.0f}% interest is worth: ${p*(1+r)**years:.2f}')
    
  
