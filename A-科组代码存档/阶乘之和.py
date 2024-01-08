while True:
    
    s=0
    n=int(input())
    for i in range(1,n+1):
        s1=1
        for j in range(1,i+1):
            s1*=j
        s+=s1
    print(s)


    
