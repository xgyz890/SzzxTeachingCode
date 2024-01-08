#交换a,b的数，方法一：
a,b=10,20
print('原数；a=',a,' b=',b)
tmp=a       #交换a,b的数值
a=b
b=tmp      
print('交换后：a=',a,' b=',b)

#交换a,b的数，方法二：
a,b=10,20
print('原数；a=',a,' b=',b)
a,b=b,a    #交换a,b的数值
print('交换后：a=',a,' b=',b)

#斐波拉契数列
print('\n斐波拉契数列：')     #引号中加入\n表示换行
a,b=0,1
while b<1000:
    print(b,end=',')
    a,b=b,a+b           
    


    
