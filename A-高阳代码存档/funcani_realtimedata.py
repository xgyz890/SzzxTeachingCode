#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 11:52:45 2020

@author: Yang
"""
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import pandas as pd

plt.style.use("fivethirtyeight")
def animate(i):
    data=pd.read_csv("realtimedata.csv")
    x=data["x_values"]
    y1=data["total_1"]
    y2=data["total_2"]
    y3=data["total_3"]
    
    plt.cla()
    plt.plot(x,y1,label="c1")
    plt.plot(x,y2,label="c2")
    plt.plot(x,y3,label="c3")
    plt.legend(loc="upper left")
    plt.tight_layout()

ani=animation.FuncAnimation(plt.gcf(), animate, interval=200)
#ani.save("funcani_realtimedata.mp4")
print("video saved")
plt.show()