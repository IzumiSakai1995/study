# -*- coding: utf-8 -*-
# @Time    : 2018/07/16 21:44:37
# @Author  : Izumi Sakai
# @File    : configureparser_module.py
# @Software: PyCharm

import configparser
config = configparser.ConfigParser()

config["DEFAULT"] = {'ip':"0.0.0.0"}

with open('example.ini','w') as configfile:
    config.write(configfile)