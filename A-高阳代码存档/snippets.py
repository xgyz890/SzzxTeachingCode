# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 09:00:52 2020

@author: Yang
"""
##################################################

a = int(input("a = "))
b = int(input("b = "))

n = int((10*a + b) / 19)
m = 10*a + b - 19*n

print("n=", n)
print("m=", m)

###################################################

a = int(input("a = "))
b = int(input("b = "))

n = (10*a + b) // 19
m = (10*a + b) % 19

print("n=", n)
print("m=", m)

###################################################

a = 1
b = 2
if a>b:
    print(a)
else:
    print(b)
    
###################################################

x = float(input("a = "))

if a>=0:
    print(a)
else:
    b = -a
    print(b)

###################################################

a = 3
b = 8
c = 4

if a>b:
    m = a
else:
    m = b
if m>c:
    print(m)
else:
    m = c
    print(m)
    
###################################################

x = float(input("x = "))

if x>0:
    y = x**2 + 3*x + 2
elif x>-2 and x<=0:
    y = abs(x-1)
else:
    y = 2**x

print(y)
    
    
###################################################
   
x = float(input("x = "))

if x <= 200:
    cost = 0.66*x
elif x<=400:
    cost = 0.71*(x-200) + 0.66*200
else:
    cost = 0.96*(x-400) + 0.71*(400-200) + 0.66*200
    
print(cost)


###################################################
  
year = int(input("请输入年份："))

if year%400 == 0:
    print("yes")
else:
    if year%100 == 0:
        print("no")
    else:
        if year%4 == 0:
            print("yes")
        else:
            print("no")
            
###################################################

year = int(input("请输入年份："))

if year%400 == 0:
    print("yes")
elif year%100 == 0:
    print("no")
elif year%4 == 0:
    print("yes")
else:
    print("no")
    
    
###################################################

a = int(input("请指定正确数字： "))
b = int(input("请输入猜的数字： "))
if b == a:
    print("猜对了")
else:
    if b < a:
        print("数字太小")
    else:
        print("数字太大") 
    
###################################################

a = int(input("请指定正确数字： "))
b = int(input("请输入猜的数字： "))
if b == a:
    print("猜对了")
elif b < a:
    print("数字太小")
else:
    print("数字太大") 
        
        
###################################################
  
x = float(input("x = "))

if x<=200:
    y = 0.66*x
else:
    if x<=400:
        y = 0.71*(x-200) + 0.66*200
    else:
        y = 0.96*(x-400) + 0.71*(400-200) + 0.66*200
    
print(y)



###################################################

import math

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if a == 0:
    print("不是一元二次方程")
else:
    delta = b*b - 4*a*c
    if delta<0:
        print("无实数解")
    else:
        if delta == 0:
            x = -b/(2*a)
            print("有一个解: ",x)
        else:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            print("有两个解: ",x1,", ",x2)

###################################################

def is_prime(k):
    for i in range(2,int(k**0.5)+1):
        if k%i == 0:
            return False
    return True

for i in range(2,10000):
    if is_prime(i):
        print(i)
        
###################################################

sentence = "Mary has a little lamb"
for character in sentence:
    print(character, ord(character))

###################################################    
       
x = int(input("请输入成绩（整数）："))

if 90<=x<=100:
    print("A")
elif 80<=x<90:
    print("B")
elif 70<=x<80:
    print("C")
elif 60<=x<70:
    print("D")
elif 0<=x<60:
    print("E")
else:
    print("成绩无效")

###################################################

x = int(input("请输入成绩（整数）："))

if 90<=x<=100:
    print("A")
else:
    if 80<=x<90:
        print("B")
    else:
        if 70<=x<80:
            print("C")
        else:
            if 60<=x<70:
                print("D")
            else:
                if 0<=x<60:
                    print("E")
                else:
                    print("成绩无效")
                    
###################################################

a = 30
b = 2
if a>=25:
    a = 20
elif a>=28:
    a = 40
elif a>30:
    b = a
else:
    b = 0
print(a,b)

###################################################

a = 20
b = 5.1
print(int(a/(b-1)))

###################################################

print("python"*3)

###################################################

n = 1
n = n+1
print(n)
n = n+1
print(n)
n = n+1
print(n)
n = n+1
n = n+1
n = n+1
print(n)

###################################################

n = 58
a = bin(n)
print(a)
b = hex(n)
print(b)
c = oct(n)
print(c)

###################################################

a = 144
b = 24 + 45 + int(a/3)
c = a/1.2
if b>c:
    print("green")
else:
    if b==c:
        print("red")
    else:
        print("black")
        
###################################################

a = 2
b = 1
if (a<=2 and b>=0) and a-3*b>=0:
    c = 2*a-3*b
else:
    c = 3*a-1
print(c)

###################################################

# 演示错误程序
# a = 32
# if a<25:
#     print("a+1”)
# else:
#       x = a-16
#     print（(x-1)*2)）

###################################################

n=1
while n<=10:
    print(n)
    n=n+1

n=10
while n>=1:
    print(n)
    n=n-1

n=1
while n<=100:
    if n%2==0:
        print(n)
    n=n+1


n=0
while n<=20:
    print(n)
    n=n+2

k=int(input("k="))
s=0
i=1
while i<=k:
    s=s+i
    i=i+1
print(s)

###################################################


a=int(input("请输入正确数字："))
count=0
while True:
    b=int(input("请输入猜的数字："))
    count=count+1
    if b==a:
        print("猜对了！")
        print("使用的次数：",count)
        break
    elif b<a:
        print("数字太小")
    else:
        print("数字太大")
    
###################################################

male=0
female=0
total=int(input("总人数为："))
count=0
while count<total:
    p=int(input("性别："))
    if p==0:
        female=female+1
        count=count+1
    elif p==1:
        male=male+1
        count=count+1
    else:
        print("输入错误，重新输入")
print("男生人数：",male)
print("女生人数：",female)
        
###################################################

for i in range(1,21):
    print(i)

for i in range(1,501):
    if i%4==0:
        print(i)
    
for i in range(1,501):
    if i%2==0 and i%4!=0:
        print(i)

###################################################

k=int(input("k="))
s=1
i=1
while i<=k:
    s=s*i
    i=i+1
print(s)

###################################################

k=int(input("输入一个数："))
i=1
while i<k:
    if k%i==0:
        print(i)
    i=i+1


i=1
while i<=10000:
    k=1
    s=0
    while k<i:
        if i%k==0:
            s=s+k
        k=k+1
    if s==i:
        print(i)
    i=i+1
print("end")

for k in range(1,10000):
    m=0
    for i in range(1,k):
        if k%i==0:
            m=m+i
    if m==k:
        print(m)
        
###################################################

for i in range(10,0,-1):
    print(i)


for i in range(1,11):
    print("*"*i)
    
###################################################

n=int(input("n="))
while n>0:
    print(n%10)
    n=n//10


n = int(input("n="))
reverse_n = 0
while n>0:
    last_d = n%10
    reverse_n= reverse_n*10 + last_d
    n = n//10
print("reverse number is:{:s}".format(reverse_n))
    
###################################################

for z in range(1,13):
    if 4*z==50:
        print(z)
print("end")


for y in range(1,11):
    for z in range(1,13):
        if 4*z+5*y==50:
            print(y,z)
print("end")

for x in range(1,9):
    for y in range(1,11):
        for z in range(1,13):
            if 4*z+5*y+6*x==50:
                print(x,y,z)
print("end")
    
###################################################

for x in range(0,21):
    for y in range(0,34):
        for z in range(0,101):
            if 5*x+3*y+z/3==100 and x+y+z==100:
                print(x,y,z)
print("end")

###################################################

a1=int(input("a1="))
d=int(input("d="))
n=int(input("n="))
s=0

an=a1+(n-1)*d
for i in range(a1, an+1, d):
    print(i)
    s=s+i
print("Sum: ",s)

###################################################

k=int(input("k="))
s=1
for i in range(1,k+1):
    s=s*i
print(s)

s=0
money=20
n=0
while s<=500:
    s=s+money
    money=money+5
    n=n+1
print(n)

s=1
for i in range(1,5):
    s=s*i
print(s,i)

k=int(input("k="))
for i in range(1,k+1):
    if k%i==0:
        print(i)
        
for i in range(10,100,30):
    print(i)

for i in range(1,10):
    print(i)
    if i%3==0:
        break

k=int(input("k="))
for i in range(1,k):
    if k%i==0:
        print(i)

s=0
for i in range(10,1,-2):
    s=s+i
print(s)

'''
程序的输出结果是：
A 28  B 29  C 30  D 31
'''

for i in range(0,100):
    if i%7==0 and i%5==0:
        print(i)

'''
程序的输出结果是：
三行填空
'''

x1=0
for i in range(1,11):
    x=int(input("请输入正整数："))
    if x>x1:
        x1=x
print("最大的数字是：", x1)

 
x1=100
for i in range(1,11):
    x=int(input("请输入一个 100 以内的正整数："))
    if x<x1:
        x1=x
print("最小的数字是：", x1)

n=1
s=0
for i in range(1,65):
    s=s+n
    n=n*2
print("总数为：",s)

s=0
for i in range(1,20):
    if i%3==0:
        s=s+i
print(s)

s=1
for i in range(1,11):
    if i%2==0:
        s=s*i
print(s)

n=int(input("n="))
for i in range(1,n+1):
    s=" "*(int(0.5*((2*n-1)-(2*i-1))))
    print(s+"*"*(2*i-1)+s)
    
s=0
for i in range(1,65):
    s=s+2**(i-1)
print(s)

# s=0
# for i in range(1,11)
#     if i%2=0:
#     x=i*i  
#         s=s+x
    
k=int(input("输入一个数："))
for i in range(1,k):
    if k%i==0:
        print(i)


def findx(x,nums):
    for num in nums:
        print(num)
        if num==x:
            print("found")
            break

findx(1,[0,2,4,5,6,7,1])    
    
import itertools
k=10000000
for i in itertools.count():
    if (2*i+1)%(i+1)==0:
        print(i)
    if i>k:
        break
        
print("done")

a=20
b=80
if b>a:
    t=a
    a=b
    b=t
m=0


for i in range(1,b+1):
    if a%i==0 and b%i==0:
        m=i
print(m)

###################################################
class_28=["Jim","Ned","Jason","Tim","Howard","Mike","Jane","Jennifer"]
numbers=[82,78,25]
for everynumber in numbers: 
    print(everynumber//2+1)
    
for i in range(1,10):
    if i%5==0:
        break
    print(i)
else:
    print("no")



import itertools
import time
for i in itertools.count(10,0.5):
    print(i)
    time.sleep(0.5)
    

for z in range(1,12):
    if 4*z==44:
        print(z)
print("end")


import timeit
start=timeit.default_timer()
s=0
for i in range(1,100):
    for j in range(1,100):
        s=i*j
        print(s,end=" * ")
print(s)
end=timeit.default_timer()
print("total:{:.5f}s".format(end-start))


n=int(input("n="))
for k in range(2,n+1):
    for i in range(2,int(k**0.5)+1):
        if k%i==0:
            break
    else:
        print(k)

x1=100
y1=100
z1=100
s=x1+y1+z1
r=1000-(1.8*x1+1.9*y1+2.1*z1)
for x in range(100,555+1):
    for y in range(100,526+1):
        for z in range(100,476+1):
            if 1.8*x+1.9*y+2.1*z<=1000:
                if x+y+z>s:
                    s=x+y+z
                    r=1000-(1.8*x+1.9*y+2.1*z)
                    x1=x    # 储存目前最优的 x
                    y1=y    # 储存目前最优的 y
                    z1=z    # 储存目前最优的 z
                elif x+y+z==s and 1000-(1.8*x+1.9*y+2.1*z)<r:
                    r=1000-(1.8*x+1.9*y+2.1*z)
                    x1=x
                    y1=y
                    z1=z
            else:
                break
print("单价 1.8 元物品数量为：",x1,"件")            
print("单价 1.9 元物品数量为：",y1,"件")            
print("单价 2.1 元物品数量为：",z1,"件")
print("共买到礼物总数量为：",s)
print("剩余金额：",r,"元")            


x1=2
y1=2
s=x1+y1
r=19-(x1+2*y1)
for x in range(2,20):
    for y in range(2,10):
        if x+2*y<=19:
            if x+y>s:
                s=x+y
                r=19-(x+2*y)
                x1=x
                y1=y
            elif x+y==s and 19-(x+2*y)<r:
                r=19-(x+2*y)
                x1=x
                y1=y
        else:
            break
print("第一种元件数量为：",x1)
print("第二种元件数量为：",y1)
print("总数为：",s)
print("余额是：",r)


k=10
for i in range(2,k+1):
    for j in range(2,i):
        if i%j==0:
            break
        print(i)
        
        
for n in range(50,201):
    if n%3==2 and n%5==4 and n%7==6:
        print("n=",n)
    

x1=100
for i in range(1,11):
    x=int(input("请输入一个 100 以内的正整数："))
    if x<x1:
        x1=x
        i_final=i
print("最小的数字是：",x1,"，输入序号为：",i_final)
        
# 骑士金币

while 1:
    k=int(input("k="))
    s=0
    for day in range(1,k+1):
        if k>day:
            s=s+day**2
            k=k-day
        else:
            break
    res=s+k*day
    print(res)


while 1:
    k=int(input("k="))
    s=0
    day=1
    while k>day:
        s=s+day*day
        k=k-day
        day=day+1
    res=s+k*day
    print(res)
    
# 滴盐水

while True:
    v=int(input("V="))
    d=int(input("D="))
    s=0
    i=1
    t1=0
    while s<v:
        s=s+i*d
        t1=t1+i
        i=i+1
    s_1=s-(i-1)*d
    v_1=v-s_1
    k=1
    while k*d<v_1:
        k=k+1
    print(t1-1+k)
    
while True:
    v=int(input("V="))
    d=int(input("D="))
    drop=1
    time=0
    time2=0
    if v%d==0:
        time+=v//d
    else:
        time+=v//d+1
    i=1
    while time2<time:
        time2+=i
        i=i+1
    print(int(time+i-2))
        

    
# 猴子吃桃

while 1:
    n=int(input("n="))
    s=1
    for i in range(1,n):
        s=(s+1)*2
        print('第',n-i,'天，有',s,'个桃')
    print(s)
    

# 与 7 有关

while True:
    n=int(input("n="))
    for i in range(1,n+1):
        if i%7==0 or "7" in str(i):
            print(i)
    print("end")

while True:
    n=int(input("n="))
    for i in range(1,n+1):
        if i%7==0:
            print(i)
        else:
            i_copy=i
            has_7=False
            while i>0:
                if i%10==7:
                    has_7=True
                i=i//10
            if has_7:
                print(i_copy)
    

import string
import random
# s=string.ascii_letters + string.digits + string.punctuation
s=string.ascii_letters + string.digits + "!@#$%^&*"
for k in range(10):
    real="".join(random.choice(s) for i in range(3))
    a=""
    i=1
    while a!=real:
        a="".join(random.choice(s) for i in range(3))
        i+=1
    print("i={},password={}".format(i,a))
    
    
for k in range(2,100):
    is_prime = True
    for j in range(2,k):
        if k%j == 0:
            is_prime = False
    if is_prime:
        print(k)
        

def countdown(n):
    if n <= 0:
        print("blastoff!")
    else:
        print(n)
        return countdown(n-1)



