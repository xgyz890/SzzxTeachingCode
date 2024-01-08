#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 11:52:45 2020

@author: Yang
"""
import itertools
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

plt.style.use("fivethirtyeight")

fig, ax=plt.subplots()
xdata,ydata=[],[]
line, =plt.plot([],[],"ro",animated=True)

def init():
    ax.set_xlim(-np.pi,np.pi)
    ax.set_ylim(-1.1,1.1)
    return line,

def data_gen():
    frame=-np.pi
    step=2*np.pi/120
    while frame<np.pi:
        frame+=step
        yield frame
    
def update(frame):
    xdata.append(frame)
    ydata.append(np.sin(frame))
    line.set_data(xdata,ydata)
    return line,

ani=animation.FuncAnimation(fig, update, frames=data_gen, interval=10,
                            init_func=init, blit=True)

plt.show()

