#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 15:54:08 2020

@author: Yang
"""
n = 500
ans = []
count = 0
for i in range(n):
    if i%3==2 and i%5==3 and i%7==2:
        count += 1
        ans.append(i)
print("{} answers in {}: {}".format(count, n, ans))