#! /usr/bin/env python3
################################################################################
#   legendary.py
#
#   Legendary multiplication table
#
#   06.12.2016  Created by: Rada Telyukova
################################################################################

print("Таблица умножения:")
for k in range(0,6,5):
    for j in range(1,11):
        for i in range(1,6):
            print(str(i+k).rjust(2) + ' x ' + str(j).rjust(2) + ' = ' + str((i+k)*j).rjust(3) + "\t", end='')
        print("\n", end='')
    print("\n")