#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 09:38:56 2021

@author: Yang
"""
############################

import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = ["SimHei"]

x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 7, 25, 11, 8, 10, 16]

# 画出折线图，同时用 marker 标注出每个数据点
plt.figure()
plt.plot(x, y, color="yellow", linewidth = 2,
         marker = "o", markerfacecolor = "gray", markersize = 8)
plt.title("折线图示例")
plt.xlabel("序号")
plt.ylabel("数量")
plt.show()


############################

import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = ["SimHei"]

x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 7, 25, 11, 8, 10, 16]

# 绘制散点图
plt.figure()
plt.scatter(x, y, color = "red")
plt.title("散点图示例")
plt.xlabel("序号")
plt.ylabel("数量")
plt.show()


############################

import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = ["SimHei"]

x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 7, 25, 11, 8, 10, 16]

# 绘制柱状图
plt.figure()
plt.bar(x, y, color = "blue")
plt.title("柱状图示例")
plt.xlabel("序号")
plt.ylabel("数量")
plt.show()


############################

import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = ["SimHei"]

# 绘制饼图
plt.figure()
labels = ["境外输入","河北","黑龙江","北京"]
nums = [15,90,23,2]
plt.pie(nums, labels = labels, startangle = 50)
plt.title("2021-1-15 新冠肺炎确诊病例来源")
plt.xlabel("序号")
plt.ylabel("数量")
plt.show()


