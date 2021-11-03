# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 12:22:50 2019

@author: RSU8
"""


import numpy as np

D = np.array([[ 1, 6],[ 7, 2],[ 4, 0],[ 3, 9],[ 8, 2]])
#find min of Row for D
meanRow = np.mean(D,axis=1)

Data = np.array([[1, 3, 3], [0, 2, 5], [7, 9, 10],
                 [2, 3, 4]])
meanCol1 = np.mean(Data,axis=0)
meanCol2 = np.mean(Data[1:2, :],axis=0)
meanCol3 = np.mean(Data[0:2, :],axis=0)

