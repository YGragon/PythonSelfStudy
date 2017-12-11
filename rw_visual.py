import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 只要程序属于活动状态，就不断的模拟随机漫步
while True:
    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    # 增加点数,运行时间也会变长
    # rw = RandomWalk(50000)
    rw = RandomWalk()
    rw.fill_walk()

    # 设置窗口的尺寸
    # plt.figure(figsize = (10, 6))

    # 传递屏幕分辨率
    plt.figure(dpi = 128, figsize = (10, 6))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c = point_numbers, cmap = plt.cm.Blues, edgecolor='none', s = 1)

    # 突出起点和终点
    plt.scatter(0, 0, c = 'green', edgecolor='none', s = 100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c = 'red', edgecolor='none', s = 100)

    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)


    plt.show()

    # plt.savefig('rw_visual.png', bbox_inches = 'tight')

    # 关闭matplotlib时会提示是否要再模拟一次，输入y可以再运行一次，输入n则退出
    keep_running = input("Make another walk ? (y/n): ")
    if keep_running == 'n':
        break

