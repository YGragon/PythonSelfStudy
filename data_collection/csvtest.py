import csv

from urllib.request import urlopen
from bs4 import BeautifulSoup

def func_csv_test():
    csvFile = open("../files/test.csv", 'w+')
    try:
        writer = csv.writer(csvFile)
        writer.writerow(('number','number plus 2', 'number time 2'))
        for i in range(10):
            writer.writerow((i, i + 2, i * 2))
    finally:
        csvFile.close()

def func_get_wiki_csv():
    html = urlopen("http://en.wikipedia.org/wiki/Comparison_of_text_editors")
    bsObj = BeautifulSoup(html,  "lxml")
    # 主对比表格是当前页面上的第一个表格
    table = bsObj.findAll("table",{"class":"wikitable"})[0]
    rows = table.findAll("tr")

    csvFile = open("../files/editor.csv", 'wt', newline='', encoding='utf-8')
    writer = csv.writer(csvFile)
    try:
        for row in rows:
            csvRow = []
            for cell in row.findAll(['td','th']):
                csvRow.append(cell.get_text())

            writer.writerow(csvRow)
    finally:
        csvFile.close()

func_csv_test()
func_get_wiki_csv()
