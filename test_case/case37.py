# 题目：对10个数进行排序。
# 程序分析：可以利用选择法，即从后9个比较过程中，选择一个最小的与第一个元素交换，下次类推，即用第二个元素与后8个进行比较，并进行交换。
#!/usr/bin/python
# -*- coding: UTF-8 -*-

print('请输入10个数字:\n')
a=[]
for n in range(10):
    a.append(int(input('输入一个数字:\n')))
a.sort()
print(a)