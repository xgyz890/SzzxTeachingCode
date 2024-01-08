#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 20:54:47 2020

@author: Yang
"""
for a in range(10):
    b = a
    for c in range(10):
        d = c
        for x in range(int(1000**0.5),100):
            num = 1000*a+100*b+10*c+d
            if num == x**2:
                print(num, x)
                
                