# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 13:53:08 2020

HW Exercise 7.9
Alex Adams

"""

import numpy as np

a1 = np.arange(1,16,1).reshape(3,5)

#a
a1[2]

#b
a1[:,4]
#is this a trick question? There is no column 5???

#c
a1[0:2]

#d
a1[:,2:5]

#e
a1[1,4]

#f
a1[1:3,[0,2,4]]

