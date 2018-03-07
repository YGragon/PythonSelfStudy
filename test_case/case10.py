# 题目：暂停一秒输出，并格式化当前时间。
import time,datetime
print("暂停一秒输出，并格式化当前时间")
time.sleep(1)
TIME = datetime.datetime.now()
print(TIME.strftime("%Y.%m.%d %H-%M-%S"))