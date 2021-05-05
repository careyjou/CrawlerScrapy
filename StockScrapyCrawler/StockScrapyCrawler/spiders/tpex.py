import scrapy


class TpexSpider(scrapy.Spider):
    name = 'tpex'
    allowed_domains = ['www.tpex.org.tw/']
    start_urls = ['https://www.tpex.org.tw/web/stock/aftertrading/peratio_analysis/pera_result.php?l=zh-tw&o=htm&d=110/05/04&c=&s=0,asc']

    def parse(self, response):
        pass
