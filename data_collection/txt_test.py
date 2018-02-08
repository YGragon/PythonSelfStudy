from urllib.request import urlopen
from io import StringIO
# pdf 需要的库
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import open

# docx 需要的库
from zipfile import ZipFile
from io import BytesIO
from bs4 import BeautifulSoup

# 可视化
from author import Author
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

import csv
import json
import requests


def get_text():
    textPage = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1.txt")
    # print(str(textPage.read(),'utf-8'))

def get_csv():
    data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii','ignore')
    dataFile = StringIO(data)
    dictReader = csv.DictReader(dataFile)
    print(dictReader.fieldnames)

    for row in dictReader:
        print(row)

def read_pdf(pdfFile):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)

    process_pdf(rsrcmgr, device, pdfFile)
    device.close()

    content = retstr.getvalue()
    retstr.close()
    return content

def read_docx():
    wordFild = urlopen("http://pythonscraping.com/pages/AWordDocument.docx").read()
    wordFild = BytesIO(wordFild)
    document = ZipFile(wordFild)
    xml_content = document.read('word/document.xml')
    # print(xml_content.decode('utf-8'))

    wordObj = BeautifulSoup(xml_content.decode('utf-8'), 'lxml')
    textStrings = wordObj.findAll("w:t")
    for textElem in textStrings:
        print(textElem.text)


def get_gank_info(ipaddress):
    """
    获取干货集中营的数据
    """
    r = requests.get(ipaddress)
    r = r.json()

    results = r['results']

    authors, names, counts = [], [], []
    # 得到所有作者
    for result in results:
        name = result['who']
        if name != 'None' and name != 'null':
            names.append(name)


    count = {}
    for i in names:
        # 和 get() 方法类似, 如果键不存在于字典中，将会添加键并将值设为默认值
        # key -- 查找的键值。
        # default -- 键不存在时，设置的默认键值
        count[i] = count.setdefault(i,0)
        count[i] += 1
        print(count[i])

    for k, v in count.items():
        authors.append(str(k))
        counts.append(v)
        print(str(k) + ' : ' + str(v))


    my_style = LS('#333366', base_style=LCS)
    chart = pygal.Bar(style=my_style, x_label_rotation=45, show_lengend=False)
    chart.title = "300条干货数据谁提供的最多"
    chart.x_labels = authors

    chart.add('',counts)
    chart.render_to_file('gank_most_post_type.svg')


# get_text()

# get_csv()

# 读取pdf
# pdfFile = urlopen("http://pythonscraping.com/pages/warandpeace/chapter1.pdf")
# outputString = read_pdf(pdfFile)
# print(outputString)
# pdfFile.close()

# 读取 docx
# read_docx()

get_gank_info("http://gank.io/api/data/all/300/1")