#! /usr/bin/env python3
################################################################################
#   my_test.py
#
#   Test of Dictionary
#
#   08.12.2016  Created by: Rada Telyukova
################################################################################

me = {'name': 'Rada', 'age': 9, 'class': '3B'}
print(me)
print(me.keys())
print(me.values())
print(me.items())
print(len(me))

for key in me:
    print(key, ':', me[key])

for key, value in me.items():
    print(key,': ', value)