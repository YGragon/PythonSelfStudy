# 题目：使用lambda来创建匿名函数
#!/usr/bin/python
# -*- coding: UTF-8 -*-

MAXIMUM = lambda x,y :  (x > y) * x + (x < y) * y
MINIMUM = lambda x,y :  (x > y) * y + (x < y) * x

a = 10
b = 20
print('The largar one is %d' % MAXIMUM(a,b))
print('The lower one is %d' % MINIMUM(a,b))