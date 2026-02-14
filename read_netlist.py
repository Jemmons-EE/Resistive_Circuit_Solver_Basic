#read_netlist_updated

#initialAuthor: J Emmons
#VERS: 2.2
#Created: 01 Feb 2026

import comp_constants_rcsb as COMP  # get the constants needed for lists
from sys import exit                # needed to exit on error

################################################################################
# Read NETLIST from Spice File                                                 #
# Input:  NONE                                                                 #
# Outputs:                                                                     #
#   netlist: List of Components; Each Component is List Prperties              #
#   node_cnt: number of nodes in the netlist                                   #
#   volt_cnt: number of voltage sources in the netlist                         #
#   Structure                                                                  #
# --TYPE NAME, I, J, Magnitude --                                              #
#   Func: convert_values: convert strings in netlist to int and float          #
################################################################################

def convert_values(props,netlist):
    props[COMP.I]   = int(props[COMP.I])        # CONVERT STR TO INT
    props[COMP.J]   = int(props[COMP.J])        # CONVERT STR TO INT
    props[COMP.VAL] = float(props[COMP.VAL])    # CONVERT STR TO FLOAT
    netlist.append(props)     
    return

def read_netlist():                                         # Read Netlist, Count Netlist No Argument
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
    print("Converted netlist to Numerical")
    node_cnt = 0
    res_cnt = 0
    volt_cnt = 0
    curr_cnt = 0
    print("Getting Dimensions"  )
    for index, items in enumerate(netlist):
        typpy = netlist[index]
      #  for index[0] in typpy:
        if(typpy[2]>node_cnt):          #CHECK HIGHEST NODE I
            node_cnt = typpy[2]
        if(typpy[3]>node_cnt):          #CHECK HIGHEST NODE J
            node_cnt = typpy[3]
        if(typpy[0] == 0):              #UPDATE RESISTOR COUNT
            res_cnt +=1
        elif(typpy[0] == 1):            #UPDATE VOLT SRC COUNT
            volt_cnt += 1
        elif(typpy[0] == 2):            #UPDATE CURR SRC COUNT
            curr_cnt += 1
        else:                           #UNKNOWN COMP
            print("Unknown component type:\n",typpy[0], 'check components list')   # bad data!
            exit()                      #REPORT AND EXIT 

    # testnetlist, node_cnt, volt_cnt = read_netlist()      # Debug Statement
    # print("Netlist is ", testnetlist)                     # Debug Statement
    # print("Node Count is ",node_cnt)                      # Debug Statement
    # print("Volt Count is ", volt_cnt)                     # Debug Statement
    return netlist, node_cnt, volt_cnt


