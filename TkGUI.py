#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 16:38:04 2021

@author: Yang
"""

"""
from tkinter import *

def p_label():
    global root
    lb=Label(root,text="我爱学习，学习使我快乐！")
    lb.pack()

root=Tk()
root.title("window")
B=Button(root,text="click",command=p_label,bg="red")
B.pack()
root.mainloop()
"""

import calendar
from tkinter import *
root=Tk()

def label_cal(year,month):
    label=Label(root,text=str(year)+"年")
    label.grid(row=0,column=2)
    label=Label(root,text=str(month)+"月")
    label.grid(row=0,column=4)

    labels=[["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]]
    month_cal=calendar.monthcalendar(year,month)

    for r in range(7):
        for c in range(7):
            label=Label(root,
                        width=5,
                        padx=5,
                        pady=5,
                        text=" ")
            label.grid(row=r+1,column=c)
    for i in range(len(month_cal)):
        labels.append(month_cal[i])
        
    for r in range(len(month_cal)+1):
        for c in range(7):
            if labels[r][c]==0:
                labels[r][c]=" "
            label=Label(root,
                        width=5,
                        padx=5,
                        pady=5,
                        text=str(labels[r][c]))
            label.grid(row=r+1,column=c) #注意缩进，此行应该属于内侧的for循环，否则只会画出最后一列日期

year,month=2021,10
label_cal(year,month)

def button_pre():
    global year,month
    month-=1
    if month<1:
        month+=12
        year-=1
    label_cal(year,month)

button1=Button(root,text="previous",command=button_pre)
button1.grid(row=8,column=0)

def button_next():
    global year,month
    month+=1
    if month>12:
        month-=12
        year+=1
    label_cal(year,month)

button2=Button(root,text="next",command=button_next)
button2.grid(row=8,column=6)

root.mainloop()
