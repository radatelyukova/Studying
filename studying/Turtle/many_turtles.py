#!/usr/bin/env python3
################################################################################
#   many_turtles.py
#
#   <Executable Module Purpose>
#
#   20.07.2017  Created by:  rada
################################################################################

import turtle as t

lisa = t.Pen()
rob = t.Pen()

lisa.shape('turtle')
rob.shape('turtle')

lisa.color('purple')
rob.color('orange')

lisa.fd(100)
rob.lt(90)
rob.fd(120)

t.mainloop()
