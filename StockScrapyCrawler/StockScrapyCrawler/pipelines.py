# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from StockScrapyCrawler import settings
import pymysql
import math
import pandas as pd
from datetime import datetime
from dateutil import relativedelta


class StockscrapycrawlerPipeline:
    def __init__(self):
        # 傳入在settings.py檔案中所設定的MySQL資料庫連線資訊，來建立連線物件
        self.connect = pymysql.connect(
            host=settings.MYSQL_HOST,
            db=settings.MYSQL_DATABASE,
            user=settings.MYSQL_USERNAME,
            passwd=settings.MYSQL_PASSWORD,
            charset='utf8'
        )
        # 利用cursor()方法(Method)建立cursor物件，以便能夠對資料庫進行操作
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):

        def diff_month(d1, d2):
            return abs(d1.year - d2.year) * 12 + abs(d1.month - d2.month)

        x = pd.to_datetime("2010-03-31")
        monthdiff = diff_month(datetime(2010, 3, 31), datetime.today())
        # 依照每間公司最後一季的月份與日期

        try:
            for m in range(0, math.ceil(monthdiff / 3)):
                res = x + relativedelta.relativedelta(months=+3 * m)
                # 2017-04-01年後的資料長相不同
                self.cursor.execute(
                    "INSERT INTO `stock`.`StockETLLog`(`stock_id`,`TransactionDate`,`StockType`,`Status`) VALUES (%s, %s, %s,%s)",
                    (item['stock_id'], res.date(), item['type'], item['verify']),
                )
        except Exception as e:
            self.logger.error(item, e)
        finally:
            print('sucess')

        return item


    def close_spider(self, spider):
        self.connect.commit()
        self.connect.close()
