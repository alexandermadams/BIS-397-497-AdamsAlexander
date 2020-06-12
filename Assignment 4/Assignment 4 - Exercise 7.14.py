# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 13:53:08 2020

HW Exercise 7.14
Alex Adams

"""

import numpy as np

a1 = np.array([[0,1],[2,3]])
a2 = np.array([[4,5],[6,7]])

#a
a3 = np.vstack((a1,a2))

#b
a4 = np.hstack((a1,a2))

#c
a5 = np.vstack((a4,a4))

#d
a6 = np.hstack((a3,a3))
