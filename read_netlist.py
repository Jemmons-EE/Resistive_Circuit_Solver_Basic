#read_netlist_updated

#initialAuthor: J Emmons
#Created: 01 Feb 2026

import comp_constants_rcsb as COMP      # FETCH CONSTANTS
from sys import exit                    # ERROR EXIT

################################################################################
# Read NETLIST from Spice File                                                 #
# Input:  NONE                                                                 #
# Outputs:                                                                     #
#   netlist: List of Components; Each Component is List Prperties              #
#                                                                              #
# List Structure                                                               #
# --TYPE NAME, I, J, Magnitude --                                              #
################################################################################

def convert_values(props,netlist):              # CONVERTS STR TO NUMERICAL
    props[COMP.I]   = int(props[COMP.I])        # CONVERT STR TO INT
    props[COMP.J]   = int(props[COMP.J])        # CONVERT STR TO INT
    props[COMP.VAL] = float(props[COMP.VAL])    # CONVERT STR TO FLOAT
    netlist.append(props)     
    return

def read_netlist():                                         # Read Netlist No Argument
    filename = input("Enter Netlist File Name: ")           # Query Netlist File Name Include .txt or
    #print(filename)                                        # Debug Statement
    flop = open(filename,"r")                               # Open File
    lines = flop.readlines()                                # Read File
    flop.close()                                            # Close File

    netlist = []                                            # Initialize List
    for line in lines:                                      # Each Line is a Component
        line=line.strip()                                   # Strip Lead / Trail Whitespaces
        if line:                                            # Skip Empty Lines

            # READS: NAME, I, J, Magnitude -- NAME, FROM NODE, TO NODE, VALUE
            # INSERT NODE TYPE START OF LIST
            # PARSE PROPERTIES DELIMINATED BY SPACES

            props = line.split(" ")

            if ( props[COMP.TYPE][0] == COMP.RESIS ):       # RESISTOR CHECK
                props.insert(COMP.TYPE,COMP.R)              # INSERT TYPE

                convert_values(props,netlist)

            elif ( props[COMP.TYPE][0:2] == COMP.V_SRC ):   # VOLTAGE CHECK
                props.insert(COMP.TYPE,COMP.VS)             # INSERT TYPE

                convert_values(props,netlist)

            elif ( props[COMP.TYPE][0:2] == COMP.I_SRC ):   # CURRENT CHECK
                props.insert(COMP.TYPE,COMP.IS)             # INSERT TYPE

                convert_values(props,netlist)

            else:                                           # COMPONENT NOT RECOGNIZED
                print("Unknown component type:\n",line)     # REPORT FAIL
                exit()                                      # OUT

    return netlist

# testnetlist = read_netlist()        # Debug Statement
# print(testnetlist)                  # Debug Statement

