# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 17:18:03 2022

@author: yang-
"""

import os
os.chdir("D:\Documents\Code\Filename_example") # change it to your own path.
# print(os.getcwd())

for f in os.listdir():
    # print(f)
    # print(os.path.splitext(f))
    
    f_name, f_ext = os.path.splitext(f)
    # print(f_name.split("-"))
    
    f_title, f_num = f_name.split("-")
    # print(f_title)
    
    # print("{}-{}{}".format(f_num, f_title, f_ext))
    
    # 1. deal with white spaces
    f_title = f_title.strip()
    # f_num = f_num.strip()
    
    # print("{}-{}{}".format(f_num, f_title, f_ext))
    
    # 2. remove the # sign
    # f_num = f_num.strip()[1:]
    
    # print("{}-{}{}".format(f_num, f_title, f_ext))
    
    # 3. pad the single digits with 0s
    f_num = f_num.strip()[1:].zfill(2)
    
    print("{}-{}{}".format(f_num, f_title, f_ext))
    
    new_name = "{}-{}{}".format(f_num, f_title, f_ext)
    
    # os.rename(f, new_name)
    
    
    