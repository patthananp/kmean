# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 15:23:07 2019

@author: RSU8
"""


import numpy as np

D = np.array([[ 1, 6],[ 7, 2],[ 4, 0],[ 3, 9],[ 8, 2]])
#find min of Row for D
minRow = np.argmin(D,axis=1)
minRowVal = np.amin(D, axis=1)
Data = np.array([[1, 3, 3], [0, 2, 5], [7, 9, 10],
                 [2, 3, 4]])
minCol = np.argmin(Data,axis=0)
minColVal = np.amin(Data,axis=0)       
