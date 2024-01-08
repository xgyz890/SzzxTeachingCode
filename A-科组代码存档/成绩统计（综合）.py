#逐个输入学生的语文、数学、英语成绩，输出每位同学的总分、平均分
#统计最大和最小的总分

n=int(input())
Max=0
Min=1000
for i in range(1,n+1):
    a,b,c=map(int,input().split())
    total=a+b+c
    ave=(a+b+c)/3
    print(total,' ',ave)
    if total>Max:
        Max=total
    if total<Min:
        Min=total
print(Max,' ',Min)
