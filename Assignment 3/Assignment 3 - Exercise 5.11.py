# -*- coding: utf-8 -*-
"""
Created on Fri May 29 08:23:46 2020

@author: alexa
"""

def summarize_letters(instr):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    alphaC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    list = []

    for num in range(len(alpha)):
        letcount = instr.count(alpha[num])+instr.count(alphaC[num])
    
        if letcount != 0:
            tu = (alpha[num] , letcount)
            list.append(tu)
    return list


f = summarize_letters('abcdefghijklmnopqrstuvwxyz')

    
if len(f) == 26:
    print('This string had all the letters of the alphabet')
