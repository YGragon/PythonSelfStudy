# 题目：字符串日期转换为易读的日期格式。
#!/usr/bin/python
# -*- coding: UTF-8 -*-

from dateutil import parser
import time
time_str = time.ctime(time.time())
print(time_str)
dt = parser.parse(time_str)
print(dt)