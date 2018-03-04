#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 17:34:40 2018

@author: joyce
"""

def adjacency_matrix(Y,num_bran,num_bus):
    import numpy as np
    List_adj = []
    index_bus=0
    while index_bus < num_bus:       
       
        adj_bus = np.flatnonzero((Y[index_bus,:]))
        List_adj.append((adj_bus))  
        
        index_bus = index_bus + 1   

    return List_adj
    
