#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 11:21:18 2022

@author: Yang
"""
my_list = ["Maurice","Lisa","Kerry"]
print("{} is friends with {}.".format(my_list[0],my_list[-1]))

my_list[-1] = "Andy"
print(my_list)
print("{} is friends with {}.".format(my_list[0],my_list[-1]))
