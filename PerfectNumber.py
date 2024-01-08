"""
2021-09-22
高阳
将真因数表示为质因数的乘积再求和，判断是否为完美数。

"""
import sys
print(sys.version)
print(sys.executable)

import numpy as np
import itertools

def is_prime(n):
    r = True
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            r = False
    return r

def find_primes(n):
    res = dict()
    for i in range(2, n+1):
        if is_prime(i):
            res[i] = 0
    return res

def find_power(n, m):
    if m == 1:
        return None
    res = 0
    while n % m == 0:
        res += 1
        n /= m

    return res

def find_nonzeropower(d):
    res = dict()
    for key in d:
        if d[key] > 0:
            res[key] = d[key]
    return res

def sum_factors(d):
    res = 0
    factors = list(d.keys())
    powers_full = list(d.values())
    p = []
    
    for e in powers_full:
        p.append(np.arange(e+1))
        
    for powers in itertools.product(*p):
        f = 1
        for i,power in enumerate(powers):
            f *= factors[i] ** power
        res += f
        
    return res

# Main
n = 10000
primes = find_primes(n)

for i in range(2,n+1):
    
    if i % 5000 == 0:
        print("i =",i)
        
    for key in primes:
        if key > i: 
            break 
        primes[key] = find_power(i,key)

    non_zero_primes = find_nonzeropower(primes)
    
    s = sum_factors(non_zero_primes)
    
    if s - i == i:
        print(i,"is a perfect number.")
