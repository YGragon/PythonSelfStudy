# 题目：练习函数调用。
#!/usr/bin/python
# -*- coding: UTF-8 -*-

def hello_world():
    print('hello world')

def three_hellos():
    for i in range(3):
        hello_world()

three_hellos()