# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
#from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
def KmeansRun(pattern,k):

    [maxRow, maxCol] = np.shape(pattern)
    # Find 2 Centroids by random
        
    IdxCentroid = np.random.permutation(???)
    centroid_init= pattern[IdxCentroid[0:k], ???]

    centroid = centroid_init
    centroid_new = np.zeros([???, maxCol])
    iteration = 0
    cont = True
    d = np.zeros((maxRow, k))
    while cont == True:
        iteration = iteration + 1 
        #find distance between centroids j and pattern data) i
        for i in range(0,maxRow):
            for j in range(0, ???): 
                d[???, ???] = np.sum(np.absolute(centroid[???,:]-pattern[i,:]))
        # find the cluster (group) of each pattern (sample)
        group=np.argmin(d,axis=1)
        group = np.array(group)
        g = []
        #calculate centroid of each group
        for i in range(0, k):
            #In each group, find the patterns belong to it
            f= np.where(group==???)
            if len( f ) > 0:
               centroid_new[???,:]= np.mean(pattern[f,:], axis=1)
            g.append(np.array(f))
      
        fitness = FitnessCalc(k, centroid_new, pattern, g);
        if np.all(np.absolute(centroid_new - centroid)<0.001):
           print ('BREAK\n')
           cont = False
        else: 
           centroid=centroid_new
        
   
    return centroid,centroid_init, g, fitness 
def Plot3D(pattern, centroid, g):
    fig = plt.figure(figsize=(12,12))
    ax = fig.add_subplot(111, projection='3d')
    centroidT = np.transpose(centroid)
    ax.scatter(centroidT[???,0], centroidT[???,0], centroidT[???,0], c='r', marker='o')
#    hold on 
#    #plot 3D: patterns in group -1
    
    patternT0 = np.transpose(Data[group[???]][:])
    ax.scatter(patternT0[???,:], patternT0[???, :],patternT0[???, :],c='g' , marker='o')
#    hold on
#    plot 3D: centroid -2
    ax.scatter(centroidT[???,1], centroidT[???,1], centroidT[???,1],c='b', marker='^');
#    hold on
#    #plot 3D: patterns in group -2
    patternT1 = np.transpose(Data[group[???]][:])
    ax.scatter(patternT1[???,:], patternT1[???, :],patternT1[???, :],c='k', marker='x')
#    hold on
#    display(centroid )
#    display(centroid_new)
#    sprintf('fitness = %f', fitness)
    plt.show()
    

#%     
def FitnessCalc(k, centroid, pattern, g): 
    fitness = 0
    for j in range(0, ??? ):
        #sizeG = len(g[j][0])
        sizeG = len(g[???])
        for i in range(0, ???):
            fitness = fitness + np.sum(np.absolute(centroid[???,:]-pattern[g[???][???],:])) 
    return ???

Data = np.array([[1,       3,       3],
        [1,       4,       2],
        [7,       9,       10],
        [8,       9,       7],
        [2,       3,       4]])

[centroid,centroid_init,group, fitness] = KmeansRun(???,2)
Plot3D(Data, centroid, ???)
     
    
