#编写一个程序，求出1/(1*2)-1/(2*3)+ 1/(3*4)-1/(4*5)+......,前n项和，n由用户输入

s=0
n=int(input())
i=1
while i<=n:
    if i%2==1:
        s=s+1/(i*(i+1))
    else:s=s-1/(i*(i+1))
    print(s)
    i+=1
print(s)
    
    
