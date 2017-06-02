#! /usr/bin/env python3
################################################################################
#   shapes.py
#
#   Shapes Library
#
#   02.06.2017  Created by: Rada Telyukova
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

def draw_rectangle(x1, y1, x2, y2, color, size):
    t.fillcolor(color)
    t.begin_fill()
    draw_line(x1, y1, x2, y1, color, size)
    draw_line(x2, y1, x2, y2, color, size)
    draw_line(x2, y2, x1, y2, color, size)
    draw_line(x1, y2, x1, y1, color, size)
    t.end_fill()
