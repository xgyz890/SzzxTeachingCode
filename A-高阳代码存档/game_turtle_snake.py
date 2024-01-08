
####################################################
#
#      Gao Yang
#      Snake game using turtle module 
#
####################################################
import turtle 
import time
import random
import os
from random import randrange
import pandas as pd
import numpy as np
import csv

soft_border = False
score = 0
header = ["Scores"]

# 储存每次的分数
if os.path.exists("scores.csv") > 0:

    df = pd.read_csv("scores.csv")

    # 这里注意：
    # df["Scores"] 是 series 类型，是类似字典的索引，不支持[-1]取末尾的操作
    # 另外 series 的值需要判断类型，不如 list 简单
    # 所以转换成 list 再取最大值
    highest_score = max(list(df["Scores"]))
    
else:
    with open("scores.csv", "w") as f:
        f_writer = csv.DictWriter(f, fieldnames = header)
        f_writer.writeheader()
    highest_score = 0
    
    
delay = 0.1
BREAK_FLAG = False

bg_color = "orange"
head_color = "black"
body_color = "white"
food_colors = ["red","yellow"]
foods = ["type1", "type2"]
border_color = "white"
pen_color = "white"
label_font = ("Roman", 14, "normal")
end_font = ("Roman", 40, "normal")

s = turtle.Screen()
s.title("Snake game")
s.tracer(0)
s.setup(650, 650)
s.bgcolor(bg_color)

border = turtle.Turtle()
border.hideturtle()
border.penup()
border.goto(-300,300)
border.pendown()
border.color(border_color)
border.pensize(4)
border.goto(-300,-300)
border.goto(300,-300)
border.goto(300,300)
border.goto(-300,300)

snake = []
for i in range(3):
    segment = turtle.Turtle()
    segment.shape("square")
    segment.color(head_color)
    segment.penup()
    if i > 0:
        segment.color(body_color)
    snake.append(segment)

# 1~n 一共 n 个数里选 1 个数，选中 1 的概率是 1/n

food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color(food_colors[0])
food.penup()
food.goto(randrange(-280,280,20), randrange(-280,280,20))

# 海龟不能从朝上直接变成朝下。所以当 head 向上运动时，按下 down（往往为误触）应该设计为没有反应。
# 下面的方法没有考虑到这一点：
# s.onkeypress(lambda:snake[0].setheading(90), "Up")
# s.onkeypress(lambda:snake[0].setheading(180), "Left")
# s.onkeypress(lambda:snake[0].setheading(270), "Down")
# s.onkeypress(lambda:snake[0].setheading(0), "Right")
# 结果是 head 反向移动到 body 里，触发游戏结束条件，这显然不够合理。

# 因此加上这个 feature：

def go_up():
    if snake[0].heading() != 270:
        snake[0].setheading(90)

def go_down():
    if snake[0].heading() != 90:
        snake[0].setheading(270)

def go_left():
    if snake[0].heading() != 0:
        snake[0].setheading(180)

def go_right():
    if snake[0].heading() != 180:
        snake[0].setheading(0)

s.onkeypress(go_up, "Up")
s.onkeypress(go_down, "Down")
s.onkeypress(go_left, "Left")
s.onkeypress(go_right, "Right")

s.listen()

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.penup()
pen.color(pen_color)
pen.goto(-280,250)

while True:
    
    pen.clear()
    pen.write("Current: {} \nHighest: {}".format(score, highest_score), 
              align = "Left", font = label_font)
    
    snake_pos = [(i.position()) for i in snake]
    # 用turtle 自带工具 distance(), 用来计算 turtle 到 x,y 的距离
    if snake[0].distance(food) < 10:

        new_food_x, new_food_y = randrange(-280,280,20), randrange(-280,280,20)
        while (new_food_x, new_food_y) in snake_pos:
            new_food_x, new_food_y = randrange(-280,280,20), randrange(-280,280,20)
        food.goto(new_food_x, new_food_y)
        
        segment = turtle.Turtle()
        segment.color(body_color)
        segment.shape("square")
        segment.penup()
        snake.append(segment)
        score += 1*10
 
    for i in range(len(snake) - 1, 0, -1):
        x = snake[i-1].xcor()
        y = snake[i-1].ycor()
        snake[i].goto(x,y)
    
    snake[0].fd(20)
    s.update()

    x_cor = snake[0].xcor()
    y_cor = snake[0].ycor()
    
    if soft_border:
        if x_cor >= 300:
            x_cor -= 600
            snake[0].goto(x_cor, y_cor)
        elif x_cor <= -300:
            x_cor += 600
            snake[0].goto(x_cor, y_cor)
        if y_cor >= 300:
            y_cor -= 600
            snake[0].goto(x_cor, y_cor)
        elif y_cor <= -300:
            y_cor += 600
            snake[0].goto(x_cor, y_cor)
    else:
        if x_cor >= 300 or x_cor <= -300 or y_cor >= 300 or y_cor <= -300:
            BREAK_FLAG = True

    for i in snake[1:]:
        i = i.position()
        if snake[0].distance(i) < 10:
            BREAK_FLAG = True

    if BREAK_FLAG:
        s.bgcolor("red")
        pen.goto(0,0)
        pen.write("GAME OVER", align = "Center", font = end_font)
        break

    time.sleep(delay)

# 注意 open 里面的”a“模式代表”继续写入“，
# 如果写成了”w”就会覆盖之前的数字
with open("scores.csv", "a") as f:
    f_writer = csv.DictWriter(f, fieldnames = header)
    info = {"Scores": score}
    f_writer.writerow(info)

# 启动事件循环：调用Tkinter的mainloop函数。
# 必须是乌龟图形程序中的最后一个语句
s.mainloop()
# turtle.done()

