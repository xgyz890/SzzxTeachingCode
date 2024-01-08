# 原理


# 解 x**2=a

def square(a):
    x0 = 10 #初始点，也可以是别的值
    x1 = x0-(x0**2-a)/(2*x0)
    i=0
    while abs(x1-x0)>1e-5:
        x0 = x1
        x1 = x0-(x0**2-a)/(2*x0)
        # 输出精确到小数点后四位
        print('迭代第{}次，解={:.4f}'.format(i,x1))
        i=i+1
square(2)




# 解 a*x**3+b*x**2+c*x+d = 0   在-1.5附近的解
def cubic(a,b,c,d):
    x0 = 100 #初始点，也可以是别的值
    x1 = x0-()/()
    i=0
    while abs(x1-x0)>1e-5:
        x0 = x1
        x1 = x0-()/()
        print('迭代第{}次，解={:.4f}'.format(i,x1))
        i=i+1
cubic(1,2,3,4)


#用sympy求解，检验牛顿迭代的正确性
from sympy import *
x= symbols('x')
print('方程的解：')
a=solveset(x**3+2*x**2+3*x+4, x, domain = Reals) 
print(float(list(a)[0])) # 把解变为小数












# 导数越来越复杂，表达式越来越长。改进：用符号运算求导

# 解 x**2 = a
from sympy import *
# 方程统一写在这里
def f(x):
    f = x**2-10
    return f

def solver():
    x = symbols('x')
    x0 = 1
    i = 0
    x1 = x0 - f(x0)/diff(f(x),x).subs(x,x0)
    while abs(x1-x0)>1e-6: 
        x0=x1
        x1=x0-f(x0)/diff(f(x),x).subs(x,x0)
        i=i+1
        print('迭代第{}次，解={}'.format(i,float(x1)))
solver()






# 解 cosx = x
# 只需要改变f
def f(x):
    f = cos(x)-x
    return f

solver()














# 解方程组

import numpy as np

def Fun(x,num):
    # 方程组在这里，三个变量分别是x的三个分量，num是未知数个数，这里是2，f是两个方程组
    i = num
    f = np.zeros((i),dtype=float)
    f[0] = x[0]**3-x[1]**2+1.    #x**3-y**2+1=0
    f[1] = x[0]**2-x[1]-1.    #x**2-y-1=0
    return f

#计算雅可比矩阵的逆矩阵
def dfun(x,num):                         
    df = np.zeros((num,num),dtype=float)
    dx = 0.00001                           
    x1 = np.copy(x)    #x1 = x
    for i in range(0,num):              # 求导数，i是列，j是行
        for j in range(0,num):
            x1 = np.copy(x)
            x1[j] = x1[j]+dx           #x+dx
            df[i,j] = (Fun(x1,num)[i]-Fun(x,num)[i])/dx   #f(x+dx)-f（x）/dx
    df_1 = np.linalg.inv(df)                              #计算逆矩阵
    return df_1

def Newton(x,num):
    x1 = np.copy(x)  #x1 = x   1行num列
    i = 0
    delta = np.copy(x)
    while(np.sum(abs(delta)) > 1.e-8 and i < 100):  #控制循环次数
        x1 = x-np.dot(dfun(x,num),Fun(x,num))  #公式 x_k+1 = x_k - (dF(x_k))^(-1)·F(x_k)
        delta = x1-x     #比较x的变化
        x = x1
        i = i+1
        print(x)
    return x

# 方程未知数的个数
num = 2                     
#初始值
x = np.array((-1,1), dtype=float)
print(x)
a = Newton(x,num)
print(a)

#用sympy求解，检验牛顿迭代的正确性
import sympy
x,y = sympy.symbols('x,y')
print('方程的解：')
print(sympy.solve([x**3-y**2+1, x**2-y-1], [x,y]))
