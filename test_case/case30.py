# 题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
#!/usr/bin/env python3

str = input("请输入5位数: ")

if str[0] == str[-1] and str[1] == str[-2]:
    print( "%s 是一个回文数!" % str)
else:
    print( "%s 不是一个回文数!" % str)