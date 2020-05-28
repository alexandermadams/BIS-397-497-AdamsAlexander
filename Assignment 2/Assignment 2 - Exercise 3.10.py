# -*- coding: utf-8 -*-
"""
Homework Problem 2.12
Alex Adams
Summer BIS497

"""
p = 1000
r = .07

for years in range(30):
    thisyear = years+1
    print(f' ${p:.2f} invested for {thisyear} years at {r*100:.0f}% interest is worth: ${p*(1+r)**thisyear:.2f}')
    
  
