def is_ugly(num):
    if num<=0:
        return False
    elif num<=6:
        return True
    if num%2==0:
        return is_ugly(num/2)
    if num%3==0:
        return is_ugly(num/3)
    if num%5==0:
        return is_ugly(num/5)
    return False

while True:
    try:
        n=int(input("n="))
        print(is_ugly(n))
    except ValueError:
        print("enter a num")
        continue

