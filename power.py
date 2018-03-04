#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 10:11:27 2018

@author: joyce
"""
def calculate_power(num_bus,theta_bus,v_bus,Y,List_Adj):
    import numpy as np
    from math import cos, sin
    P = np.zeros(num_bus)
    Q = np.zeros(num_bus)
    
    k = 0 
 
    while k < num_bus:
        sum_P = 0
        sum_Q = 0
        for m in List_Adj[k]:
            g_km = Y[k,m].real   
            b_km = Y[k,m].imag
            
            cos_km = cos(theta_bus[k]-theta_bus[m])            
            sin_km = sin(theta_bus[k]-theta_bus[m])
            
            sum_P =  sum_P + (v_bus[m]*(g_km *cos_km+b_km*sin_km))
            sum_Q =  sum_Q + ((v_bus[m])*(g_km *sin_km-b_km*cos_km))
            
       
        P[k] = v_bus[k] * sum_P 
        Q[k] = v_bus[k] * sum_Q 
        k=k+1
    return P, Q
        
        
    
    