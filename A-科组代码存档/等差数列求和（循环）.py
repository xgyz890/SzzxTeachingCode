#输出等差数列，并求和
m,n,d=map(int,input("输入m,n,d:").split())
s=0;
for i in range(m,n,d):
    print(i,end=" ")
    s=s+i
print(s)

