# -*- coding: utf-8 -*-

import scrapy
import pymysql
import time
import sys
from BUFF.mysql_processor import logger  # 引用的是实例，来自于check_time模块中的日志对象实例，以此保证输出日志格式相同
from BUFF.fetch_buff_id import fetcher  # 引用的是实例,一次读取一个buff_id
from BUFF.mysql_processor import processor  # 引用的是实例，进行mysql数据库的各种检测
from BUFF.items import BuffItem

import re

# processor.check_time()
processor.open_mysql()
processor.check_table()
processor.check_whether_the_first_time()
processor.check_column()
processor.close_procedure()


class BuffItemSpider(scrapy.Spider):
    name = 'BUFF_ITEM'
    allowed_domains = ['buff.163.com']
    start_urls = ['https://buff.163.com/market/goods?goods_id=1']

    def parse(self, response):
        try:
            self.item_id = str(next(fetcher.fetch()))  # 去除重复的1
            buff_item = BuffItem()
            raw_material = response.xpath('//*[@id="market_min_price_pat"]/text()').extract()[0]
            re_formula = re.compile(r'"custom-currency" data-price=\S+' + '\'?')
            buff_item['price'] = (re.findall(re_formula, raw_material)[0].split('\"'))[3]
            buff_item['buff_id'] = self.item_id
            yield buff_item
            self.item_id = str(next(fetcher.fetch()))
            yield scrapy.Request('https://buff.163.com/market/goods?goods_id=' + self.item_id, callback=self.parse_next)
        except StopIteration as iter_err:
            logger.info('the url iter has completed')
            processor.close_procedure()

    def parse_next(self, response):
        try:
            buff_item = BuffItem()
            '''buff_item['price'] = response.xpath('/html/body/div[@class="market-list"]/div[@class="l_Layout"] \
                                                /div[@class="relative-goods"]/a[@class="i_Btn i_Btn_trans_bu \
                                                le active"]/text()'
                                               ).extract()'''
            raw_material = response.xpath('//*[@id="market_min_price_pat"]/text()').extract()[0]
            re_formula = re.compile(r'"custom-currency" data-price=\S+' + '\'?')
            buff_item['price'] = (re.findall(re_formula, raw_material)[0].split('\"'))[3]
            buff_item['buff_id'] = self.item_id
            yield buff_item
            self.item_id = str(next(fetcher.fetch()))
            yield scrapy.Request('https://buff.163.com/market/goods?goods_id=' + self.item_id, callback=self.parse_next)
        except StopIteration as iter_err:
            logger.info('the url iter has completed')
            processor.close_procedure()
