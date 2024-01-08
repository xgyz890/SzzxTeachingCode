# _*_ coding:utf-8 _*_

correct = int(input("请指定正确数字： "))
while True:
    guess = int(input("请输入猜的数字： "))
    if guess == correct:
    	print("猜对了")
    	break
    if guess < correct:
    	print("数字太小")
    elif guess > correct:
        print("数字太大") 
