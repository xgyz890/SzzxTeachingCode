#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 20:33:22 2020

@author: Yang
"""

def solver(n,k):
    for i in range(1, k-2):
        for j in range(1, k-2):
            for s in range(1, k-2):
                if i+j+s==45 and i<j and j<s \
                    and 30*i+20*j+10*s==800:
                    print(i,j,s)
                    return None
    print("None")
    return None
            

solver(800, 45)