# 题目：斐波那契数列。
# 程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。

#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 使用递归
def fib_index(n):
    if n <= 0:
        print('请输入大于 0 的数')
    else:
        if n==1 or n==2:
            return 1
        return fib_index(n-1)+fib_index(n-2)


def fib_list(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

# 输出了第10个斐波那契数列
print(fib_index(0))

# 输出前 10 个斐波那契数列
print(fib_list(10))


