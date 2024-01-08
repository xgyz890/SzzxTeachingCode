#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 20:47:39 2021

@author: Yang
"""
from turtle import *
colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
for x in range(240):
    speed(500)
    pencolor(colors[x % 6])
    width(x / 50 + 1)
    forward(x)
    left(59)
forward(20)
hideturtle()
mainloop()

