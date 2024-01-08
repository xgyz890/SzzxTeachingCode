# 倒序输出百位数
# 输入123，输出321
n=int(input())
ge=n%10
shi=n//10%10
bai=n//100
print(ge,shi,bai)
