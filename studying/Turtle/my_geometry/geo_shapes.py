#! /usr/bin/env python3
################################################################################
#   shapes.py
#
#   <Executable Module Purpose>
#
#   02.02.2017  Created by: Rada Telyukova
###############################################################################

import turtle

t = turtle.Turtle()

def draw_line(x1, y1, x2, y2, color, size):
    t.pencolor(color)
    t.pensize(size)
    
    t.penup()
    t.setpos(x1, y1)
    t.pendown()
    t.goto(x2, y2)
    t.hideturtle()

draw_line(-20, 50, 100, 100, 'green', 10)
draw_line(100, 30, 100, 100, 'purple', 20)


turtle.done()