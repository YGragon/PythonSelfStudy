# 两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵：
#!/usr/bin/python
# -*- coding: UTF-8 -*-

# X = [[12,7,3],
#     [4 ,5,6],
#     [7 ,8,9]]

# Y = [[5,8,1],
#     [6,7,3],
#     [4,5,9]]

# result = [[0,0,0],
#          [0,0,0],
#          [0,0,0]]

# # 迭代输出行
# for i in range(len(X)):
#    # 迭代输出列
#    for j in range(len(X[0])):
#        result[i][j] = X[i][j] + Y[i][j]

# for r in result:
#    print(r)
#!/usr/bin/python
# coding:utf-8

# 第二种方法 使用 numpy
# import numpy as np

# x = np.array( [[12,7,3],
#                [4 ,5,6],
#                [7 ,8,9]])
# y = np.array( [[5,8,1],
#                [6,7,3],
#                [4,5,9]])

# z = x+y
# print(z)

# 第三种
import random

data1 = [[random.randint(1,100) for i in range(3)] for j in range(3)]
data2 = [[random.randint(1,100) for i in range(3)] for j in range(3)]

print("data1:",data1)
print("data2:",data2)

data3 = data1[:]

for i in range(len(data1)):
    for j in range(len(data1[i])):
        data3[i][j] = data1[i][j] + data2[i][j]
print("data3:",data3)