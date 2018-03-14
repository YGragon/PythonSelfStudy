# 题目：画图，学用circle画圆形。
#!/usr/bin/python
# -*- coding: UTF-8 -*-
#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import turtle
turtle.title("画圆")
turtle.setup(800,600,0,0)
pen=turtle.Turtle()
pen.color("yellow")
pen.width(5)
pen.shape("turtle")
pen.speed(1)
pen.circle(100)
time.sleep(5)


# import numpy as np
# import matplotlib.pyplot as plt

# x = y = np.arange(-11, 11, 0.1)
# x, y = np.meshgrid(x,y)
# #圆心为（0，0），半径为1-10
# for i in range(1,11):
#    plt.contour(x, y, x**2 + y**2, [i**2])
#    #避免因比例而压缩为椭圆
#    plt.axis('scaled')
# plt.show()