import csv

from matplotlib import pyplot as plt
# 从文件中获取最高气温
filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    # 返回文件的下一行
    header_row = next(reader)

    highs = []
    for row in reader:
        high = int(row[1])
        highs.append(high)

    print(highs)

    # 打印头文件及其位置
    # for index, colume_header in enumerate(header_row):
    #     print(index, colume_header)

    fig = plt.figure(dpi = 128, figsize = (10, 6))
    plt.plot(highs, c = 'red')

    # 设置图表标签，坐标轴标签
    plt.title("Daily high temperature, July 2014", fontsize = 24)
    plt.xlabel('', fontsize = 16)
    plt.ylabel("Temperature(F)", fontsize = 16)

    # 设置标记刻度的大小
    plt.tick_params(axis = 'both', which = 'major', labelsize = 16)

    plt.show()
