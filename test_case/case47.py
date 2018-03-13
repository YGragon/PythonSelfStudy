# 题目：两个变量值互换
#!/usr/bin/python
# -*- coding: UTF-8 -*-

def exchange(a,b):
    a,b = b,a
    return (a,b)


x = 10
y = 20
print('原来的 x = %d,原来的 y = %d' % (x,y))
x,y = exchange(x,y)
print('交换后的 x = %d,交换后的 y = %d' % (x,y))