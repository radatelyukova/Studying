#! /usr/bin/env python3
################################################################################
#   epic.py
#
#   Epic multiplication table
#
#   06.12.2016  Created by: Rada Telyukova
################################################################################

print('Таблица умножения:')
for j in range(1,11):
    for i in range(1,6,):
        print(str(i).rjust(2) + ' x ' + str(j).rjust(2) + ' = ' + str(i*j).rjust(3) + "\t", end='')
    print("\n", end='')
print("\n")
for j in range(1,11):
    for i in range(6,11):
        print(str(i).rjust(2) + ' x ' + str(j).rjust(2) + ' = ' + str(i*j).rjust(3) + "\t", end='')
    print("\n", end='')