
#数字猜谜游戏—不断猜数，直到猜中或者猜的次数超过了5次

number=7         
guess=-7
n=0
while guess!=number and n<5:
    guess=int(input('请输入你猜的数：'))
    n=n+1
    if guess==number:
        print('猜对啦！')
        break
    elif guess>number:
        print("猜大了!")
    else:print("猜小了!")
       
print('你共猜了',n,'次')

