import math,random
n=10000
k=1000000
y=0
for _ in range(k):
    a=random.randint(1,n)
    b=random.randint(1,n)
    while a==b:
        b=random.randint(1,n)
    if math.gcd(a,b)==1:
        y+=1
print(y,m,y/m)
print(6/(math.pi**2))

# a math proof:
# https://math.stackexchange.com/questions/64498/probability-that-two-random-numbers-are-coprime-is-frac6-pi2