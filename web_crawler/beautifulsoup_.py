# -*- coding: utf-8 -*-
# @Time    : 2018/07/12 14:35:02
# @Author  : Izumi Sakai
# @File    : beautifulsoup_.py
# @Software: PyCharm

from bs4 import BeautifulSoup
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc,'lxml')
#格式化输出
#print(soup.prettify())
# print(soup.title.string)
# print(soup.findAll('a'))
print(soup.findAll('a'))