'''
输入一个只包含+-*/的一个运算式子，计算它的结果
输入格式：
输出格式：
'''
while True:
    num1=int(input())
    op=input()
    num2=int(input())

    if op == "+":
        print(num1,op,num2,'=',(num1+num2))
    if op == "-":
        print(num1,op,num2,'=',(num1-num2))
    if op == "*":
        print(num1,op,num2,'=',(num1*num2))
    if op == "/":
        print(num1,op,num2,'=',(num1/num2))    
