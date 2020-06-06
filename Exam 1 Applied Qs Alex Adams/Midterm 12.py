# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 07:47:03 2020

@author: Alex Adams
BIS497 Exam 1 Applied Q12
"""

def descriptive(numbers):
    import statistics as s

    me = s.mean(numbers)
    print(f'Mean is: {me:.4f}')
    
    md = s.median(numbers)
    print(f'Mediam is: {md:.4f}')
    
    sd = s.stdev(numbers)
    print(f'Sample Standard Deviation is: {sd:.4f}')
    
    psd = s.pstdev(numbers)
    print(f'Population Standard Deviation is: {psd:.4f}')
    return [me,md,sd,psd]

import random as r
rannumlis = [r.random() for item in range(10)]
descriptive(rannumlis);
