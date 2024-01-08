# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 15:45:23 2023

@author: HiteVision
"""

import turtle as t

length = 5
angle = -60
t.setup(1280,720)
t.up()

t.goto(-640,-350)
t.down()
def draw_path(path):
    for symbol in path:
        if symbol == 'A' or symbol == 'B':
            import random
            t.colormode(255)
            t.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
            t.forward(length)
        elif symbol == '-':
            t.right(angle)
        elif symbol == '+':
            t.left(angle)
    t.ht()

def apply_rules(path,rules):
    lit = [_ for _ in path]
    for i in range(len(lit)):
        symbol = lit[i]
        if symbol in rules:
            lit[i] = rules[symbol]
    path = ''.join(lit)
    return path


rules = {
    'A':'B-A-B',
    'B':'A+B+A'
}
path = 'A'
t.speed(0)
for i in range(7):
    path = apply_rules(path,rules)
draw_path(path)
t.up()
t.goto(0,-340)
angle = 60
t.down()
draw_path(path)
t.up()
t.goto(0,-340)
angle = -60
t.down()
draw_path(path)

t.done()
