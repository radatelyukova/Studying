#! /usr/bin/env python3
################################################################################
#   test_shapes.py
#
#   Tests my Shapes Lib with prefix
#
#   02.02.2017  Created by: Rada Telyukova
#   02.06.2017  Last update
###############################################################################

import shapes

#shapes.draw_line(-20, 50, 100, 100, 'green', 10)
#shapes.draw_line(100, 30, 100, 100, 'purple', 20)
#
#shapes.draw_rectangle(200, 300, -100, 80, 'red', 5)

x1 = -60
y1 = -30
x0 = -120
x2 = 0
y2 = 60
y3 = 120
shapes.draw_rhomb(x1, y1, x0, x2, y2, y3, 'yellow', 15)

shapes.keep_picture()