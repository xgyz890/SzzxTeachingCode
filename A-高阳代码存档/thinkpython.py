#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 10:17:45 2020

@author: Yang
"""
f=open("words.txt")
d={}
for line in f:
    word=line.strip()
    d[word]=len(word)
