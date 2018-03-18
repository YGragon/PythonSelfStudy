# 题目：输入3个数a,b,c，按大小顺序输出。

#!/usr/bin/python
# -*- coding: UTF-8 -*-

a=[]
for i in range(3):
    a.append(input("请输入一个数字："))
a.sort()
print(a)