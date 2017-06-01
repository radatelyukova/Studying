#!/usr/bin/env python3
################################################################################
#   roll_dices.py
#
#   <Executable Module Purpose>
#
#   31.05.2017  Created by:  rada
################################################################################

import random, sys

while(True):
    print(random.randint(1,6), random.randint(1,6))
    answer = input('продолжить(y/n)? ')
    if (answer == 'n'): sys.exit("stop")
    
    
