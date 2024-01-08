#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 10:29:13 2021

@author: Yang
"""

import numpy as np

c = np.random.randint(1,100)

while True:
    guess = int(input("Enter a number:"))
    if guess > c:
        print("too large")
    elif guess < c:
        print("too small")
    else:
        print("correct!")
        break
