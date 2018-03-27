# 题目：读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊。
#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    n = 1
    while n <= 7:
        a = int(input('input a number:\n'))
        while a < 1 or a > 50:
            # 重新输入
            a = int(input('input a number:\n'))
        print(a * '*')
        n += 1