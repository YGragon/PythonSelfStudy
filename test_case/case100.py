# 题目：列表转换为字典。
#!/usr/bin/python
# -*- coding: UTF-8 -*-

i = ['a', 'b']
l = [1, 2]
print(dict([i,l]))

#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# 从列表创建字典
i = ['a','b','c']
l = [1,2,3]
#  zip() 函数用于将可迭代的对象作为参数,
# 将对象中对应的元素打包成一个个元组,然后返回由这些元组组成的列表
b=dict(zip(i,l))
print(b)