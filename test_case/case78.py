# 题目：找到年龄最大的人，并输出。请找出程序中有什么问题。
#!/usr/bin/python
# -*- coding: UTF-8 -*-

# if __name__ == '__main__':
#     person = {"li":18,"wang":50,"zhang":20,"sun":22}
#     m = 'li'
#     for key in person.keys():
#         if person[m] < person[key]:
#             m = key

#     print('%s,%d' % (m,person[m]))

# 不太好的地方是需要知道字典中的第一个内容

# 改进法
if __name__ == '__main__':
    person = {"li":18,"wang":50,"zhang":20,"sun":22}
    max_age = 0
    for key,value in person.items():
        if value > max_age:
            max_age = value
            name = key

    print('%s,%d' % (name,max_age))