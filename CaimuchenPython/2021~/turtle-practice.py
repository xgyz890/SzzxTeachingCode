from turtle import *
from math import *

color = ["purple","black"]
step = 160
n = 7

home() # pos = (0,0), direction = right (which is 0 degrees)
pencolor(color[0])
width(4)

for i in range(n):
    forward(step)
    penup()
    backward(step)
    pendown()
    left(360/n)

penup()
forward(step)
left(180/n + 90)
pendown()
pencolor(color[1])

y = 2*step*cos((90-180/n)/360*(2*pi))
for i in range(n):
    forward(y)
    left(360/n)

hideturtle()
mainloop()


