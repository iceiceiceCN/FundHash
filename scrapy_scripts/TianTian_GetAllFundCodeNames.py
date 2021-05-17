#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import requests
import re
from getYAML import *
filename = os.path.basename(__file__).split('.')[0]
yaml_data = getyaml(filename)
# 头部信息
headers = {
    'Host':yaml_data['TianTian_GetAllFundCodeNames']['Host'],
    'Accept-Language':"zh-CN,zh;q=0.9",
    'Accept-Encoding':"gzip, deflate",
    'Content-Type':"application/x-www-form-urlencoded",
    'Connection':"keep-alive",
    'Referer':yaml_data['TianTian_GetAllFundCodeNames']['Referer'],
    'Cookie':yaml_data['TianTian_GetAllFundCodeNames']['cookies'],
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
}

responese = requests.get(url=yaml_data['TianTian_GetAllFundCodeNames']['url'],headers=headers)
W = open(r'D:\基金数据\最新数据\fundcode_4_21.txt','w')
W.write(responese.text)

# 下一步转 DA_scripts\处理基金代码及名称.ipynb