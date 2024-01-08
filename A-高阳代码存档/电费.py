x = float(input())

if x<=200:
    y = 0.66*x
else:
    if x<=400:
        y = 0.71*(x-200) + 0.66*200
    else:
        y = 0.96*(x-400) + 0.71*(400-200) + 0.66*200
    
print(y)