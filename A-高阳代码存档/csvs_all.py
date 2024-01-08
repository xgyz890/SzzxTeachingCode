#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 16:28:06 2020

@author: Yang
"""
import pandas as pd
import csv
import math

df = pd.read_excel("~/Documents/SMS/Semester_one/students_2020_all.xlsx")

a = df["学号"]
num_list_all = list(a)
print(len(num_list_all))

def gen_csv(num_list, k):
    csv_name = "student_group_" + str(k) + ".csv"
    with open(csv_name, mode="w") as f:
        f_writer = csv.writer(f)
        for i in range(len(num_list)):
            f_writer.writerow([num_list[i],num_list[i],num_list[i]])
    print("generated")
    
seg = 100
for i in range(math.ceil(len(num_list_all)/seg)):
    print(i)
    if i<len(num_list_all)//seg:
        seg_list = num_list_all[i*seg:(i+1)*seg]
    else:
        seg_list = num_list_all[i*seg:]
    gen_csv(seg_list, i+1)


    