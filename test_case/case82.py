# 题目：八进制转换为十进制
#!/usr/bin/python
# -*- coding: UTF-8 -*-
# ord()函数是chr()函数（对于8位的ASCII字符串）或unichr()函数（对于Unicode对象）的配对函数，
# 它以一个字符（长度为1的字符串）作为参数，返回对应的ASCII数值
if __name__ == '__main__':
    n = 0
    p = input('输入十进制的数转为八进制的数:\n')
    for i in range(len(p)):
        n = n * 8 + ord(p[i]) - ord('0')
    print(n)
