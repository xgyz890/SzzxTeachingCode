# 挂盐水的时候，如果滴起来有规律，先是滴一滴，停一下；
# 然后滴二滴，停一下；再滴三滴，停一下...，
# 现在有一个问题：这瓶盐水一共有VUL毫升，每一滴是D毫升，
# 每一滴的速度是一秒（假设最后一滴不到D毫升，则花费的时间也算一秒），
# 停一下的时间也是一秒这瓶水什么时候能挂完呢？
# Input
# 由VUL和D组成，其中 0<D<VUL<5000。第一行VUL，第二行D
#Output
#请输出挂完盐水需要的时间
#Sample Input 1 
#10
#1
#Sample Output 1
#13

v=int(input("V="))
d=int(input("D="))
drop=1
time=0
time2=0
if v%d==0:
    time+=v//d
else:
    time+=v//d+1
i=1
while time2<time:
    time2+=i
    i=i+1
print(int(time+i-2))


v=int(input("V="))
d=int(input("D="))
s=0
i=1
t1=0
while s<v:
    s=s+i*d
    t1=t1+i
    i=i+1
s_1=s-(i-1)*d
v_1=v-s_1
k=1
while k*d<v_1:
    k=k+1
print(t1-1+k)