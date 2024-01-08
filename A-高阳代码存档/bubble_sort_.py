#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 16:06:05 2020

@author: Yang
"""

def bub_sort(s):
    for k in range(len(s)-1, 0, -1):
        for i in range(k):
            if s[i] > s[i+1]:
                t = s[i+1]
                s[i+1] = s[i]
                s[i] = t


a = [81,35,2,97,44,56]
bub_sort(a)
print(a)