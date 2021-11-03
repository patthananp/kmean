# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 12:52:58 2019

@author: RSU8
"""

import numpy as np
old = np.array([1, 2, 3])
new = np.array([5, 6, 7])
cont = True  #cont = continue
iteration = 0
while cont == True:
    if (old == new).all():
        cont = False
    else:
        old = old + 1
        iteration = iteration + 1
    