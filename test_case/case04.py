# 题目：输入某年某月某日，判断这一天是这一年的第几天？
# 程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天：

import time

while 1:
    try:
        a=input('请输入日期格式为 yyyy-mm-dd:')
        b=time.strptime(a,'%Y-%m-%d') # 按输入格式转化成时间格式 local变量
    except ValueError:
        print('请输入正确的日期格式！')
    else:
        b=time.strptime(a,'%Y-%m-%d') # 按输入格式转化成时间格式 global变量
        dd=time.strftime('%j',b)  # 十进制表示的每年的第几天
        yy=time.strftime('%Y',b)  # 带世纪部分的十制年份
        print("输入的日期是 %s 年的第 %s 天" %(yy,dd))
        break