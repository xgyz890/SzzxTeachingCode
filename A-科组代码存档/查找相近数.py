row_data=[-1,1,3,4,5,6,3,7,8]
look_for=2
min_diff=9999999999

for i in range(len(row_data)):
    
    diff=abs(row_data[i]-look_for)
    if diff<min_diff:
        min_diff=diff
        pos=[]        #如果有更近似的数，创建空列表pos用来存放位置   
        appro=[]      #创建空列表appro用来存放更近似的数
        pos.append(i)   #列表pos添加新的位置
        appro.append(row_data[i])   #列表appro添加新的数
        
    elif diff==min_diff:   #如果和最小差值相等，就在列表中添加该位置和数
        pos.append(i)
        appro.append(row_data[i])
        
for i in range(len(pos)):   #打印
    print('近似数位置:',pos[i],'近似数：',appro[i])
        
    
