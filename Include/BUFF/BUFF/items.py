# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BuffItem(scrapy.Item):
      # define the fields for your item here like:
      # name = scrapy.Field()
      price = scrapy.Field()  # 存储商品价格
      buff_id =scrapy.Field() # BUFF_ID

