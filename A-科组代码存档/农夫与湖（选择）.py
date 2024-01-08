'''
农夫约翰想要定居在一个地方（x,y），但是坐标（0,0）中有一个湖。这个湖每年
面积增长 50 平方米，农夫想要知道，在他有生之年居住的地方会不会被水淹没。
输入三个正整数 X,Y,N。 X,Y 分别代表农夫现在的居住坐标， N 则代表农夫剩下的
日子。如果农夫能安享晚年，则输出 Nice,否则输出 Unfortunate
'''
x = int(input('请输入横坐标;'))
y = int(input('请输入纵坐标;'))  
n = int(input('请输入年份;'))
s=50*n/3.14
if x*x+y*y<=s:
 print('Unfortunate')
else:
 print('Nice')
