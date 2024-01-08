#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 16:40:57 2021

@author: Yang
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("Tremor.xlsx", sheet_name = "Sheet3",header = 0)
tremor = list(df[df.columns[1]].dropna(axis = 0))
time = list(df[df.columns[0]].dropna(axis = 0))

valleys, peaks, t_valley, t_peak = [], [], [], []
i = 0

while i < len(tremor) - 1:
    print(i)
    while i < len(tremor) - 1 and tremor[i+1] <= tremor[i]:
        i += 1
    valleys.append(tremor[i])
    t_valley.append(time[i])
    while i < len(tremor) - 1 and tremor[i+1] >= tremor[i]:
        i += 1
    peaks.append(tremor[i])
    t_peak.append(time[i])

print("Total time is: {:.3f} s".format(time[-1] - time[0]))
print("There are {} valley points: \n".format(len(valleys)), valleys)
print("There are {} peak points: \n".format(len(peaks)), peaks)

plt.figure()
plt.plot(time, tremor, "gray")
plt.plot(t_valley, valleys, "ro")
plt.plot(t_peak, peaks, "yo")
plt.title("{} valley points, {} peak points".format(len(valleys),len(peaks)))
plt.show()