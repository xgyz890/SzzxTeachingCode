score = int(input("成绩："))
if score <= 100 and score >= 90:
    print("A+")
else:
    if score >= 80:
        print("A")
    else:
        if score >= 70:
            print("B")
        else:
            if score >= 60:
                print("C")
            else:
                print("D")


x = int(input("x = "))
print(x)

x = float(input("x = "))
if x > -2:
    y = x ** 2 + 3 * x + 2
else:
    y = 2 ** x
print("y = ", y)


a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
if a > b:
    m = a
else:
    m = b
if m > c:
    print(m)
else:
    m = c
    print(m)

a = float(input("a="))
b = float(input("b="))
c = float(input("c="))
if a + b > c and b + c > a and c + a > b:
    print("yes")
else:
    print("no")


import random

from perfectnum import is_prime

a = random.randint(1, 1000)  # 生成随机整数，范围1~1000
b = int(input("请输入猜的数字："))
if b == a:
    print("猜对了！")
elif b < a:
    print("数字太小")
else:
    print("数字太大")


x = int(input("x="))
points = 0
if x > 89:
    points += 4
elif x > 79:
    points += 3
elif x > 69:
    points += 2
else:
    points += 0


x = int(input("x="))
points = 0
if x > 89:
    points += 4
if x > 79:
    points += 3
if x > 69:
    points += 2
if x < 70:
    points += 0


m = int(input("请输入一个三位数："))
ge = m % 10
shi = m // 10 % 10
bai = m // 100
print("个位：", ge)
print("十位：", shi)
print("百位：", bai)


a = int(input("请输入三角形边长1："))
b = int(input("请输入三角形边长2："))
c = int(input("请输入三角形边长3："))
if a + b > c and a + c > b and b + c > a:
    print("可以")
else:
    print("不可以")

m = int(input("请输入一个三位数："))
ge = m % 10
shi = m // 10 % 10
bai = m // 100
if ge == 0 or shi == 0 or bai == 0:
    print("no!")
elif (m % ge == 0 and m % shi == 0) and m % bai == 0:
    print("yes!")
else:
    print("no!")


year = int(input("请输入年份："))

if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    print("yes")
else:
    print("no")


from threading import Thread, Lock

number = 0
lock = Lock()


def target():
    global number
    for _ in range(1000000):
        with lock:
            number += 1


thread_01 = Thread(target=target)
thread_02 = Thread(target=target)
thread_01.start()
thread_02.start()

thread_01.join()
thread_02.join()

print(number)


for i in range(1, 5):
    print("Hello world!")

n = int(input("n="))
i = 2
flag = True

while i < n:
    if n % i == 0:
        flag = False
        break
    i = i + 1

if flag is True:
    print("质数")
else:
    print("非质数")


import random

a = random.randint(1, 1000)  # 生成随机整数，范围1~1000
while True:
    b = int(input("请输入猜的数字："))
    if b == a:
        print("猜对了！")
        break
    elif b < a:
        print("数字太小")
    else:
        print("数字太大")

n = 1
while n < 20:
    if n % 3 == 0:
        n = n + 1
        continue
    if n == 13:
        break
    print(n)
    n = n + 1

n = 1
while n < 100:
    if n == 8:
        break
    print(n)
    n = n + 1

n = 5
i = 1
while i <= n:
    print("* " * i)
    i = i + 1
while i > 0:
    print("* " * i)
    i = i - 1

print("ABC-" * 4)

i = 1
while i < 100:
    i = i + 1
    if i == 45:
        break
    print(i)

i = 1
while i < 100:
    i = i + 1
    if i == 45:
        continue
    print(i)

for num in [1, 2, 3]:
    print(n)


n = int(input("台阶级数："))
if n < 2:
    y = 1
else:
    first = 1
    second = 1
    i = 2
    while i <= n:
        y = first + second
        first = second
        second = y
        i = i + 1
print(y)

for n in range(2, 101):
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(n)

for n in range(1, 10001):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s = s + i
    if s == n:
        print(n)

n = int(input("请输入一个数："))
while n > 0:
    print(n % 10, end=" ")
    n = n // 10

i = 1
while i < 100:
    i = i + 1
    if i == 45:
        break
    print(i, end=" ")

i = 1
while i < 100:
    i = i + 1
    if i == 45:
        continue
    print(i, end=" ")

k = int(input("Enter a number:"))
s = 0
for n in range(1, k + 1):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    s = s + f
print(s)

print(123 ** (31 * 71) % 253)

for k in range(1, 100):
    d = (220 * k + 1) / 31
    if int(d) == d:
        print(d, k)

M = "F"
print(M >= "D")
print(M >= "H")


n = int(input("n="))
x = int(input("x="))
count = 0
for i in range(1, n + 1):
    while i > 0:
        if i % 10 == x:
            count = count + 1
        i = i // 10
print(count)


def is_prime(a):
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False
    return True


n = int(input("n="))
if n % 2 == 0:
    for n1 in range(3, n // 2 + 1):
        if is_prime(n1) and is_prime(n - n1):
            print(n1, n - n1)
            break
else:
    print("n is not even.")
