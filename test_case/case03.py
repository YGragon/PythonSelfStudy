#!/usr/bin/python
# coding=utf-8

# 题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
# 程序分析：
# 假设该数为 x。
# 1、则：x + 100 = n^2, x + 100 + 168 = m^2
# 2、n^2 + 168 = m^2 ，则 n、m 都小于 168，而且 n 应小于 m
for m in range(168):
    for n in range(m):
        if m**2 - n**2 == 168:
            x = n**2 - 100
            print(x)