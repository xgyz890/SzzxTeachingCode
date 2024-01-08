#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 10:01:03 2021

@author: Yang
"""

import random
import curses

s=curses.initscr()
curses.curs_set(0)
sh,sw=s.getmaxyx()
sh=sh+1 if sh%2==1 else sh+0
sw=sw+1 if sw%2==1 else sw+0
w=curses.newwin(sh,sw,0,0)
w.keypad(1) #accepts keyboard input
w.timeout(100)

snake_x=int(sw/4)
snake_y=int(sh/4)
snake=[
    [snake_y,snake_x],
    [snake_y,snake_x-1],
    [snake_y,snake_x-2],
    [snake_y,snake_x-3],
    [snake_y,snake_x-4]
]

food=[int(sh/1.5),int(sw/1.5)]
w.addch(food[0],food[1],curses.ACS_PI)

boundary=[]
for i in range(sw):
    boundary.append([0,i])
for j in range(sh):
    boundary.append([j,sw-1])
for i in range(sw-1,-1,-1):
    boundary.append([sh-1,i])
for j in range(sh-1,-1,-1):
    boundary.append([j,0])
for p in boundary:
    # cannot draw at [sh-1,sw-1] (lower right corner), error otherwise
    if p!=[sh-1,sw-1]:
        w.addch(p[0],p[1],curses.ACS_CKBOARD)

key=curses.KEY_RIGHT

while True:
    next_key=w.getch()
    key=key if next_key==-1 else next_key
    
    if snake[0][0] in [0,sh-1] or snake[0][1] in [0,sw-1] or snake[0] in snake[1:]:
        curses.endwin()
        quit()
        
    new_head=[snake[0][0],snake[0][1]]
    
    if key==curses.KEY_DOWN:
        new_head[0]+=1
    if key==curses.KEY_UP:
        new_head[0]-=1    
    if key==curses.KEY_LEFT:
        new_head[1]-=1    
    if key==curses.KEY_RIGHT:
        new_head[1]+=1
    
    snake.insert(0, new_head)
    
    if snake[0]==food:
        food=None
        while food is None:
            new_food=[
                random.randint(1,sh-2),    # so the next food does not appear on the edge lol
                random.randint(1,sw-2)
            ]
            food=new_food if new_food not in snake else None
        w.addch(food[0],food[1],curses.ACS_PI)
    else:
        tail=snake.pop()
        w.addch(tail[0],tail[1]," ")
        
    w.addch(snake[0][0],snake[0][1],curses.ACS_CKBOARD)
          