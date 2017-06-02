#! /usr/bin/env python3
################################################################################
#   my_write.py
#
#   Write to file
#
#   04.03.2017  rada
################################################################################

#import time

fout = open('my_file.txt', 'w')

fout.write("Hello\n")
fout.write("\n")
fout.write('Меня зовут Рада\n')

#time.sleep(20)
fout.close()
