# -*- coding: utf-8 -*-
# @Time    : 2018/07/16 21:01:14
# @Author  : Izumi Sakai
# @File    : logging_module.py
# @Software: PyCharm
import logging


# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)',
#                     datefmt='%a %d %b %Y %H:%M:%S',
#                     filename='test.log',
#                     filemode='w',
#                     )
#

# 模块级别的函数
logger = logging.getLogger()    # 拿到一个日志对象
fh = logging.FileHandler('./test.log')    # 文件对象

ch = logging.StreamHandler()   # 屏幕对象

formatter = logging.Formatter('%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)')    # 标准流对象
fh.setFormatter(formatter)   # 取来格式

ch.setFormatter(formatter)

logging.debug('1')    # 日志级别上到下递增
logging.info('2')   #级别可修改
logging.warning('3')
logging.error('4')
logging.critical('5')

logger.addHandler(fh)
logger.addHandler(ch)



