import random
win_no_switch = 0       # 不换而获奖的计数器
win_switch = 0         # 换而获奖的计数器
n = 100000            # 换和不换各做这么多次实验

for i in range(n):               # 不换的实验
    door_list = ["A","B","C"]           # 三扇门的编号
    car = random.choice(door_list)      # 汽车随机放在某扇门后
    bet = random.choice(door_list)      # 挑战者随机选择一扇门
    if bet == car:                      # 不换，直接揭晓答案
        win_no_switch = win_no_switch + 1   

for i in range(n):               # 换的实验
    door_list = ["A","B","C"]           # 三扇门的编号
    car = random.choice(door_list)      # 汽车随机放在某扇门后
    bet = random.choice(door_list)      # 挑战者随机选择一扇门        
   
    
    host_list = ["A","B","C"]
    host_list.remove(bet)           # 主持人先去掉挑战者选择的门
    # 主持人预先知道汽车所在的门。如果上一步还没有排除，这里就排除出去
    if car in host_list:            
        host_list.remove(car)
    discard = random.choice(host_list) # 剩下的门里，随机排除一扇门
    
    
    # 现在挑战者决定换，即换成剩下的一扇门，看看是否获奖
    door_list.remove(bet)           # 去掉自己已经选过的门
    door_list.remove(discard)       # 去掉主持人排除的门
    bet = door_list[0]              # 只剩下一扇门，换成它!
    if bet == car:                  # 换！揭晓答案
        win_switch = win_switch + 1                  

print("不换的获奖概率：", win_no_switch/n)
print("换的获奖概率：  ", win_switch/n)