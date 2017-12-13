import csv
from datetime import datetime
from matplotlib import pyplot as plt
# 从文件中获取最高气温和最低气温
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    # 返回文件的下一行
    # header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except Exception as e:
            print(current_date, 'missing data')
        else:
            highs.append(high)
            dates.append(current_date)
            lows.append(low)

    # print(highs)

    # 打印头文件及其位置
    # for index, colume_header in enumerate(header_row):
    #     print(index, colume_header)

    fig = plt.figure(dpi = 128, figsize = (10, 6))
    plt.plot(dates, highs, c = 'red', alpha = 0.5)
    plt.plot(dates, lows, c = 'blue', alpha = 0.5)
    plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)

    # 设置图表标签，坐标轴标签
    plt.title("Daily high and low temperature - 2014\nDeath Valley, CA", fontsize = 20)
    plt.xlabel('', fontsize = 16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature(F)", fontsize = 16)

    # 设置标记刻度的大小
    plt.tick_params(axis = 'both', which = 'major', labelsize = 16)

    plt.show()
