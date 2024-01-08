import random
print(random.randint(0,9))    #生成0—9之间的随机整数

a=random.uniform(10,20)      #a=10—20之间的随机浮点数
print(a)
a=round(random.uniform(10,20),2) #b=10—20之间的随机浮点数，保留小数2位
print(a)

print(random.random())          #生成0—1.0之间的随机浮点数
print(round(random.random(),3)) #生成0—1.0之间的随机浮点数，保留小数3位



print(random.randrange(10,20,2)) #生成10-20之间的整数，间距为2
