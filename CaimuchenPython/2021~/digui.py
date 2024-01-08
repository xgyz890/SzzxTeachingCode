#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 10:00:15 2021

@author: Yang
"""

def s(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        result = s(n-1) + s(n-2)
        return result

print(s(20))