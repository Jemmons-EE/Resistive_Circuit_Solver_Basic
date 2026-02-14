#RCSB_main

#Resistive Circuit Solver Basic Main 

#Author: J Emmons
#VERS: 2.0
#DTD: 11 FEB 2026

from sys import exit
import numpy as np                      # needed for arrays
from numpy.linalg import solve          # needed for matrices
# from numpy.linalg import inv            # import matrix solver
from read_netlist import read_netlist   # supplied function to read the netlist
import comp_constants_rcsb as COMP           # needed for the common constants
from rcsb_stamper import stamper            # builds matrices for solver math
from read_netlist import read_netlist          #reads netlist, gets sizes

#READ THE NETLIST, CONVEERT TO NUMERICAL AND GET SIZE COUNTS
# print("Called netlist")
netlist, node_cnt, volt_cnt = read_netlist()

#CREATE MATRICES OF SIZE NEEDED 
print("Building Matrices")
matrix_size = node_cnt + volt_cnt
y_add = np.zeros((matrix_size, matrix_size))
currents = np.zeros((matrix_size, 1))
print("Matrices Complete")

#CALL STAMPER TO BUILD MATRICES FOR SOLVE
print("Calling Stamper")
node_counter=stamper(y_add,netlist,currents,node_cnt)

#SOLVE FOR VOLTAGES AND RETURN MATRICES
print("Admittance Matrix=\n", y_add)
print("Current Matrix =\n", currents)
voltages_1 = solve(y_add,currents)

print("Voltages are: ", voltages_1.T)

exit()

