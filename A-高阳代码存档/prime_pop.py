
list1 = [x for x in range(2,1000)]
list2 = list1[:]

# for 循环的范围一定要是完整的 list，这里是 list1 的复制品 list2
for n in list2:
	for i in range(2,n):
		if n % i == 0:
			# 从 list1 里面移除 n
			list1.remove(n)
			break
print(list1)

