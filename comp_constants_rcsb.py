################################################################################
#Author: J Emmons
#VERS1.2
#08 FEB 2026

#Components Identifiers
RESIS = 'R'      # a resistor
V_SRC = 'VS'     # a voltage source
I_SRC = 'IS'     # a current source

#Component Structure Table
# 
# -- TYPE NAME, I, J, Magnitude -- 
TYPE = 0         # Resistor / Voltage Source
NAME = 1         # Component Name
I    = 2         # Out Node 
J    = 3         # In Node
VAL  = 4         # Magnitude

# Component Identifier Numerical
R    = 0         # Resistor
VS   = 1         # Voltage Source
IS   = 2         # Current Source
