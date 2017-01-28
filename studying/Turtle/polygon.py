#! /usr/bin/env python3
################################################################################
#   polygon.py
#
#   <Executable Module Purpose>
#
#   26.01.2017  Created by: Rada Telyukova
################################################################################
import sys
import turtle

polygon = turtle.Turtle()
polygon.shape('turtle')
polygon.color('lightgreen')
polygon.speed(10)

try:
    sides_number = int(input('Enter number of sides: '))
except:
    print('Эй! число надо ввести!')
    sys.exit('Ошибка!')

angle        = 360.0 / sides_number
side_length  = 50

for i in range(sides_number):
    polygon.fd(side_length)
    polygon.rt(angle)

turtle.done()