a=int(input())
s=0
n=a
m=0
while n>0:      # 反复循环，直到n=0
    m=n%10      #求出个位数
    if m%2==0:         #判断个位数，偶数就加入s
        s=s+m
    n=n//10       # 去除个位数
print(s)
