 # -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 13:08:28 2023

@author: Administrator
"""


def Euler(n):
    lis = [True] * (n+1)  # 用于筛选记录合数
    prime_numbers = []  # 存质数
    for i in range(2, n + 1): #范围2~n
        if lis[i]:  # 如果没有被筛选就加到prime_numbers
            prime_numbers.append(i)
        for prime in prime_numbers:
            if i * prime > n:  # 保证小于n，不能超出范围
                break
            lis[i * prime] = False  # 记录合数
            if i % prime == 0:  # 关键步骤，确保每个合数只被筛选一次
                break
    return prime_numbers
n=int(1e4)
a=Euler(n)
print(a)

def Eratosthenes(n):
    lis = [True] * (n+1)  # 用于筛选记录合数
    prime_numbers = []  # 存质数
    for i in range(2, n + 1): #范围2~n
        if lis[i]:  # 如果没有被筛选就加到prime_numbers
            prime_numbers.append(i)
        for k in range(2,n):
            if k * i > n:  # 保证小于n，不能超出范围
                break
            lis[i * k] = False  # 记录合数
    return prime_numbers
n=int(18)
a=Eratosthenes(n)
print(a)