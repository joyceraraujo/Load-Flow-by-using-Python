#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 21:59:28 2018

@author: joyce
"""

def fnewton(x_initial):
    import equations
    import build_jacobian as build_jac
    import numpy as np
    from Load_Flow_Main import *
    
    toler = 0.03 
    iter_max = 20
    
    sol = x_initial #solution
    vector_eq = equations.system_equations(sol)
    
    
    
    vector_P = vector_eq[0:num_bus]
    vector_Q =  vector_eq[num_bus:2*num_bus]
  
    
    res_P = max(abs(vector_P))
    res_Q = max(abs(vector_Q))


    
    n_iter = 0 
    
    while (res_P > toler or res_Q > toler or n_iter <= iter_max):
        
        J = build_jac.jacobian_matrix(sol,Y)
      
        d_sol = np.linalg.solve(J, vector_eq)
       
        
        sol = sol + d_sol
       
        # Recalculating the errors
        vector_eq = equations.system_equations(sol)
        vector_P = vector_eq[0:num_bus]
        vector_Q =  vector_eq[num_bus:2*num_bus]
        res_P = max(abs(vector_P))
        res_Q = max(abs(vector_Q))
        
        n_iter =  n_iter + 1
        
        
    return sol
        
        
    
    
    
    