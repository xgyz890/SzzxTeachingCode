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

