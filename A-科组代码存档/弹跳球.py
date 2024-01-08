#弹跳球 
n=int(input('输入n:'))
s=100
i=1
a=100
while i<n:
    #print('小球第',i,'次落地经过的距离=',s)
    a=a/2
    s=s+a*2
    i+=1
    
print('小球第',i,'次落地经过的距离=',s)    
