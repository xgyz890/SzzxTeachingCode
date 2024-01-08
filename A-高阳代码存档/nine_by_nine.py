#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 20:46:17 2020

@author: Yang
"""

for i in range(1,10):
    for j in range(1,i+1):
        print("{}*{}={:d}".format(j,i,i*j), end=" ")
    print("\n")