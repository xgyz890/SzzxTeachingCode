"""
从前有个国王准备奖赏发明国际象棋的人。 那个人说：“我就要米。国际象棋盘有64个格，
第1格放1粒米，第2格放2粒米，第3格放4粒米，第4格放8粒米，以此类推，每个格的米粒数是前一格的2倍。” 
国王答应了，结果把一个王国的米粒都放进去也不够，国王疑惑不解。
请你编写程序为国王解惑。
"""
s=0
n=1
for i in range (1,65):
    s=s+n     #两句都填空，从下面选择
    n=n*2
print(s)
    


'''
选择：
A n=n*2  s=s+n
B n=n*n  s=s+n
C s=s+i  i=i*2  
D s=s+n  n=n*2
'''