# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 16:57:01 2019

@author: RSU8
"""
#conda install matplotlib
#or
#conda install -c conda-forge matplotlib
#and
#conda install -c conda-forge mpld3

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
Data = np.array([[1,       3,       3],
        [1,       4,       2],
        [7,       9,       10],
        [8,       9,       7],
        [2,       3,       4]])
centroid = np.array([[7.5, 9, 8.5], [1.33, 3.33, 3]])
group1 = np.array([0,1,4])
group2 = np.array([2,3])
g = [group1, group2]
centroidT = np.transpose(centroid)
fig = plt.figure(figsize=(12,12))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(centroidT[0,0], centroidT[1,0], centroidT[2,0], c='r', marker='o')
#    hold on 
#    #plot 3D: patterns in group -1
    
patternT0 = np.transpose(Data[g[0]][:])
ax.scatter(patternT0[0,:], patternT0[1, :],patternT0[2, :],c='g' , marker='o')
#    hold on
#    plot 3D: centroid -2
ax.scatter(centroidT[0,1], centroidT[1,1], centroidT[2,1],c='b', marker='^');
#    hold on
#    #plot 3D: patterns in group -2
patternT1 = np.transpose(Data[g[1]][:])
ax.scatter(patternT1[0,:], patternT1[1, :],patternT1[2, :],c='k', marker='x')
#    hold on
#    display(centroid )
#    display(centroid_new)
#    sprintf('fitness = %f', fitness)
plt.show()
    