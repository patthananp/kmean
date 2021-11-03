# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 15:13:34 2019

@author: RSU8
"""


import numpy as np
Data = np.array([[1,       3,       3],
        [1,       4,       2],
        [7,       9,       10],
        [8,       9,       7],
        [2,       3,       4]])
Cent = Data[[2, 4],:]
group1 = np.array([0,1,4])
group2 = np.array([2,3])
g = [group1, group2]
fitness = 0
k = 2 #k refers to number of clusters
for j in range(0, k ):
   sizeG = len(g[j])
   for i in range(0, sizeG):
       gElement = g[j]
       fitness = fitness + np.sum(np.absolute(Cent[j,:]-Data[gElement[i],:])) 
    