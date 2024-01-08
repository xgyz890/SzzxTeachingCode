'''
输入一个三位数
输出它的数字大写写法
'''
while True:
    number=int(input("plz input a number:"))
    while number>999 or number<100:
        number=int(input("plz reinput a number:"))
        
    b=number//100
    s=number//10%10
    g=number%10
    
    if b==1:
        b='一'
    elif b == 2:
        b='二'
    elif b == 3:
        b='三'
    elif b == 4:
        b='四'
    elif b == 5:
        b='五'
    elif b == 6:
        b='六'
    elif b == 7:
        b='七'
    elif b == 8:
        b='八'
    elif b == 9:
        b='九'

    if b==1:
        b='一'
    elif b == 2:
        b='二'
    elif b == 3:
        b='三'
    elif b == 4:
        b='四'
    elif b == 5:
        b='五'
    elif b == 6:
        b='六'
    elif b == 7:
        b='七'
    elif b == 8:
        b='八'
    elif b == 9:
        b='九'

    if s==1:
        s='一'
    elif s == 2:
        s='二'
    elif s == 3:
        s='三'
    elif s == 4:
        s='四'
    elif s == 5:
        s='五'
    elif s == 6:
        s='六'
    elif s == 7:
        s='七'
    elif s == 8:
        s='八'
    elif s == 9:
        s='九'

    if g==1:
        g='一'
    elif g == 2:
        g='二'
    elif g == 3:
        g='三'
    elif g == 4:
        g='四'
    elif g == 5:
        g='五'
    elif g == 6:
        g='六'
    elif g == 7:
        g='七'
    elif g == 8:
        g='八'
    elif g == 9:
        g='九'

    if s == 0 and g == 0:
        print(b+'百')
    elif g == 0:
        print(b+'百'+s+'十')
    elif s == 0:
        print(b+'百'+'零'+g)
    else:
        print(b+'百'+s+'十'+g)
