# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 11:14:18 2021

@author: gaoyang
"""

import random
import time
sleep_time=0.4
sleep_time_round=1
r = 1


switch=int(input("默认Boss生命值={}点\n默认玩家生命值={}点\\n\n是否要修改？\n(1=是,0=否)".format(300,100)))
if switch==1:
    s="请输入 Boss 生命值、玩家生命值和回合0数，用逗号隔开："
    boss_life,player_life=map(int,input(s).split(","))
else:
    boss_life=300
    player_life=100
print("\n设定完毕\nBoss生命值={}点\n玩家生命值={}点\n".format(boss_life,player_life))
print("\n游戏开始！\n")
time.sleep(sleep_time_round)


def draw_frac(n):
    k=random.randint(1,n)
    if k==1:
        return True
    else:
        return False


while True:
    print("*"*40)
    print("Round {:2d}:\n".format(r))
    
    boss_damage=random.randint(1,20)
    if boss_damage>10:
        print("巨龙喷出了火焰！")
    else:
        print("巨龙使用了冲撞。")
        
    o=int(input("选择对策（0=防御，1=攻击）："))

    player_damage=0
    if o==1:
        print("你拿出剑向 Boss 砍去！")
        player_damage=random.randint(20,50)
        if draw_frac(5):
            player_damage=player_damage*4
            print("暴击！！")
        player_damage=int(player_damage*0.8)
        boss_life=boss_life-player_damage
    elif o==0:
        print("你拿出了盾牌准备防御")
        boss_damage=int(boss_damage*0.1)
        if draw_frac(10):
            print("反刺！")
            player_damage=boss_damage*0.5
    else:
        print("误操作，全额吸收伤害！")
    
    time.sleep(sleep_time)
    player_life=player_life-boss_damage
    
    print("你对 Boss 的造成的伤害：",player_damage)
    time.sleep(sleep_time)
    if boss_life<=0:
        print("*"*30)
        print("恭喜！你杀死了Boss！")
        break
    print("Boss 剩余血量：",boss_life)

    time.sleep(sleep_time)
    print("受到来自Boss的伤害：",boss_damage)
    time.sleep(sleep_time)
    if player_life<=0:
        print("你死于 Boss 的利爪")
        print("-"*40)
        break
    print("你的剩余血量：",player_life)
    time.sleep(sleep_time_round)   
    r = r + 1  

       