#求 n!
n=int(input())
s=1
for i in range(1,n+1,1):
    
      s*=i
print(s)

#求和1+2+3+...+n
#输入格式：一个100以内的数，表示n
#输出格式：和的值
n=int(input())
s=0
for i in range(1,n+1):
    
      s+=i
print(s)
