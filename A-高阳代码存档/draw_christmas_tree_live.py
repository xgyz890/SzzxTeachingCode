
import threading
import random
import os
import time


tree=list(open("tree.txt").read().rstrip()) # so we can change the tree later, based on the txt file
mutex=threading.Lock()

def colored_dot(color):
    if color=="red":
        return f"\033[91m\033[0m"   # use 91 to make it red, use 0 to return to defalut color.
    if color=="green":
        return f"\033[92m\033[0m"   # use 92 to make it green, use 0 to return to defalut color.
    if color=="yellow":
        return f"\033[93m\033[0m"   # use 93 to make it yellow, use 0 to return to defalut color.
    if color=="blue":
        return f"\033[94m\033[0m"   # use 94(?) to make it blue, use 0 to return to defalut color.

def lights(color, indexes):
    off=True
    while True:
        for idx in indexes:
            tree[idx]=colored_dot(color) if off else "" # to light the bulbs that are off

        mutex.acquire() # to ensure "draw a tree" and "clear the screen" will happen one after another
        os.system("cls" if os.name=="nt" else "clear")
        print("".join(tree))
        mutex.release() # to unlock the threads

        off=not off
        time.sleep(random.uniform(0.3,0.7))

yellow=[]
blue=[]
red=[]
green=[]

for i,c in enumerate(tree):
    if c=="Y":
        yellow.append(i)
        tree[i]="✸"
    elif c=="R":
        red.append(i)
        tree[i]=""
    elif c=="G":
        green.append(i)
        tree[i]=""
    elif c=="B":
        blue.append(i)
        tree[i]=""

thread_y=threading.Thread(target=lights,args=("yellow",yellow))
thread_b=threading.Thread(target=lights,args=("blue",blue))
thread_r=threading.Thread(target=lights,args=("red",red))
thread_g=threading.Thread(target=lights,args=("green",green))

for t in [thread_y,thread_b,thread_r,thread_g]:
    t.start()
for t in [thread_y,thread_b,thread_r,thread_g]:
    t.join()

print("".join(tree),yellow)

