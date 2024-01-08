#判断输入的三个数,判断它们是否能构成三角形的三个边。

while True:
    a=int(input())
    b=int(input())
    c=int(input())
    if a+b>c and a+c>b and b+c>a:
        print('可以')
    else:print('不能')
