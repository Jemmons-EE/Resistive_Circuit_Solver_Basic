#RCSB Stamper

#Author: J Emmons
#VERS: 1.8
#DTD: 11 FEB 2026

from sys import exit
import numpy as np                      # needed for arrays
# from numpy.linalg import solve          # needed for matrices
# from numpy.linalg import inv            # import matrix solver
# from read_netlist import read_netlist   # supplied function to read the netlist
import comp_constants_rcsb as COMP           # needed for the common constants


def stamper(y_add,netlist,currents,node_cnt):
    # return the total number of rows in the matrix for
    # error checking purposes
    # add 1 for each voltage source...
    last_row = node_cnt
    for comp in netlist:                  # for each component...

        # extract the i,j and fill in the matrix...
        # subtract 1 since node 0 is GND and it isn't included in the matrix
        i = comp[COMP.I] - 1
        j = comp[COMP.J] - 1

        if ( comp[COMP.TYPE] == COMP.R ):           # a resistor
            if (i >= 0):                            # add on the diagonal its 1st connection
                y_add[i,i] += 1.0/comp[COMP.VAL]        
            if (j >= 0):                            # add on the diagonal it second connection
                y_add[j,j] += 1.0/comp[COMP.VAL]
            if (i >= 0 and j >= 0):                 # if conn to 2 nodes
                y_add[i,j] -= 1.0/comp[COMP.VAL]    # put neg conductance in row location
                y_add[j,i] -= 1.0/comp[COMP.VAL]    # put neg conductance in col location
       
        if ( comp[COMP.TYPE] == COMP.VS):
                                        #volt source added to last row                                                     
            if(i<0 and j>=0):           #check voltage source conn to gnd w neg side voltage only circ
                y_add[last_row,j]=1     #add 1 to matrix location in row at node cnt
                y_add[j,last_row]=1     #add 1 to matrix location at col node cnt
            elif(i>=0 and j<0):         #check voltage source conn w pos side to gnd voltage only circ
                y_add[last_row,i]=1     #add 1 from matrix location in row at node cnt
                y_add[i,last_row]=1     #add 1 from matrix location at col node cnt
            else:                       # voltage source conn to 2 nodes
                y_add[last_row,i]=1     #add 1 to matrix location in row at node cnt
                y_add[i,last_row]=1     #add 1 to matrix location at col node cnt
                y_add[j,last_row]=-1    #add neg 1 to row at node cnt
                y_add[last_row,j]=-1    # add neg 1 to col at node cnt
                                    #
            currents[last_row,0]=comp[COMP.VAL]     # update currents matrix
            last_row += 1           #  move cnt up 1 row incase another volt source

        if ( comp[COMP.TYPE] == COMP.IS):
            if( i >= 0):
                currents[i,0] -= comp[COMP.VAL]     #if curr source connected from i node subtract from row i
            if (j >= 0):
                currents[j,0] += comp[COMP.VAL]     #if curr source conn into node j add val to row j

        if(comp[COMP.I] == comp[COMP.J]):                                         # component connects to itself
            print("component connects to itself\n",comp[0:])    #BAD DATA
            exit()                                              #REPORT AND EXIT
    return node_cnt  # should be same as number of rows!