import scrapy
import bs4
import pandas as pd
import json

#this for ETLLog
class FinmindapiSpider(scrapy.Spider):
    name = 'finmindapi'
    allowed_domains = ['https://api.finmindtrade.com']
    start_urls = ['https://api.finmindtrade.com/api/v4/data?dataset=TaiwanStockInfo']

    def parse(self, response):
        dataList = json.loads(response.text)
        dataList = pd.DataFrame(dataList["data"])
        dataList['verify'] = False  # for verify
        type = ['ETF', '指數投資證券(ETN)', '上櫃指數股票型基金(ETF)', '存託憑證']
        for i in dataList[['industry_category', 'stock_id', 'type', 'verify']].values.tolist():
            StockscrapycrawlerItem = {
                "industry_category": i[0],
                "stock_id": i[1],
                "type": i[2],
                "verify": i[3]
            }
            yield StockscrapycrawlerItem

        # print(Companylist[:5])
