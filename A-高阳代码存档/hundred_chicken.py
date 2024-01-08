#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 15:29:22 2020

@author: Yang
"""
def solver(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i+j+k == 100 and 5*i + 3*j + 1/3*k == 100:
                    print(i, j, k)

solver(100)
