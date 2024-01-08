while True:
    n=int(input('请输入老师需要的铅笔数量:'))
    n1,p1=map(int,input('请输入第一种包装铅笔的数量和价格：').split())
    n2,p2=map(int,input('请输入第二种包装铅笔的数量和价格：').split())
    n3,p3=map(int,input('请输入第三种包装铅笔的数量和价格：').split())

    if n%n1==0:num1=n//n1  #计算第一种铅笔需要买多少包
    else:num1=n//n1+1
    s1=num1*p1             #买第一种包装的铅笔需要多少钱

    if n%n2==0:num2=n//n2  #同理计算买第二种铅笔需要多少钱
    else:num2=n//n2+1
    s2=num2*p2

    if n%n3==0:num3=n//n3  #同理计算买第三种铅笔需要多少钱
    else:num3=n//n3+1
    s3=num3*p3


    if s1<=s2 and s1<=s3:print('买第一种铅笔最省钱，花费：',s1)      
    elif s2<=s1 and s2<=s3:print('买第二种铅笔最省钱，花费：',s2) 
    elif s3<=s1 and s3<=s2:print('买第三种铅笔最省钱，花费：',s3) 


