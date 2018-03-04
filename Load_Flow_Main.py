#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 09:37:27 2018
@author: joyce
"""
import numpy as np
import build_admitance as build_admit
import build_adjacency as build_adj
import power 
import equations
from scipy.optimize import *
import build_jacobian as build_jac
import newthon_method 


from math import cos, sin
#from scipy.optimize import *

#==================================================================================================#
# Data read from the files that contains the information about the bus and the branchs of the system
# Data bus are set out as shown below: 
# for a bus "i"
   # number(ID) -- id_bus
   # Type of bus: slack(0), PV(1) ou PQ(2) -- type_bus
   # Angle -- theta_bus
   # Voltage -- v_bus
   # Active Power injected at bus i -- p_inj 
   # Reactive Power injected at bus i  -- q_inj
   # Active Load Power at bus i -- p_load 
   # Reactive Load Power at bus i -- q_load
   # Bus Shunt -- shunt_bus
     
file_bus = "proudBUS.txt" 
#file_bus = "barras.txt"  
#file_bus = "sistema2barras_PQ.txt"    
id_bus,type_bus,theta_bus,v_bus,p_inj,q_inj,p_load,q_load,shunt_bus = np.loadtxt(file_bus, unpack=True )
num_bus = id_bus.size
# Data branch are set out as shown below: 
# A branch can be a transmission line or a transformer that connects two buses. 
# Data branch are set out as shown below: 
   # initial bus          -- bi_bran
   # final bus           -- bf_bran 
   # resistance of branch -- r_bran
   # reactance of branch -- x_bran
   # shunt of branch     -- shunt_bran
   
file_bran = "proudBRAN.txt"  
#file_bran = "linha.txt"  
bi_bran, bf_bran,r_bran, x_bran, shunt_bran =   np.loadtxt(file_bran, unpack=True,ndmin=2 ) 

# If there's only one bus, Python interpret it as a scalar and not as an array, so in order to
# make the conversion possible, it's necessary this instruction , ndmin=2, the other, unpack = True 
#it's responsable to read the data in column
num_bran = bi_bran.size  
#==================================================================================================#  
# Admitance matrix assembly process 

Y=build_admit.admitance_matrix(bi_bran,bf_bran,r_bran, x_bran,shunt_bran,num_bus,num_bran,shunt_bus)
#==================================================================================================#  
# Adjacency matrix assembly process 
List_Adj = build_adj.adjacency_matrix(Y,num_bran,num_bus)

#==================================================================================================#  

#P, Q = power.calculate_power(num_bus,theta_bus,v_bus,Y,List_Adj) function created to use later!

bus_PV = np.flatnonzero(type_bus==1)

bus_PQ = np.flatnonzero(type_bus==2)

bus_slack = np.flatnonzero(type_bus==0)


# Net Power _----- (Pg_inj - Pload)

p_net = p_inj - p_load
q_net = q_inj - q_load

x_initial =  np.zeros((2*num_bus)) 
x_initial[0:num_bus] = theta_bus
x_initial[num_bus:2*num_bus] = v_bus 


vet_sol_fsolve = fsolve(equations.system_equations,x_initial) 

vet_sol_newton= newthon_method.fnewton(x_initial)

