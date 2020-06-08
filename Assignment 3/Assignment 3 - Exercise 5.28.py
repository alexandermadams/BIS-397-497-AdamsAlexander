# -*- coding: utf-8 -*-
"""

@author: Alex Adams
Assignment 3 Exercise 5.28
"""
survey = [1,2,5,4,3,5,2,1,3,3,1,4,3,3,3,2,3,3,2,5]

import statistics as s
import numpy as np

values, freq = np.unique(survey, return_counts=True)

for item in range(len(values)):
    print('Rating: ',values[item],' Appeared ',freq[item],' times'
          )
mi = np.min(freq)
print(f'Min is: {mi:.4f}')
    
ma = np.max(freq)
print(f'Max is: {ma:.4f}')

ra = ma-mi
print(f'Range is: {ra:.4f}')
    
me = s.mean(freq)
print(f'Mean is: {me:.4f}')
    
md = s.median(freq)
print(f'Mediam is: {md:.4f}')

mo = s.mode(freq)
print(f'Mode is: {mo:.4f}')
    
sd = s.stdev(survey)
print(f'Standard Deviation is: {sd:.4f}')
    
var = s.variance(freq)
print(f'Variance is: {var:.4f}')




