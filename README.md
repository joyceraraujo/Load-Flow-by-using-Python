# Load-Flow-by-using-Python

This project aims to solve the problem of load flow by using Python and its package for scientific computing, Numpy. 
Firstly,  the native fonction fsolve has been used to solve the system of nonlinear equations that represents
the load flow equations.
After checking the results obtained by fsolve,Newton's Method has been implemented to solve the system of 
nonlinear equations.
Both methods presents the same results. 


How to use this program ? 

In order to make the load flow study for a given system , it's necessary to fill out two files that contains the bus and branch informations. 
The data has to be informade in p.u. 
The informations required for both files can be view in the file Load_Flow_Main.py 


 
