
import turtle

s = turtle.getscreen()
s.title("Sprial")
turtle.setup(800, 800)
turtle.bgcolor("black")

t = turtle.Turtle()
t.setheading(90)
t.speed(5)
t.pensize(4)

pen = turtle.Turtle(visible = False)
pen.color("white")
pen.penup()
pen.goto(300,300)
pen.pendown()

n = 42
fd_dis = 10
dis_delta = 1
angle_delta = 8
pencolors = ["white","red","blue",
             "green","purple","yellow"]
pen_font = ("Arial", 14)

for i in range(1,n+1):
    pen.write("Sprial {}/{}".format(i,n), font = pen_font)
    for j in range(6):
        t.pencolor(pencolors[j])
        t.fd(fd_dis)
        t.lt(60 - angle_delta)
        fd_dis += dis_delta
    pen.clear()

turtle.done()






