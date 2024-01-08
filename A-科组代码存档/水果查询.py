class Fruit():
    def _init_(self):
        name="name"
        price=0
    def msg(self):
        print('这是',self.name,'它的价格是',self.price)
        
xj=Fruit()
xj.name='香蕉'
xj.price=3

jz=Fruit()
jz.name='桔子'
jz.price=4

xl=Fruit()
xl.name='香梨'
xl.price=5

pt=Fruit()
pt.name='葡萄'
pt.price=8

xg=Fruit()
xg.name='西瓜'
xg.price=2


n=int(input('请输入要查询的水果 1、香蕉 2、桔子 3、香梨 4、葡萄 5、西瓜(请输入数字)'))
if n==1:
    xj.msg()
elif n==2:
    jz.msg()
elif n==3:
    xl.msg()
elif n==4:
    pt.msg()
elif n==5:
    xg.msg()
else:
    print('输入错误，请输入数字1-5')
