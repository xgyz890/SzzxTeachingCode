#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 14:09:51 2020

@author: Yang
"""
import csv
import time
import random


x=0
t1=1000
t2=1000
t3=1000


fieldnames=["x_values","total_1","total_2","total_3"]

with open("realtimedata.csv", "w") as f:
    csv_writer=csv.DictWriter(f,fieldnames=fieldnames)
    csv_writer.writeheader()

while True:
    with open("realtimedata.csv", "a") as f:
        csv_writer=csv.DictWriter(f,fieldnames=fieldnames)
        info={
            "x_values":x,
            "total_1":t1,
            "total_2":t2,
            "total_3":t3}
        csv_writer.writerow(info)
        
        print(x,t1,t2,t3)

        x+=1
        t1+=random.randint(-6,8)
        t2+=random.randint(-5,6)
        # t3*=random.uniform(0.90,1.11)
        t3+=random.randint(-5,7)
    time.sleep(0.02)