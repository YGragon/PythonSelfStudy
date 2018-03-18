# 题目：有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a = [1, 2, 3, 4, 5]    # 测试列表
m = 2                  # 设置向后移动 3 位
for i in range(m):
    # 出栈后插入第一个位置
    a.insert(0, a.pop())
print(a)