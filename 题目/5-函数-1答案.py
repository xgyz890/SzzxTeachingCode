
#阶乘
def factorial(n):
	if n==1:
		return 1
	else:
		return n*factorial(n-1)


#Fibonacci
def fibo(n):
	if n==1 or n==2:
		return 1
	else:
		return fibo(n-1)+fibo(n-2)



#最大公约数
def gcd(x,y):
	while y!=0:
		t = x%y
		x = y
		y = t
	return x

def gcd(x,y):
	if x%y == 0:
		return y
	else:
		t = x%y
		return gcd(y,t)


#robber
def houserobber(x):
    if len(x)==0:
        return 0
    if len(x)==1:
        return x[0]
    dp = [0 for _ in x]
    dp[0] = x[0]
    for i in range(1,len(x)):
        if i==1:
            dp[i] = max(dp[0], x[i])
        else:
            dp[i] = max(dp[i-2]+x[i],dp[i-1])
    return dp[-1]

money=[3,8,6]
print(houserobber(money))
