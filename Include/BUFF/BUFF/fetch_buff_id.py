#  获取整个mysql数据库中所有商品id，利用生成器形式

import pymysql


# generator
class BUFF_ITEM_FETCHER():
    def __init__(self):
        self.conn = pymysql.Connect(host='localhost', port=3306, user='root',
                                    password='Lkw1998517!', database='BUFF',
                                    charset='utf8')
        self.cursor = self.conn.cursor()
        self.cursor.execute('select Item_id from buff_item_list;')

    def fetch(self):
        yield self.cursor.fetchone()[0]


fetcher = BUFF_ITEM_FETCHER()
