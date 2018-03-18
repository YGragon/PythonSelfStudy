# 题目：计算循环中最终的值。
#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    for i in range(5):
        n = 0
        if i != 1:
            # i=0，n=1
            n += 1
        if i == 3:
            # i=3，n=3
            n += 1
        if i == 4:
            # i=4，n=4
            n += 1
        if i != 4:
            # i=1，n=2
            n += 1
        if n == 3:
            # i=3，n=3，注意 n=3 输出！！
            print(64 + i)