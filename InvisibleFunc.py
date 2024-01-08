import functools
a = [(lambda x: x*x)(x) for x in range(10)]
print(a)

l = [(1, 20), (3, 0), (9, 10), (2, -1)]
l.sort(key=lambda x: x[1])
print(l)

b = [1, 2, 3, 4, 5]
n = map(lambda x: x**2, b)
print(list(n))

c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = filter(lambda x: x % 3 == 1, c)
print(list(n))

d = [1, 2, 3, 4, 5]
s1 = functools.reduce(lambda x, y: x*y, d)
s2 = functools.reduce(lambda x, y: x+y, d)
print(s1, s2, sep="\n")
