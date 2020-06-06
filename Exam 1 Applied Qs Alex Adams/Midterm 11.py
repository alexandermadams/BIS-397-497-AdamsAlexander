# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 07:47:03 2020

@author: Alex Adams
BIS497 Exam 1 Applied Q11
"""

import random

# roll dice first time and display
curdice =[]
for num in range(5):
    singdie = random.randrange(1,7)
    curdice.append(singdie)
    print(curdice[num],' ', end='')

#get string input from player for which dice to reroll
dstr = input('Enter the dice numbers to reroll on second turn.\nEnter without spaces(eg: 145) :')

#reroll selected dice
for num in range(len(dstr)):
    curdice[int(dstr[num])-1] = random.randrange(1,7)
    
#display the dice list
for num in range(5):
    print(curdice[num],' ', end='')

#get string input from player for which dice to reroll
dstr = input('Enter the dice numbers to reroll on third turn.\nEnter without spaces(eg: 145) :')

#reroll selected dice
for num in range(len(dstr)):
    curdice[int(dstr[num])-1] = random.randrange(1,7)

#display the dice list
for num in range(5):
    print(curdice[num],' ', end='')