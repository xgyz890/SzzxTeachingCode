#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 15:29:22 2020

@author: Yang
"""
def solver():
    for i in range(int(100/5)+1):
        for j in range(int(100/3)+1):
            k = 100 - i - j
            if 5*i + 3*j + 1/3*k == 100:
                    print(i, j, k)

solver()
