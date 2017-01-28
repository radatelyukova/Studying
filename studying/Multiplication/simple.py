#! /usr/bin/env python3
################################################################################
#   simple.py
#
#   Simple multiplication table
#
#   05.12.2016  Created by: Rada Telyukova
################################################################################

for i in range(1,11):
    for j in range(1,11):
        print(str(i).rjust(2) + ' x ' + str(j).rjust(2) + ' = ' + str(i*j).rjust(3))
