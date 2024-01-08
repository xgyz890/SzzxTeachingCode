# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 11:14:18 2021

@author: gaoyang
"""

import random
import time

class Boss:
    """Defines a boss."""
    def __init__(self,life=300,attack_l=50,attack_h=100):
        self.initlife=life
        self.life=life
        self.attack_l=attack_l
        self.attack_h=attack_h
        
        self.defense_rate=0.2
        self.angry_threshold=0.3
        self.angry_buff=2
        
        self.give_damage=0
        self.receive_damage=0
        
    def attack(self):
        self.give_damage=random.randint(self.attack_l,self.attack_h)
        if self.give_damage>self.attack_l+(0.5*(self.attack_h-self.attack_l)):
            print("Boss喷出了火焰！")
        else:
            print("Boss使用了冲撞。")
            
        if self.life<=int(self.initlife*self.angry_threshold):
            self.give_damage=int(self.give_damage*self.angry_buff)
            print("Boss血量已经低于{:%}，触发怒意攻击加成！".format(self.angry_threshold))
        print("Boss此轮攻击力：{}，目前血量：{}。".format(self.give_damage,self.life))
    
    def defense(self,receive_damage):
        self.receive_damage*=int(1-self.defense_rate)
        
    def settle(self):
        self.life-=self.receive_damage
    
    def show_life(self):
        print("-"*40)
        print("Boss目前的生命值：{}。\n".format(self.life))
        
    def die(self):
        print("Boss: Arrghhh!!")
        
class Player:
    """Defines a player."""
    def __init__(self,life=100,attack_l=20,attack_h=50,money=200):
        self.initlife=life
        self.life=life
        self.attack_l=attack_l
        self.attack_h=attack_h
        
        self.defense_rate=0.8
        self.bounce_rate=0.4
        
        self.receive_damage=0
        self.give_damage=0
        
        self.large_potion=1
        self.lp_vol=50
        self.lp_price=100
        
        self.small_potion=3
        self.sp_vol=20
        self.sp_price=50
        
        self.money=money
    
    def critical(self,n):
        k=random.randint(1,n+1)
        if k==1:
            return True
        else:
            False
    
    def draw(self,n):
        return random.randint(1,n+1)
    
    def choose(self):
        a=int(input("选择对策（0=防御，1=攻击）："))
        if a==1:
            self.attack()
        elif a==0:
            self.defense()
        elif a==2:
            self.heal()
        else:
            print("操作错误。没有拿起盾牌，所以承受了全部伤害！")
        
    def attack(self):
        if self.draw(5)==0:
            print("\"你拔出宝剑向Boss砍去！\"")
        elif self.draw(5) in (1,2):
            print("\"临阵磨枪，不快也光。\"")
        else:
            print("\"十年磨一剑，霜刃未曾试！\"")
        self.give_damage=random.randint(self.attack_l,self.attack_h)
        if self.critical(5):
            print("暴击！")
            self.give_damage*=4
        print("你此轮的攻击力：{}".format(self.give_damage))
            
    def defense(self):
        if self.draw(4)==0:
            print("你拿出盾牌防御。")
        else:
            print("闪！")
        self.receive_damage=int(self.receive_damage*(1-self.defense_rate))
        self.give_damage=0
        if self.critical(10):
            print("反刺！")
            self.give_damage=int(self.receive_damage*self.bounce_rate)
    
    def heal(self):
        print("-"*40)
        print("治疗环节开始。")
        while True:
            if self.large_potion==0 and self.small_potion==0:
                print(">>>已无药水可用。")
                break
            if self.life<=0:
                print(">>>你处于濒死状态！")
            s="背包里有{}瓶大药水，{}瓶小药水。".format(self.large_potion,self.small_potion)
            x=int(input(s+"\n是否使用？（1=使用，0=不使用）"))
            if x==1:
                y=int(input("使用哪种药水？（1=大药水，2=小药水，0=退出）"))
                if y==1:
                    if self.large_potion:
                        self.life+=self.lp_vol
                        print("你的生命值恢复到了：{}".format(self.life))
                        self.large_potion-=1
                    else:
                        print("大药水已经用光..")
                        continue
                elif y==2:
                    if self.small_potion:
                        self.life+=self.sp_vol
                        print("你的生命值恢复到了：{}".format(self.life))
                        self.small_potion-=1
                    else:
                        print("小药水已经用光..")
                        continue
                elif y==0:
                    break
                else:
                    print("请重新输入")
            elif x==0:
                break
        print("治疗环节结束。")
                
    def purchase_potion(self):
        print("-"*40)
        print("购物环节开始。")
        while True:
            if self.money<=0:
                print(">>>金币已经花完。")
                break
            print("（大药水{}金币，小药水{}金币）".format(self.lp_price,self.sp_price))
            s="钱包里有{}金币。".format(self.money)
            x=int(input(s+"\n是否花费金币购买物品？（1=是，0=退出）"))
            if x==1:
                y=int(input("请输入要购买的物品：（1=大药水，2=小药水）"))
                z=int(input("请输入要购买的数量："))
                if z<=0:
                    u=int(input("购买数量不能小于等于 0，是否继续购买？（1=是，0=否）"))
                    if u==1:
                        continue
                    else:
                        break
                if y==2:
                    if self.sp_price*z>self.money:
                        print("金币不够。需要{}，余额{}。".format(self.sp_price*z,self.money))
                        continue
                    else:
                        # 计算购买后的余额
                        self.money=(self.sp_price*z)%self.money
                        self.small_potion+=z
                elif y==1:
                    if self.lp_price*z>self.money:
                        print("金币不够。需要{}，余额{}。".format(self.lp_price*z,self.money))
                        continue
                    else:
                        self.money=(self.lp_price*z)%self.money
                        self.large_potion+=z
            elif x==0:
                break
            else:
                print("输入有误")
                continue
        print("购物环节结束。")
            
    def settle(self):
        self.life-=self.receive_damage
    
    def show_life(self):
        print("-"*40)
        print("你目前的生命值：{}。\n".format(self.life))
        
    def die(self):
        print("*"*40)
        if self.critical(3):
            print("你死于Boss的利爪..")
        else:
            print("你死于Boss吐出的烈焰..")
        
    def triumph(self):
        print("Hooray! You win!")
    
##################################### Main Body Begins Here ##########################################

boss_life=300
player_life=100
i=1

switch=int(input("默认Boss生命值={}点\n默认玩家生命值={}点\n是否要修改？（1=是,0=否）".format(boss_life,player_life)))
if switch:
    s="请设定Boss生命值、玩家生命值（用英文逗号隔开）："
    boss_life,player_life=map(int,input(s).split(","))

boss=Boss(boss_life)
player=Player(player_life)

print("\n设定完毕\nBoss生命值={}点\n玩家生命值={}点".format(boss.life,player.life))
print("\n背包里两种药水：\n大生命药水{}瓶，每瓶回复{}点生命\n小生命药水{}瓶，每瓶回复{}点生命".format(player.large_potion,player.lp_vol,player.small_potion,player.sp_vol))
print("\n游戏开始！\n")

while True:
    print("*"*40)
    print("\nRound {:2d}:\n".format(i))
    
    boss.attack()
    player.receive_damage=boss.give_damage

    player.choose()
    boss.receive_damage=player.give_damage
    
    player.settle()
    boss.settle()
    
    print("\n")
    print("Boss对你造成伤害：{}".format(player.receive_damage))
    time.sleep(0.2)
    print("你的血量：{}".format(player.life))
    time.sleep(0.2)
    print("你对Boss造成伤害：{}".format(boss.receive_damage))
    time.sleep(0.2)
    print("Boss的血量：{}".format(boss.life))
    time.sleep(0.2)

    player.purchase_potion()
    player.heal()
    boss.show_life()
    player.show_life()
    
    i+=1
    
    if player.life<=0:
        player.die()
        break
    if boss.life<=0:
        boss.die()
        player.triumph()
        break
      