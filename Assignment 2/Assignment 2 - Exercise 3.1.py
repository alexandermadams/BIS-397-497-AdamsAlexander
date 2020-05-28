# -*- coding: utf-8 -*-

"""Homework Problem 3.1
Alex Adams
Summer BIS497
"""

passes = 0
failures = 0

for student in range(10):
    
    result = 0
    while result != 1 and result != 2:
        result = int(input('Enter result (1=pass, 2=fail: '))
   
    if result == 1:
        passes = passes+1

failures = 10-passes