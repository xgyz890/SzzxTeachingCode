'''
小明想当丑国的总统，丑国大选是由n个州的投票结果来确定最终的结果的，
如果得到超过一半州的支持就可以当选，而每个州的投票结果又是由该州选民投票产生的，
如果某个州超过一半的选民支持小明，则他将赢得该州的支持。

现在给出丑国州每个州的选民人数，请问小明最少需要赢得多少选民的支持才能当选？
输入：输入数据四行整数（数字范围1- 5000）表示四个州的选民。
输出：输出最少获得总统的选民数。

while True:
  
    a=int(input())//2+1             #四个州选总统
    b=int(input())//2+1
    c=int(input())//2+1
    d=int(input())//2+1
    s=a+b+c+d-max(a,b,c,d)
    print(s)
'''   
while True:
    
    a=int(input())//2+1             #五个州选总统
    b=int(input())//2+1
    c=int(input())//2+1
    d=int(input())//2+1
    e=int(input())//2+1
    m1=max(a,b,c,d,e)
    if a==m1:
        m2=max(b,c,d,e)
        
    elif b==m1:
        m2=max(a,c,d,e)
    elif c==m1:
        m2=max(a,b,d,e)
    elif d==m1:
        m2=max(a,b,c,e)
    elif e==m1:
        m2=max(a,b,c,d)
    s=a+b+c+d+e-m1-m2
    print(s)
        
'''
while True:
    a=int(input())//2+1             #五个州选总统
    b=int(input())//2+1
    c=int(input())//2+1
    d=int(input())//2+1
    e=int(input())//2+1
    if a>=b and a>=c and a>=d and a>=e:
        a=b
        b=c
        c=d
        d=e
    elif b>=a and b>=c and b>=d and b>=e:
        a=a
        b=c
        c=d
        d=e
    elif c>=a and c>=b and c>=d and c>=e:
        a=a
        b=b
        c=d
        d=e
    elif d>=a and d>=b and d>=c and d>=e:
        a=a
        b=b
        c=c
  
    if a>=b and a>=c and a>=d:
        a=b
        b=c
        c=d
        
    elif b>=a and b>=c and b>=d :
        a=a
        b=c
        c=d
        
    elif c>=a and c>=b and c>=d:
        a=a
        b=b
        c=d
        
    print(a+b+c)
    
   '''




'''
输入（每个州的人数）                    输出
100
200
400
300
500                                     303

1134
4546
1231
1111
4546                                    1740

1
2
3
4
5                                        5

20
23
24
23
24                                      35

200
221
245
245
221                                     323
'''

