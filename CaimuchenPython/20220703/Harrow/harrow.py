#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 20:43:32 2022

@author: Yang
"""

import random
while True:
    a = input("please enter your school:")
    if "harrow" in a or "Harrow" in a:  
        print(random.randint(1,5))  
    else:
        print("you are not invited!")