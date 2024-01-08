# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 14:02:18 2023

@author: HiteVision
"""

import turtle as t
import random

def draw_path(path):
    t.colormode(255)
    t.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    for symbol in path:
        if symbol == 'F':
            t.forward(length)
        elif symbol == '-':
            t.right(angle)
        elif symbol == '+':
            t.left(angle)

def apply_rule(path):
    rule = 'F+F--F+F'
    return path.replace('F',rule)

length = .5
angle  = 60
t.setup(1280,720)
t.bgcolor('black')
t.up()
t.color("#0fe6ca")
t.goto(0,0)
t.down()
path = 'F--F--F'
t.speed(0)
t.up()
t.goto(-440,-250)
t.down()
for i in range(5):
    path = apply_rule(path)
draw_path(path)
draw_path(path)
draw_path(path)
a,b = t.pos()
for i in range(3):
    t.up()
    a += 250
    t.goto(a,b)
    t.down()
    draw_path(path)
    draw_path(path)
    draw_path(path)
b += 220
for i in range(2):
    t.up()
    a -= 250
    t.goto(a,b)
    t.down()
    draw_path(path)
    draw_path(path)
    draw_path(path)
b += 220
for i in range(2):

    draw_path(path)
    draw_path(path)
    draw_path(path)
    t.up()
    a += 130
    t.goto(a,b)
    t.down()

