
# 函数
print("The winner is Allen")

def f():
    print("hello from a function")
    
f()


def f(name):
    print("The winner is",name)
f("Allen")
f("Bob")



def f(name="Cynthia"):
    print("The winner is",name)
f("Allen")
f()
f("Bob")







def f(x):
    y=x**2+3*x+5
    return y
r=f(3)
print(r)



for i in range(1,1000000):
    print("x=",i,"y=",f(i))



for k in range(1,100):
    print(k)









s=0
for i in range(1,1000):
    s=s+i**2
    print(s)










print(1e13)



def is_even(n):
    if n%2==0:
        return True
    else:
        return False
print(is_even(17))



n=int(input("n="))
if is_even(n):
    print("偶数")
else:
    print("奇数")


# 练习
#解方程
写一个计算器，求解一元一次方程 a*x+b=0
输入：a，b
输出：x
def calculator():
    a=int(input("a="))
    b=int(input("b="))
    
calculator()
    


# 解方程
写一个计算器，求解一元二次方程 a*x**2+b*x+c=0
输入：a，b，c
输出：x1，x2, 或者无实数根
def calculator2():
    a=int(input("a="))
    b=int(input("b="))
    c=int(input("c="))
    
calculator2()






#扩展：符号计算法
from sympy import *
from sympy.abc import *
solveset(Eq(1*x**2+3*x+10, 0), x, domain = Reals)










#视频：微积分的本质：
微积分的本质 3Blue1Brown @bilibili

#基础：求和
s=0
for k in range(1,101):
    s=s+2*(k+1)
    print(s)
print(s)

#1
用积分求圆面积的近似解，与理论值比较

def f(r,dr):
    s=0
    n=int(r/dr)

    print(s)
    print(math.pi*r**2)
    print(s-math.pi*r**2)

import math
r=10
dr=0.00001
f(r,dr)
314.15







s=0
for k in range(1,100):
    s=s+k*2+1
    print(s)


求函数 y=8*t-t**2 在[0,8]上的积分
def f(x,dx):
    s=0
    n=int(x/dx)
    #累加

    print(s)
x=8
dx=0.1
f(x,dx)
85.33





求函数 y=x**2+3 在[0,6]上的积分

def f(x,dx):
    s=0
    n=int(x/dx)

    print(s)
x=6
dx=0.001
f(x,dx)

90



#
用积分求球体体积的近似解，与理论值比较


def f(r,dr):
    n=int(r/dr)
    s=0


    print(2*s)
    print(math.pi*r**3*4/3)

import math
r=10
dr=0.000001
f(r,dr)


4188
















#
有一口锅，横截面轮廓符合方程 
y=1/8*x**2,x范围[-10,10]
求这口锅能装多少水

#along the y-axis
def f(y,dy):
    n=int(y/dy)
    s=0

    print(s)
import math
y=12.5
dy=0.0000001
f(y,dy)

1963.5=625*math.pi


#along the x-axis
def f(x,dx):
    n=int(x/dx)
    s=0



    print(s)

import math
x=10
dx=0.00001
f(x,dx)










s=0
for k in range(1,1000):
    s=s+5*(k+2)**0.5
print(s)












#计算椭圆面积

#微积分方法
def f(a,b,dx):
    s=0
    n=int(a/dx)
    for k in range(1,n+1):
        y=b*(1-(k*dx)**2/a**2)**0.5
        s=s+dx*y
    print(4*s)
    print(math.pi*a*b)
    
import math
a=10
b=6
dx=0.0001
f(a,b,dx)








# Monte Carlo
# https://www.bilibili.com/video/BV11M4y157Ko/
#（观看前6分钟）

#1，取点
#2，数点
#3，计算


# 随机采样：均匀分布
import numpy as np
n=1000
x=np.random.uniform(0,10,n)
print(x)
y=np.random.uniform(0,10,n)
print(y)

for i in range(len(x)):
    for j in range(len(y)):
        print(x[i],y[j])

# 一共n**2个点






# 求面积：圆 (example 1 in the video)
def f(n):
    m=0
    x=np.random.uniform(-1,1,n)
    y=np.random.uniform(-1,1,n)
    for i in range(len(x)):
        for j in range(len(y)):
            if :
                m=m+1
    print(4*m/n**2)
    
for i in range(10):
    f(300)

3-3.4



# 求面积：椭圆
def f(a,b,n):
    x=np.random.uniform(-a,a,n)
    y=np.random.uniform(-b,b,n)
    m=0
    for i in range(len(x)):
        for j in range(len(y)):
            if :
                m=m+1
    approx = m/n**2*4*a*b
    print(approx)
    real = math.pi*a*b
    print(real)
    print((real-approx)/real)
import math
import numpy as np
f(2,1,1000)












# 求面积：不规则图形
def f(n):
    x=np.random.uniform(0,2,n)
    y=np.random.uniform(0,2,n)
    m=0
    for i in range(len(x)):
        for j in range(len(y)):
            if and :
               m=m+1
    print(m/n**2*4)
import math
import numpy as np

f(300)

0.5855





import numpy as np
s=np.arcsin(np.sqrt(14)/4)- \
    4*np.arcsin(np.sqrt(14)/8)+ \
        np.sqrt(7)/2
print(s)



# 求积分

def f1(x):
    return 2*x+3

def f(a,b,n):
    x=np.random.uniform(a,b,n)
    s=0
    for i in range(len(x)):
        s=s+f1(x[i])
    avg=s/n
    print(avg*(b-a))

f(1,3,1000000)
真实值：14

#很方便地更换被积函数
def f1(x):
    return 1/(np.sin(x)*np.log(x))





