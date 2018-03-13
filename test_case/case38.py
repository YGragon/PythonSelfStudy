# 题目：求一个3*3矩阵主对角线元素之和。
# 程序分析：利用双重for循环控制输入二维数组，再将a[i][i]累加后输出
# coding: utf-8
"""
    1  2  3
    4  5  6
    7  8  9
"""
a,b,c = [],[],[]
for i in range(3):
    a.append(int(input('Enter a number:')))

for i in range(3):
    b.append(int(input('Enter a number:')))

for i in range(3):
    c.append(int(input('Enter a number:')))

matrix = [a, b ,c ]
sum_ = 0
for i in range(0, 3):
    sum_ += matrix[i][i]
print(sum_)

# 第二种解法
# A = {}
# for i in range(3):
#     for j in range(3):
#         A[i,j] = int(input('Enter a number:'))
# diag = []
# for m in A.keys():
#     # 索引相同
#     if m[0] == m[1]:
#         diag.append(A[m])
# print(sum(diag))