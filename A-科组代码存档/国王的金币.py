'''
国王将金币作为工资，发放给忠诚的骑士。
第一天，骑士收到一枚金币；之后两天（第二天和第三天），每天收到两枚金币；
之后三天（第四、五、六天），每天收到三枚金币；
之后四天（第七、八、九、十天），每天收到四枚金币……；
这种工资发放模式会一直这样延续下去：
当连续N天每天收到N枚金币后，骑士会在之后的连续N+1天里，每天收到N+1枚金币。

请计算在前K天里，骑士一共获得了多少金币。
输入：一个正整数K（1=< K <=10^4），表示发放金币的天数。
输出：一个正整数，即骑士收到的金币数。
'''
while True:
    k=int(input("k="))   # 总天数
    i=1
    s=0                  # 总金币
    while k>=i:
        s=s+i*i
        k=k-i
        i=i+1
    print(s+k*i)
    
        
'''
输入(正整数n,天数）             输出（金币数）
6                               14
10                               30
50                              335
100                             945
'''

        













