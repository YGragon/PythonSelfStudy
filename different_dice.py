import pygal
from die import Die

# 创建一个D6骰子和D10
die_1 = Die(6)
die_2 = Die(10)

# 掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling on D6 and D10 50000 times."
# 最小总数
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '10', '11', '12', '13', '14', '15', '16']
hist.x_title = "Results"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)
# 将图表渲染为一个SVG文件，这种文件的扩展名必须为svg
hist.render_to_file('die_visual.svg')

print(frequencies)
