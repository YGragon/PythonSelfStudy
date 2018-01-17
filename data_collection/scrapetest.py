from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError, URLError
# 导入正则表达式
import re

def getTitle(url):
    """获取标题"""
    try:
        # url 可能返回为空，或者 url 输入错误
        html = urlopen(url)
    except (HTTPError, URLError) as e:
        return None
    try:
        # BeautifulSoup 需要添加第二参数：'lxml'，不然会有警告, 参数二是个库，需要安装
        bsObj = BeautifulSoup(html.read(),'lxml')
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title

def get_person_name(url):
    """获取绿色的人名"""
    try:
        # url 可能返回为空，或者 url 输入错误
        html = urlopen(url)
    except (HTTPError, URLError) as e:
        return None
    try:
        # BeautifulSoup 需要添加第二参数：'lxml'，不然会有警告, 参数二是个库，需要安装
        bsObj = BeautifulSoup(html,'lxml')
        nameList = bsObj.findAll("span",{"class":"green"})
    except AttributeError as e:
        return None
    return nameList

def get_images(url):
    """获取所有符合格式的图片"""
    try:
        # url 可能返回为空，或者 url 输入错误
        html = urlopen(url)
    except (HTTPError, URLError) as e:
        return None
    try:
        # BeautifulSoup 需要添加第二参数：'lxml'，不然会有警告, 参数二是个库，需要安装
        bsObj = BeautifulSoup(html,'lxml')
        imgList = bsObj.findAll("img",{"src":re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
    except AttributeError as e:
        return None
    return imgList



title = getTitle("http://pythonscraping.com/pages/page1.html")
if title == None:
    print("Title could not be found")
else:
    print(title)

nameList = get_person_name("http://www.pythonscraping.com/pages/warandpeace.html")
if nameList == None:
    print("nameList could not be found")
else:
    for name in nameList:
        print(name.get_text())

imgList = get_images("http://www.pythonscraping.com/pages/page3.html")
if imgList == None:
    print("imgList could not be found")
else:
    for img in imgList:
        print(img["src"])
