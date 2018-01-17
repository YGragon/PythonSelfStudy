from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError, URLError

def getTitle(url):
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

title = getTitle("http://pythonscraping.com/pages/page1.html")
if title == None:
    print("Title could not be found")
else:
    print(title)
