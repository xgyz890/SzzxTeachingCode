#循环条件，循环变量初始值，循环变量变化

#一、1-10输出。
'''
i=1
while i <= 10:
    print(i)
    i=i+1
'''    

#二、1+2+3....+N
'''
while True:
    N=int(input("请输入一个N:"))
    s=0
    i=0
    while i < N:
        i=i+1
        s=s+i
        #print(s)
    print(N,"以内数的和为：",s)
'''
'''
while True:
    N=int(input("请输入一个N:"))
    s=0
    for i in range(1,N+1,1):
        s=s+i
    print(N,"以内数的和为：",s)
'''
#三、1*2*3....N(阶乘) 0!=1
'''
while True:
    N=int(input("请输入一个N:"))
    s=1
    i=0
    while i < N:
        i=i+1
        s=s*i
    print(N,"的阶乘为：",s)
'''
#四、N!+(N-1)!+(N-2)!.....2!+1! N以内数的阶乘和？
'''
while True:
    N=int(input("请输入一个N:"))
    s=1
    i=0
    h=0
    while i < N:
        i=i+1
        s=s*i
        h=h+s
    if N == 0:
        h = 1
    print(N,"以内数的阶乘和为:",h)
'''
#for:循环条件，循环变量初始值，循环变量变化
#for i in range(i=1,i<11,i=i+1):
"""
for i in range(1,11,1):
    print(i)
"""
'''
*
**
***
****
*****
******
'''
'''
while True:
    N=int(input("请输入一个数N:"))
    j=1
    while j <= N:

        i=0
        while i < j:
            print("*",end="") 
            i = i + 1

        print("")

        j = j + 1

'''








































