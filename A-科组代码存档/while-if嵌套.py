#了解数据类型转换

num=' '

while True:
    num=input("请输入一个整数，输入q结束：")         #输入的是字符串
    if num=='q':break         #输入字母q结束循环     
    else:
        num=int(num)          #转换字符串为整型
        if num%2==0:
           if num%3==0: print(num,"可以整除 2 和 3")
           else: print(num,"可以整除 2，但不能整除 3")
        else:
           if num%3==0:print(num,"可以整除 3，但不能整除 2")
           else: print(num,"不能整除 2 和 3")
      
