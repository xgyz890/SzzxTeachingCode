#患者就诊管理系统
print("欢迎光临患者就诊管理系统")
jiuzhen=[]

while True:
    menu=int(input("1:排队  2:就诊  3:查看排队  4:下班  请您输入序号："))
    if menu==1:
        num=input("请输入病历号码：")
        jiuzhen.append(num)
        print("添加成功")
    elif menu==3:
        print("查看排队")
        for a in jiuzhen:
            print(a)
    elif menu==2:
        print("请",jiuzhen[0],"就诊")
        jiuzhen.pop(0)
    
    elif menu==4:
        print("已下班，以下病人请明天来就诊，已将您的就诊号保存，并安排至明天优先就诊")
        print(jiuzhen)
        print("程序运行结束")
        break
    else:print("输入错误")
