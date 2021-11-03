# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 12:39:49 2019

@author: RSU8
"""



import numpy as np
pattern = np.array([[1,       3,       3],
        [1,       4,       2],
        [7,       9,       10],
        [8,       9,       7],
        [2,       3,       4]])
[maxRow, maxCol] = np.shape(pattern)
    # Find 2 Centroids by random
k = 2  # k refers to number of clusters      
IdxCentroid = np.random.permutation(maxRow)
centroid_init= pattern[IdxCentroid[0:k], :]
centroid = centroid_init
    
d = np.zeros((maxRow, k))
for i in range(0,maxRow):
    for j in range(0, k):
        temp = np.absolute(centroid[j,:]-pattern[i,:])
        d[i,j] = np.sum(temp)