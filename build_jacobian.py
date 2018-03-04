#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 18:35:15 2018

@author: joyce
"""

def jacobian_matrix(x,Y):
    from Load_Flow_Main import *
    import numpy as np

    J = np.zeros((2*num_bus,2*num_bus))
    
    theta=x_initial[0:num_bus]
    v=x_initial[num_bus:2*num_bus]
    
    p_bran, q_bran = power.calculate_power(num_bus,theta,v,Y,List_Adj)
    
    
    # -----> PQ-bus 
    
    for k in bus_PQ:
        
        for m in List_Adj[k]:
            
            # Diagonal elements:
            if k ==m:
                g_kk = Y[k,k].real
                b_kk = Y[k,k].imag
                vk = v[k]
                
                
                
                J[k,k] = -q_bran[k] - vk**2*b_kk # H_kk, partial derivative of Pk with respect to THETAk
               
                J[k,k+num_bus] = (p_bran[k] + vk**2*g_kk) / vk # N_kk, partial derivative of Pk with respect to Vk
                J[k+num_bus,k] = p_bran[k] -  vk**2*g_kk # M_kk, partial derivative of qk with respect to THETAk
                J[k+num_bus,k+num_bus] = (q_bran[k] - vk**2*b_kk) / vk # L_kk, partial derivative of Qk with respect to Vk
            else:
                g_km = Y[k,m].real
                b_km = Y[k,m].imag
                vk = v[k]
                vm = v[m]
                theta_k= theta[k]
                theta_m=theta[m]
                
                J[k,m] = vk*vm*(g_km*sin(theta_k-theta_m)-b_km*cos(theta_k-theta_m)) # H_km, partial derivative of Pk with respect to THETAm
                J[k,m+num_bus] = vk*(g_km*cos(theta_k-theta_m)+b_km*sin(theta_k-theta_m))# N_km, partial derivative of Pk with respect to Vm 
                J[k+num_bus,m] = -vk*vm*(g_km*cos(theta_k-theta_m)+ b_km* sin(theta_k-theta_m)) # M_km, partial derivative of qk with respect to THETHAm
                J[k+num_bus,m+num_bus] = vk*(g_km*sin(theta_k-theta_m)-b_km*cos(theta_k-theta_m))# L_km, partial derivative of Qk with respect to Vm
                
        
    # -----> PV-bus 
    
    for k in bus_PV:
        
        for m in List_Adj[k]:
            
            # Diagonal elements:
            if k ==m:
                g_kk = Y[k,k].real
                b_kk = Y[k,k].imag
                vk = v[k]
                
                
                
                J[k,k] = -q_bran[k] - vk**2*b_kk # H_kk, partial derivative of Pk with respect to THETAk
               
                J[k,k+num_bus] = (p_bran[k] + vk**2*g_kk) / vk # N_kk, partial derivative of Pk with respect to Vk
                
                J[k+num_bus,k+num_bus] = 1 # L_kk, partial derivative of Qk with respect to Vk
            else:
                g_km = Y[k,m].real
                b_km = Y[k,m].imag
                vk = v[k]
                vm = v[m]
                theta_k= theta[k]
                theta_m=theta[m]
                
                J[k,m] = vk*vm*(g_km*sin(theta_k-theta_m)-b_km*cos(theta_k-theta_m)) # H_km, partial derivative of Pk with respect to THETAm
                J[k,m+num_bus] = vk*(g_km*cos(theta_k-theta_m)+b_km*sin(theta_k-theta_m))# N_km, partial derivative of Pk with respect to Vm 
      
    
    # -----> Slack-bus 
    
    for k in bus_slack:
        
        for m in List_Adj[k]:
            
            # Diagonal elements:
            if k ==m:
    
                J[k,k] = 1 # H_kk, partial derivative of Pk with respect to THETAk
                J[k+num_bus,k+num_bus] = 1 # L_kk, partial derivative of Qk with respect to Vk
                
        return J
    
    