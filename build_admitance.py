#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 11:32:47 2018

@author: joyce
"""

def admitance_matrix(bi_bran,bf_bran,r_bran, x_bran, shunt_bran,num_bus,num_bran,shunt_bus):
    import numpy as np
    index=0
   
    Y = np.zeros((num_bus,num_bus),dtype=complex)

    for r in r_bran:
       
        k = int(bi_bran[index])-1
        m = int(bf_bran[index])-1

        x= x_bran[index]
        brsh = shunt_bran[index]/2 #the division by 2 depends of the way the datas were set out

        g = r / (r**2 + x**2)
        b = -x / (r**2 + x**2)
        
        ykm=complex(g,b)
      
        Y[k,m] = -ykm
        Y[m,k] = -ykm
        Y[k,k] = Y[k,k] + complex(0,brsh) + ykm
        Y[m,m] = Y[m,m] + complex(0,brsh) + ykm
        
        index = index +1 
        
    index=0
    for bush in shunt_bus:
        
        Y[index,index] = Y[index,index] + complex(0,bush) 
        index = index +1
        
    return Y    
        
        
        
        
      
   
    
    