import matplotlib.pyplot as plt

x_values = list(range(1,1000))
y_values = [x**2 for x in x_values]

# s 表示线的粗细, edgecolor='none'表示删除数据点的轮廓, c = 'red' 修改线条颜色
# plt.scatter(x_values, y_values, s = 40)
# plt.scatter(x_values, y_values, edgecolor='none', s = 40)
# plt.scatter(x_values, y_values, c = 'red', edgecolor='none', s = 40)

# 颜色值还可以用RGB表示，值越接近0，指定的颜色越深，越接近1指定的颜色越浅
# plt.scatter(x_values, y_values, c = (0, 0, 0.8), edgecolor='none', s = 40)

# 将参数c设置成y值列表，用参数cmap告诉pyplot使用哪个颜色映射
# 这些代码将y值较小的点显示为浅蓝色，将 y值较大的设置为深蓝色
plt.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Blues,  edgecolor='none', s = 40)

# 设置图表标签，坐标轴标签
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square on Value ", fontsize = 14)

# 设置标记刻度的大小
plt.tick_params(axis = 'both', which = 'major', labelsize = 14)

# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

# 展示
# plt.show()

# 自动保存图片,参数1：文件名（下面这么写是保存在当前文件的目录下），参数2：将图表多余的空白区域裁剪掉
plt.savefig('squares_plot.png', bbox_inches = 'tight')