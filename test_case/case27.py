# 题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
#!/usr/bin/env python3

S = input('Input a string:')
L = list(S)
L.reverse()
for i in range(len(L)):
    print(L[i])