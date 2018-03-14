# 题目：查找字符串。
#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Python find() 方法检测字符串中是否包含子字符串 str
# 如果指定 beg（开始） 和 end（结束） 范围，
# 则检查是否包含在指定范围内，如果包含子字符串返回开始的索引值，否则返回-1
# str.find(str, beg=0, end=len(string))
sStr1 = 'abcdefg'
sStr2 = 'cde'
sStr3 = 'cdeg'
print(sStr1.find(sStr2))
print(sStr1.find(sStr3))