#while True:
    
    s=0
    s1=1
    n=int(input())
    for i in range(1,n+1):
        s1*=i
        s+=s1
    print(s)
