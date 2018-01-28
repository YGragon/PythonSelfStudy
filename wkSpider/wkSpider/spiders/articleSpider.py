from scrapy.selector import Selector
from scrapy import Spider
from wkSpider.items import Article

class ArticleSpider(Spider):
    """docstring for ArticleSpider"""
    name = "article"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["http://en.wikipedia.org/wiki/Main_page",
                    "http://en.wikipedia.org/wiki/Python_%28programmin_language%29"]

    def parse(self, response):
        item = Article()
        title = response.xpath('//h1/text()')[0].extract()
        print("Title is : "+title)
        item['title'] = title
        return item
