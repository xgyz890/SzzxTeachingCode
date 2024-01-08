一个正整数,如果它能被7整除,或者它的十进制表示法中某一位上的数字为7,则称其为与7相关的数。

现求所有小于等于n(n \le≤ 100)的与7无关的正整数的平方和。
输入为一行,正整数n(n \le≤ 100)
输出一行，包含一个整数，即小于等于n的所有与7无关的正整数的平方和。
n=int(input())
s=0
for i in range(1,n+1):
    if i%7!=0 and i//10!=7 and (i-7)%10!=0:
        s+=i*i
print(s)




n=int(input())
ans=int(0)
now=int(1)
while(now<=n):
    if(now//10!=7 and now%10!=7 and now%7>0):
        ans+=now*now
    now+=1
print(ans)
