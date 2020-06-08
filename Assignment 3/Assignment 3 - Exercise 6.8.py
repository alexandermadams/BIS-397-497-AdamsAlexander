# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 13:53:08 2020

HW Exercise 6.8
Alex Adams

"""
HD = {'One':'1','Two':'2','Three':'3','Four':'4','Five':'5','Six':'6','Seven':'7','Eight':'8','Nine':'9'}

TEEND = {'Eleven':'1','Twelve':'2','Thirteen':'3','Fourteen':'4','Fifteen':'5','Sixteen':'6','Seventeen':'7','Eighteen':'8','Nineteen':'9'}

TD  = {'One':'1','Twenty':'2','Thirty':'3','Forty':'4','Fifty':'5','Sixty':'6','Seventy':'7','Eighty':'8','Ninety':'9'}

amt = '679.94'

amt[0]

for word, number in HD.items():
    if amt[0] == number:
        print(word,'HUNDRED ',end='')

if amt[1] == '1':
   for word, number in TEEND.items():
       if amt[2] == number:
           print(word, end='')
else:
    for word, number in TD.items():
        if amt[1] == number:
            print(word, end=' ')
    for word, number in HD.items():
        if amt[2] == number:
            print(word,'AND ', end='')

print(amt[-2:len(amt)],'/','100')
