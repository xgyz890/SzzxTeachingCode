
#while循环

#数字猜谜游戏（1）—不断猜数，直到猜中为止
number=7         
guess=-1
print('数字猜谜游戏—不断猜数，直到猜中为止')
n=1            # n用来存放猜的次数
while guess!=number:
    guess=int(input('\n输入你猜的数：'))
    if guess==number:
        print('猜对啦！')
    else:
        print('错啦！继续猜')
        n+=1     # n=n+1
print('一共猜了',n,'次\n')
       
#数字猜谜游戏（2）—最多可以猜5次，猜中结束
number=7
guess=-1
print('数字猜谜游戏—最多可以猜5次')
n=1
while n<=5:   
    guess=int(input('输入你猜的数：'))
    if guess==number:
        print('猜对啦！')
        break            #如果猜中，退出循环
    else:
        print('错啦！你还有',5-n,'次机会')
        n=n+1


    
