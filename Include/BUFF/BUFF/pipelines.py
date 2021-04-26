# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# from BUFF.buff_item_info_storage import Buff_info_storage  as buff_store    引用的是实例
from BUFF.mysql_processor import processor  # 引用的是实例


class BuffPipeline(object):
    def process_item(self, item, spider):
        processor.open_mysql()
        processor.cursor.execute('select * from {table_name} where Item_id={item_id} and  \
                                 {column_date} != NULL '
            .format(
            table_name=processor.table_name,
            item_id=item['buff_id'],
            column_date=processor.return_time()[1]

        ))
        if processor.cursor.fetchall():
            return item
        else:
            if eval(item['price']) == 0:
                item['price'] = '暂无在售'
            else:
                item['price'] = '￥' + item['price']
            if processor.check_whether_the_first_time() == 0:
                processor.cursor.execute("INSERT INTO {table_name} (Item_id,{column_date}) values ({item_id}, \
                                         '{item_price}') \
                                                                    ".format(table_name=processor.return_time()[0],
                                                                             column_date=processor.return_time()[1],
                                                                             item_price=item['price'],
                                                                             item_id=item['buff_id']
                                                                             ))
            else:
                print("UPDATE  {table_name} SET {column_date}='{item_price}' \
                                          where Item_id = {item_id}; \
                                                                    ".format(table_name=processor.return_time()[0],
                                                                             column_date=processor.return_time()[1],
                                                                             item_price=item['price'],
                                                                             item_id=item['buff_id']
                                                                             ))
                processor.cursor.execute("UPDATE  {table_name} SET {column_date}='{item_price}' \
                                          where Item_id = {item_id}; \
                                                                    ".format(table_name=processor.return_time()[0],
                                                                             column_date=processor.return_time()[1],
                                                                             item_price=item['price'],
                                                                             item_id=item['buff_id']
                                                                             ))

            processor.conn.commit()
            return item
