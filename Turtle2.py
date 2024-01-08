# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 13:56:26 2023

@author: HiteVision
"""

import turtle as t
t.bgcolor("black")
sides=6
colors=["red","yellow","green","blue","orange","purple"]
for x in range(360):
    t.pencolor(colors[x%sides])
    t.forward(x*3/sides+x)
    t.left(360/sides+1)
    t.width(x*sides/200)
