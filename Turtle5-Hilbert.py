# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 15:46:48 2023

@author: HiteVision
"""

# -*- coding: utf-8 -*-

import turtle as t
import random
length = 10
angle  = 90
t.setup(1280,720)
t.up()

t.goto(-640,-360)
t.down()
def draw_path(path):
    for symbol in path:
        if symbol == 'f':
            t.colormode(255)
            t.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
            t.fd(length)
        elif symbol == '+':
            t.lt(angle)
        elif symbol == '-':
            t.rt(angle)

def apply_path(rules,path):
    lit = [x for x in path]
    for i in range(len(lit)):
        symbol = lit[i]
        if symbol == 'x':
            lit[i] = rules[symbol]
        elif symbol == 'y':
            lit[i] = rules[symbol]
    path = ''.join(lit)
    return path

rules = {
    'x':'+yf-xfx-fy+',
    'y':'-xf+yfy+fx-'
}
path = 'x'
t.speed(0)
for i in range(7):
    path = apply_path(rules,path)
draw_path(path)
t.done()
