def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

a = histogram("Hello world")
print(a)

# 上面的代码统计了字母的出现频率，但要统计的句子要提前写入程序（第10行）
# 能否实现这样的效果：程序运行后请用户输入英文单词或句子，再统计字母频率
# 提示：用 python 自带的 input 