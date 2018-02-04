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

import csv

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

# get_text()

# get_csv()

# 读取pdf
# pdfFile = urlopen("http://pythonscraping.com/pages/warandpeace/chapter1.pdf")
# outputString = read_pdf(pdfFile)
# print(outputString)
# pdfFile.close()

# 读取 docx
read_docx()
