#  mysql数据操作模块

from functools import wraps

import logging
import pymysql
import time

logging.basicConfig(level=logging.INFO,
                    # format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s', #返回值：Thu, 26 May 2016 15:09:31 t11.py[line:92] INFO
                    format='[%(asctime)s %(filename)s %(levelname)s ]  %(message)s',
                    # datefmt='%a, %d %b %Y %H:%M:%S',
                    # datefmt='%Y/%m/%d %I:%M:%S %p', #返回2016/05/26 03:12:56 PM
                    datefmt='%Y-%m-%d %H:%M:%S',  # 返回2016/05/26 03:12:56 PM
                    # filename=logfile
                    # filemode='a' #默认为a
                    )
logger = logging.getLogger(__name__)


class mysql_process(object):

    def __init__(self):
        self.local_time = time.strftime('%m_%d', time.localtime())
        self.table_name = ''

    def open_mysql(self):
        self.conn = pymysql.Connect(host='localhost', port=3306, user='root', password='Lkw1998517!',
                                    database='BUFF', charset='utf8')
        self.cursor = self.conn.cursor()

    def check_table(self):  # 检测当前月份的表格有没有创建
        self.cursor.execute('show tables; ')
        tables = self.cursor.fetchall()
        # print(tables)
        a = (('BUFF_PRICE_' + time.strftime('%Y_%m', time.localtime())).lower(),)
        if a in tables:
            logger.info('table has been created')
            self.table_name = 'buff_price_' + time.strftime('%Y_%m', time.localtime())
        else:
            logger.info('table has not been created')
            self.table_name = 'buff_price_' + time.strftime('%Y_%m', time.localtime())
            self.cursor.execute('create table ' + self.table_name + ' ( \
                                                            `Item_id` int  primary key \
                                                             ); ')
            logger.info('table has been created automatically')

    def check_column(self):  # 检测当前日期的列有没有创建
        self.cursor.execute('desc ' + 'buff_price_' + time.strftime('%Y_%m', time.localtime()))
        columns = self.cursor.fetchall()
        # print(columns)
        date = [item[0] for item in columns]
        if self.local_time in date:
            logger.info('column has been created')
        else:
            logger.info('column has not been created')
            self.cursor.execute('alter table {table_name} add {local_time} varchar(128)'.format(
                table_name=self.table_name,
                local_time=self.local_time
            )
            )
            logger.info('column has been created automatically')

    def return_time(self):  # 返回今天所在的数据表和属性
        table_name = ('buff_price_' + time.strftime('%Y_%m', time.localtime()))
        column_name = time.strftime('%m_%d', time.localtime())
        return [table_name, column_name]

    def check_whether_the_first_time(self):  # 检测是否为第一次在表中插入数据，如果是第一次，在pipeline中使用insert语句； *\
        self.cursor.execute(
            'desc ' + 'buff_price_' + time.strftime('%Y_%m', time.localtime()))  # 如果不是，在pipeline中使用update
        columns_number = len(self.cursor.fetchall())
        # print(columns_number)
        if columns_number == 2:  # 判断是否为第一次在表中插入数据，如果是第一次，返回0，如果不是，返回1
            # 第一次运行时已经有两列：BUFF_ID和当日的日期
            # print(0)
            return 0
        if columns_number > 2:
            # print(1)
            return 1

    def close_procedure(self):
        self.cursor.close()
        self.conn.close()
        logger.info('cursor and conn close')


"""    def check_time(self):
        self.today = 1593792000 # 00:00:00 7/4/2020
        while now_time <today:
            time.sleep(3600*6)
        else:
            today += 86400"""

processor = mysql_process()
