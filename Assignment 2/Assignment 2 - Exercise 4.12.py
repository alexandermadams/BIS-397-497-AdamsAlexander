# -*- coding: utf-8 -*-
"""
Homework Problem 4.12
Alex Adams
Summer BIS497
"""

import random
import time


#Turtle Movement Function
def tortmove():
    rnum = random.randint(1,10)
    if rnum <= 5:
        movepos = 3
    elif rnum <= 7:
        movepos = -6
    else:
        movepos = 1
    return movepos

#Hare Movement Function
def haremove():
    rnum = random.randint(1,10)
    if rnum <= 2:
        movepos = 0
    elif rnum <= 4:
        movepos = 9
    elif rnum <= 5:
        movepos = -12
    elif rnum <= 8:
        movepos = 1
    else:
        movepos = -2
    return movepos



print('BANG !!!!!')
print('AND THEY\'RE OFF !!!!!')

tortpos = 1
harepos = 1
while tortpos < 70 and harepos < 70:
    time.sleep(.5)
    tortpos = tortpos + tortmove()
    harepos = harepos + haremove()
    if tortpos < 1:
        tortpos = 1
    if harepos < 1:
        harepos = 1
    line = ''
    for num in range(1,70,1):
        if num == tortpos and num == harepos:
            line = line + 'OUCH!!!'
        elif num == tortpos:
            line = line + 'T'
        elif num == harepos:
            line = line + 'H'
        else:
            line = line + '-'  
    print(line)
    
if tortpos >= 70 and harepos >= 70:
    print('It\'s a tie')
elif tortpos >=70:
    print('TORTOISE WINS!!! YAY!!!')
else:
    print('Hare wins')
        
    

