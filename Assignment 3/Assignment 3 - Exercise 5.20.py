# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 12:23:43 2020
HW Question 5.20
@author: Alex Adams
"""
tdl = [[3,6,9],
       [4,6,788],
       [3,6,9]]

def display_table(tdl):
    print('    ', end = '')
    for item in range(len(tdl[0])):
        print(f'{item:4.0f}', end = '')
    
    print('')
    
    for row in range(len(tdl)):
        print(f'{row:4.0f}', end = '')
        for item in range(len(tdl[0])):
            print(f'{tdl[row][item]:4.0f}', end = '')
        print('')     
    
display_table(tdl)    
