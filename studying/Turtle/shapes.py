#! /usr/bin/env python3
################################################################################
#   shapes.py
#
#   <Executable Module Purpose>
#
#   28.01.2017  Created by: Rada Telyukova
################################################################################

import turtle
import time 

t=turtle.Turtle()
screen = turtle.Screen()

#screen.setup(1200,900)
screen.bgcolor('black')

t.pensize(5)
t.speed(2)
t.shape('turtle')

shapes=['Точка', 'Линия',      'Треугольник', 'Квадрат', 'Пятиугольник', 'Шестиугольник', 'Семиугольник', 'Восьмиугольник', 'Девятиугольник', 'Деситиугольник']
colors=['white', 'lightgreen',  'red',        'yellow',  'lightblue',    'green',         'purple',         'cyan',         'maroon',          'pink']

# Loop: shapes
for i in range(10):
    time.sleep(1)
    t.clear()
    t.pencolor(colors[i])
    angle = 360. / (i+1)
    side  = 100
    
    t.penup()
    t.setpos(-10,20)
    t.pendown()
    t.showturtle()

    # Loop: sides of shape
    for j in range(i+1):
        if (i == 0):
            t.stamp()
        else:
            t.fd(side)
            t.rt(angle)
 
    # Title
    t.hideturtle()
    t.penup()
    t.setpos(-100,200)
    t.pendown()
    t.write(shapes[i], font = ('Arial', 20, 'bold'))
    
turtle.done()