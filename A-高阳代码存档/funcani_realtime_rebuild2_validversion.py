#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 11:52:45 2020

@author: Yang

Ref: funcani_decay.py
"""
import itertools
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

plt.style.use("fivethirtyeight")
fig, ax=plt.subplots(figsize=(6,6))
xdata,y1data,y2data=[],[],[]
line1, =plt.plot([],[],"-r",lw=1.5,label="series a",animated=True)
line2, =plt.plot([],[],"-y",lw=1.5,label="series b",animated=True)

ax.legend(loc="upper left")
ax.set_xlabel("Time")
ax.set_ylabel("Amount")
plt.tight_layout()

def init():
    ax.set_xlim(0,200)
    ax.set_ylim(800,1200)
    return line1,line2, 

def y_gen(init, frame,r1,r2):
    y=init
    for _ in range(frame):
        y+=np.random.randint(r1,r2)
    return y

def data_gen():
    for frame in itertools.count():
        y1=y_gen(800,frame,-10,25)
        y2=y_gen(1000,frame,-15,20)
        yield frame,y1,y2
    
def update(data):
    frame, y1,y2=data
    xdata.append(frame)
    y1data.append(y1)
    y2data.append(y2)
    
    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()
    if frame >= xmax:
        ax.set_xlim(0, 1.2*xmax)
        ax.figure.canvas.draw()
    if y1>=ymax or y1<ymin or y2>=ymax or y2<ymin:
        ax.set_ylim(0.9*ymin, 1.1*ymax)
        ax.figure.canvas.draw()
        
    line1.set_data(xdata,y1data)
    line2.set_data(xdata,y2data)
    return line1,line2,

ani=animation.FuncAnimation(fig, update, frames=data_gen, 
                            interval=5,init_func=init, blit=True)
plt.show()

