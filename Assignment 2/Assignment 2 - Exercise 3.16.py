# -*- coding: utf-8 -*-
"""
Created on Tue May 26 21:00:59 2020

@author: alexa
"""
count = 1
high = 0
shigh = 0

while count <= 10:
    number = float(input('Enter a Number: '))
    if number > high:
        shigh = high
        high = number
    elif number > shigh:
        shigh = number
    count = count+1

# TAA: please have your program print the result at the end of processing