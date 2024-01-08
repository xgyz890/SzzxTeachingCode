# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 15:49:20 2023

@author: HiteVision
"""


a=2
for n in range(a,a+20,2):
    for i in range(2,n):
        c=0
        for k in range(1,i+1):
            if i%k==0:
                c=c+1
        if c==2:
            j=n-i
            d=0
            for p in range(1,j+1):
                if j%p==0:
                    d=d+1
            if d==2:
                print("{:4d}={:3d}+{:3d}".format(n,i,j))
                break



def f(x):
    return x**(x**8)

b=2#上限是2
a=1#下限是1
diff=0.00000001
while True:
    x=(a+b)/2 #找到中点
    if f(x)<8: #如果中点小于真实值
        a=x #令新的下限等于中点
    if f(x)>8:
        b=x
    if abs(f(x)-8)<diff:
        print(x)
        print(f(x))
        break

import sympy
d = sympy.Symbol("d")
b = sympy.solve(d**(d**8)-8,d)
print(b)



# 分解质因数 n = 1300 = 2 * 2 * 5 * 5 * 13
n=int(input("输入一个数："))
d = 2 # 用d从2开始试，不成功则增加d
while n > 1:  # 目标未完成 还有质因数未提取
     if n % d == 0:
        print(d, end = ' ')
        n = n // d
     else:
        d = d + 1

a=2
while n>1:
    while n%a==0:
        print(a)
        n=n/a
    a=a+1


# s = 1/1 + 1/2 + 1/3 + 1/4 + ......
# 至少加到 1/d  s才能大于10
s = 0 # 累加
d = 1 # 从1/1开始
while s < 10:  # 目标未完成
     s = s + 1 / d
     d = d + 1
print(d)




# 百钱百鸡问题 100钱 要买 100只鸡
# x公鸡5钱一只，y母鸡3钱一只，z小鸡一钱3只  
for x in range(0, 20 + 1):
   for y in range(0, 33 + 1):
       for z in range(0, 300 + 1): 
           if x + y + z == 100 and 5 * x + 3 * y + z / 3 == 100:
               print(x, y, z)     
            
# 密码
pw = '123'
sec = 'Congratulations'
cnt = 0 # 连续错误次数
end=False
while not end:
    x = input('input password:')
    if cnt >= 2:
        print('locked')
        end=True
    else:
        if pw == x:
            print(sec)
            end=True
        else:
            print('wrong')
            cnt = cnt + 1
            