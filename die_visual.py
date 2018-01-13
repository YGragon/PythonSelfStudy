import pygal

from die import Die
# 创建一个D6
die = Die(6)

# 掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# 分析结果
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling on D6 1000 times."
# hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_labels = list(range(1,7))
hist.x_title = "Results"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
# 将图表渲染为一个SVG文件，这种文件的扩展名必须为svg
# pygal 1.7.0 版本会报错 ValueError: Invalid PI name 'b'xml''，解决办法是卸载该版本后安装新的版本
    # pip uninstall pygal
    # 输入 y 确认卸载
    # pip install --user pygal==2.4
hist.render_to_file('die_visual.svg')

print(frequencies)