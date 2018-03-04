#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 22:55:20 2018

@author: joyce
"""


def system_equations(x):
    from Load_Flow_Main import *
    import numpy as np
    import power
       
    vector_eq = np.zeros((2*num_bus))

    
    theta=x[0:num_bus]
    v=x[num_bus:2*num_bus]
    
    p_bran, q_bran = power.calculate_power(num_bus,theta,v,Y,List_Adj)
    
    
    vector_eq[bus_PV] = p_net[bus_PV] -  p_bran[bus_PV]  
   
    vector_eq[bus_PV+num_bus] = v[bus_PV] - v_bus[bus_PV]
    
    vector_eq[bus_PQ] = p_net[bus_PQ] -  p_bran[bus_PQ]   
    vector_eq[bus_PQ+num_bus] =  q_net[bus_PQ]-q_bran[bus_PQ]  
    
    vector_eq[bus_slack] =   theta[bus_slack] - theta_bus[bus_slack]
    vector_eq[bus_slack+num_bus] = v[bus_slack] - v_bus[bus_slack]   
    
    
    
    
    return vector_eq
    