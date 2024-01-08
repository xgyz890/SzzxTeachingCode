import math
a,b,c=eval(input('输入一元二次方程的a,b,c,(用逗号分隔):'))
if a<=0:
    print('不是一元二次方程')
else:
    dlt=b*b-4*a*c
    if dlt>0:
        x1=(-b+math.sqrt(dlt))/(2*a)
        x2=(-b-math.sqrt(dlt))/(2*a)
        print('有两个解：',x1,'，',x2)
    elif dlt==0:
        x1=(-b+math.sqrt(dlt))/(2*a)
        print('有一个解：',x1)
    else:print('无解')
