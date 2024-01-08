
# 函数


# 1,自觉型。无自变量，无返回值
print("Allen")
print("Bob")
print("Chris")
print("Dylan")


def f():
    print("Allen")
    print("Bob")
    print("Chris")
    print("Dylan")
f()


def f2():
    f()
    f()
    f()
f2()


#2,默默奉献型。有自变量，无返回值
def out_n(n):
    for i in range(1,n+1):
        print(i,end=" ")
        
out_n(100)
out_n(999)
out_n(500)





#3,有始有终型。有自变量，有返回值
def add(m,n):
    c=m+n
    return c
r=add(1111,9999)
print(r)

def quadratic_f(x):
    y=x**2+3*x+1
    return y
c=quadratic_f(1)
print(c)


import math
def my_sin(x):
    y=math.sin(x/2)
    return y
print(my_sin(math.pi))


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


for n in range(0,100):
    c=quadratic_f(n)
    print(c)

# 练习

输出y=x**2-2*x+4 在x=1~20的值
例如x=1，y=3
def f():
    for x in range(1,21):
        y = x**2-2*x+4
        print("x=",x,"y=",y)
f()

def quadratic_f(x):
    y=x**2-2*x+4
    return y

def f():
    for x in range(1,21):
        print("x=",x,"y=",quadratic_f(x))
f()

输入一个正整数n，输出1~n每个数的平方
例如输入3，输出1,4,9
def f():
    n=int(input("n="))
    for k in range(1,n+1):
        print(k**2)
f()

输入一个数n，判断它是否是质数
素数=质数=只有1和它本身两个因数的正整数
例如 2,3,5,7
非素数（合数）：4,6,8
def is_prime(n):
    for k in range(2,n):
        if n%k==0:
            return False
    return True
print(is_prime(16))


输出 1~100 的每一个素数
def f():
    for n in range(2,101):
        if is_prime(n):
            print(n)
f()





用函数求解一元二次方程
def solver(a,b,c):
    if a==0:
        return "不是二次方程"
    else:
        delta=b**2-4*a*c
        if delta<0:
            return "无实数根"
        elif delta==0:
            x1=(-b+delta**0.5)/2*a
            return x1
        else:
            x1=(-b+delta**0.5)/2*a
            x2=(-b-delta**0.5)/2*a
            return x1,x2
print(solver(0,-2,2))







# 递归
输出斐波那契数列的前n项

def factorial(n):
    if n==1:
        return 1
    else:
        return factorial(n-1)*n
factorial(4)


def fibonacci(n):
    if n==1 or n==2:
        return 1
    else:
        result = fibonacci(n-1)+fibonacci(n-2)
        return result

def f5():
    n=int(input("n="))
    for i in range(1,n+1):
        print(fibonacci(i))
f5()













定义函数，功能为：输入一个正整数 n，输出 1~n 之间（包含 n）所有的完全
平方数。
示例：
输入：99
输出：1,4,9,16,25,36,49,64,81


def f():
    n=int(input("n="))
    for i in range(1,n+1):
        for m in range(1,n+1):
            if i==m**2:
                print(i)
f()



def f1():
    n=int(input("n="))
    i=1
    while i**2<=n:
        print(i**2)
        i=i+1
f1()




def f2():
    n=int(input("n="))
    for i in range(1,n+1):
        if is_squarenumber(i):
            print(i)
f2()




