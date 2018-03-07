# 题目：判断101-200之间有多少个素数，并输出所有素数。
# 程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。

#!/usr/bin/python
# -*- coding: UTF-8 -*-
l = []
for i in range(101,200):
    for j in range(2,i-1):
        if i%j ==0:
            break
    else:
        l.append(i)

print(l)

print("总数为：%d" % len(l))