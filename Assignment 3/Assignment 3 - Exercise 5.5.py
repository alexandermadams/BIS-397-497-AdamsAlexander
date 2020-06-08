# -*- coding: utf-8 -*-
"""
Created on Fri May 29 08:23:46 2020

@author: alexa
"""

alphabet = 'abcdefghijklmnopqrstuvwxyz'

#a
alphabet[0:int(len(alphabet)/2)]

#b
alphabet[:-int(len(alphabet)/2)]

#c
alphabet[-int(len(alphabet)/2):len(alphabet)]

#d
alphabet[-int(len(alphabet)/2):]

#e
alphabet[::2]

#f
alphabet[::-1]

#g
alphabet[::-3]
