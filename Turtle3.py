# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 14:03:37 2023

@author: HiteVision
"""

# -*- coding: utf-8 -*-

import turtle as t

angle = 60 #通过改变角度，绘制出各种多边形
t.bgcolor('black')
t.pensize(2)
randomColor = ['red','blue','green','purple','gold','pink']
t.speed(0)
for i in range(200):
      t.color(randomColor[i%6])
      t.circle(i)
      t.rt(angle+1)
t.up()
t.color("#0fe6ca")
t.goto(0,0)
t.down()

