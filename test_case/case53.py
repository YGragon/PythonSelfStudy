# 题目：学习使用按位异或 ^ 。
# 程序分析：0^0=0; 0^1=1; 1^0=1; 1^1
#!/usr/bin/python
# -*- coding: UTF-8 -*-
a = 0
b = a ^ 3
print('a ^ b is %d' % b)
b ^= 1
print('a ^ b is %d' % b)