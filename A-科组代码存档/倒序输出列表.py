while True:
    n=int(input())
    list1=[]
    list2=[]
    for i in range(n):
        a=int(input())
        list1.append(a)
    print(list1)
    for i in range(len(list1)):
        list2.append(list1[n-i-1])
    print(list2)
        
