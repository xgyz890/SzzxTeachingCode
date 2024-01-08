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