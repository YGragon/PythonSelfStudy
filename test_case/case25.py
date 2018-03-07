# 题目：求1+2!+3!+...+20!的和。
# 程序分析：此程序只是把累加变成了累乘。

#!/usr/bin/python
# -*- coding: UTF-8 -*-

n = 0
s = 0
t = 1
for n in range(1,21):
    t *= n # 累积
    s += t # 累加
print('1! + 2! + 3! + ... + 20! = %d' % s)