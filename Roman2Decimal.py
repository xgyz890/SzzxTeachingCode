# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 15:56:34 2022

@author: HiteVision
"""

s=input("roman:").upper()
sum=0 
convert={'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1} 

       
i = 0
num = 0
for i in range(len(s)-1):
    if convert[s[i]] < convert[s[i+1]]:
        sum -= convert[s[i]]
    else:
        sum += convert[s[i]]
sum += convert[s[-1]]

print(sum)
