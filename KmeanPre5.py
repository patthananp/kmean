# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 13:15:06 2019

@author: RSU8
"""



import numpy as np
Data = np.array([[1, 3, 3, 1], [1, 4, 2, 1], [7, 9, 10, 2],
           [8, 9, 7, 2], [2, 3, 4, 1]])
k = 2 # k refers to number of clusters
group=Data[:,-1]
     
g = []
#calculate centroid of each group
for i in range(1,k+1):
    #In each group, find the patterns belong to it
    f= np.where(group==i)
    g.append(np.array(f))

gElement0 = g[0] 
gElement1 = g[1]    

#sizeG0 = len(g[0][0])  
#sizeG1 = len(g[1][0])    
#
#g00 = g[0][0]
#g000 = g[0][0][0]
#g001 = g[0][0][1]
#g002 = g[0][0][2]
#gE00 = gElement0[0][0]
#
#DataG000 = Data[g[0][0][0], 0:-1]
#DataGE00 = Data[gElement0[0][0], 0:-1]


# Get [7, 9, 10]   ???