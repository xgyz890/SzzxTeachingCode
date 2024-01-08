#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 16:50:28 2020

@author: Yang
ref:
    matplotlib.org -> gallery -> animation decay
"""
import itertools

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

plt.style.use("fivethirtyeight")

def data_gen():
    for cnt in itertools.count():
        t = cnt / 10
        yield t, np.sin(2*np.pi*t) * np.exp(-t/10.)


def init():
    ax.set_ylim(-1.1, 1.1)
    ax.set_xlim(0, 10)
    del xdata[:]
    del ydata[:]
    line.set_data(xdata, ydata)
    return line,


def run(data):
    # update the data
    t, y = data
    xdata.append(t)
    ydata.append(y)
    xmin, xmax = ax.get_xlim()

    if t >= xmax:
        ax.set_xlim(xmin, 2*xmax)
        ax.figure.canvas.draw()
    line.set_data(xdata, ydata)
    ax.grid()

    return line,

fig, ax = plt.subplots()
line, = ax.plot([], [], "b", lw=2)
xdata, ydata = [], []

ani = animation.FuncAnimation(fig, run, data_gen, 
                              interval=10, 
                              init_func=init)
plt.show()