# -*- coding: utf-8 -*-
"""
Created on Tue May 26 18:21:33 2020

Homework Problem 3.6
Alex Adams
Summer BIS497

"""

problem = input("What is your problem? ")

before = 'badanswer'
while before != 'N' and before != 'Y' and before != 'n' and before != 'y':
    before = input("Have you had this problem before(Y/N) ")

if before == 'Y' or before == 'y':
    print('Well, you have it again.')
    
if before == 'N' or before == 'n':
    print('Well, you have it now.')

# this exchange would not convince the operator because it is an obvious logical response to the question.