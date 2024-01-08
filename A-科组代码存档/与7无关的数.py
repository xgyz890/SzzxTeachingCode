'''
一个正整数，如果它能被7整除，或者它的某一位上的数字为7，则称其为“与7有关”的数。
现在，请编程求出所有小于或等于n的“与7无关”的正整数个数。
输入：一个正整数n，范围<=10^6。
输出：一个正整数，表示答案。
'''
while True:
    n=int(input())
    while n>=0:
        if n%7!=0:
            i=n
            flag=0
            while i>0:
                if (i%10)==7:
                    flag=1
                i=i//10
        n-=1


'''
输入                      输出
21                        17
'''

def has_7(num):
    while num>0:
        if num%10==7:
            return True
        num=num//10
    return False

while True:
    n=int(input("n="))
    for i in range(1,n+1):
        if i%7==0 or has_7(i):
            print(i)
    print("end")



  
