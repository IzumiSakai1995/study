# -*- coding: utf-8 -*-
# @Time    : 2018/07/12 14:54:54
# @Author  : Izumi Sakai
# @File    : Demo.py
# @Software: PyCharm

import requests

headers = {
    'User-Agent':'"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)"'
}
url = 'http://maoyan.com/board/4'
response = requests.get(url,headers=headers)
with open('demo_log.txt','a',encoding='utf-8') as f:
    f.write(response.text)
    f.close()
