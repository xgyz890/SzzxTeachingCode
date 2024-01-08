#-*- coding: utf-8 -*-

import numpy as np
from scipy.optimize import leastsq
import matplotlib.pylab as pl


def func(x,p):
    """数据拟合所用的函数：A*sin(2*pi*k*x+theta)"""

    A,k,theta=p  #p为系数
    return A*np.sin(2*np.pi*k*x+theta)

def residuals(p,y,x):
    """实验数据x,y和拟合函数之间的差，p为需要拟合的系数"""

    return y-func(x,p)

#在0～-2*np.pi均匀返回100个数字
x=np.linspace(0,-2*np.pi,100)

A,k,theta=10,0.34,np.pi/6   #真实数据的函数参数
y0=func(x,[A,k,theta])
y1=y0+2*np.random.randn(len(x)) #加入噪声之后的实验数据

p0=[7,0.2,0] #第一次猜测的函数拟合参数

#调用leastsq进行数据拟合
#residuals为计算误差的函数
#p0为拟合参数的初始值
#args为需要拟合的实验数据
plsq=leastsq(residuals,p0,args=(y1,x))

print("Real_parameter：",[A,k,theta])
print("Fitting_parameters" ,plsq[0])



pl.plot(x,y0,label="RealData")
pl.plot(x,y1,label="NoiseData")
pl.plot(x,func(x,plsq[0]),label="FittingData")

pl.legend()
pl.show()

















#coding:utf-8

import scipy.optimize as opt
import numpy as np


def test_fmin_convolve(fminfunc,x,h,y,yn,x0):
    """x(*)h=y卷积
        yn为在y的基础上添加一些干扰噪声的结果
        x0为求解x的初始值
        """

    def convolve_func(h):
        """计算yn-x(*)h的power
            fmin将通过计算使得此power最小
        """
        return np.sum((yn-np.convolve(x,h))**2)

    #调用fmin函数，以x0为初始值
    h0=fminfunc(convolve_func,x0)

    print(fminfunc.__name__)
    print("----------------------")

    #输出x(*)h0和y之间的相对误差
    print("error of y:",float(np.sum(np.convolve(x,h0)-y)**2)/np.sum(y**2))

    #输出h0和h之间的相对误差
    print("error of h:",float(np.sum((h0-h)**2)/np.sum(h**2)))
    print('/n')

def test_n(m,n,nscale):
    """随机产生x,h,y,yn,x0等数列，调用个和宗fmin函数求解b
        m为x的长度，n为h的长度，nscale为干扰强度
    """

    x=np.random.rand(m)
    h=np.random.rand(n)
    y=np.convolve(x,h)

    yn=y+np.random.rand(len(y))*nscale
    x0=np.random.rand(n)

    test_fmin_convolve(opt.fmin,x,h,y,yn,x0)
    test_fmin_convolve(opt.fmin_powell,x,h,y,yn,x0)
    test_fmin_convolve(opt.fmin_cg,x,h,y,yn,x0)
    test_fmin_convolve(opt.fmin_bfgs,x,h,y,yn,x0)


test_n(200,20,0.1)









#coding:utf-8
from scipy.optimize import fsolve
from math import sin,cos



def f(x):
    x0=float(x[0])
    x1=float(x[1])
    x2=float(x[2])
    return [
        5*x1+3,
        4*x0*x0-2*sin(x1*x2),
        x1*x2-1.5
    ]

result=fsolve(f,[1,1,1])  #输入一组可能解

print(result)
print(f(result))  #返回误差


