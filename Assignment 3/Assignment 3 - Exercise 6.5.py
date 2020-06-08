# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 13:53:08 2020

@author: alexa
"""


text = 'This is a sentence that repeats itself a few times within the times of this sentence'

text = text.lower()

word_counts = {}

for word in text.split():
    if word in word_counts:
        word_counts[word]+=1
    else:
        word_counts[word] = 1
        
numdup = 0

for word, count in word_counts.items():
    if count >1:
        numdup = numdup+1
   
print('There are ',numdup, 'duplicates in this sentence.')