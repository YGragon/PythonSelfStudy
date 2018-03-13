# 题目：按相反的顺序输出列表的值。
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

list_ = ['a', 'b', 'c', 'd']
if len(list_) <= 1:
    print("集合长度为1：",list_[0])
else:
    list_.reverse()
    print("集合长度为",len(list_),"：",list_)
