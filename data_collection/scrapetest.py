from urllib.request import urlopen
from bs4 import BeautifulSoup

try:
    # url 可能返回为空，或者 url 输入错误
    html = urlopen("http://pythonscraping.com/pages/page1.html")
except Exception as e:
    print(e)
else:
    if html is None:
        print("URL is not found")
    else:
        # BeautifulSoup 需要添加第二参数：'lxml'，不然会有警告, 参数二是个库，需要安装
        bsObj = BeautifulSoup(html.read(),'lxml')
        # print(html.read())
        print(bsObj.h1)

