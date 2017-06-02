#! /usr/bin/env python3
################################################################################
#   my_read.py
#
#   File reading
#
#   04.03.2017  rada
################################################################################

fin = open('days.txt', 'r')

#print(fin.read())
#print(fin.read(12))

#print(fin.readline())
#print(fin.readline())
print(fin.readline())
print(fin.readline(6))

days = fin.readlines()
print(days)

fin.close()
