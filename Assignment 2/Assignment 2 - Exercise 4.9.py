# -*- coding: utf-8 -*-
"""
Homework Problem 4.9
Alex Adams
Summer BIS497
"""
def farenheit(celcius):
    return (9/5)*celcius+32

print('Celcius\tFarenheit')

for number in range(0,101,1):
    far = farenheit(number)
    print(f'{number:>6.1f}\t{far:>9.1f}')
    

