#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 14:51:44 2021

@author: Yang
"""

import pandas as pd

a = pd.read_excel("test_vlookup.xlsx",sheet_name="Sheet1")
b = pd.read_excel("test_3_copy.xlsx",sheet_name="Sheet1")

res = pd.merge(a,b,how="left",on="学号")
print(res)

w = pd.ExcelWriter("res.xlsx")
res.to_excel(w, index=False)
w.save()
