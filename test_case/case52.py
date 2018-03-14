# 题目：学习使用按位或 | 。
# 程序分析：0|0=0; 0|1=1; 1|0=1; 1|1=1
#!/usr/bin/python
# -*- coding: UTF-8 -*-

a = 0
b = a | 0
print('a | b is %d' % b)
b |= 7
print('a | b is %d' % b)
