"""
通过分析得到的Json数据，获取主力持仓数据
"""

import json
import requests
import xlrd
import xlwt
import yaml
from datetime import datetime


# 文件及路径，log目录需要先建好
from getYAML import *
filename = os.path.basename(__file__).split('.')[0]
yaml_data = getyaml(filename)

today = datetime.now()
excelpath = r"D:\基金数据\最新数据\主力持仓数据_{}_{}_{}.xls".format(today.year, today.month, today.day)


# excelpath = r'主力持仓数据.xls'
wtbook = xlwt.Workbook(encoding = 'ascii')
#新增一个sheet工作表
sheet = wtbook.add_sheet('Sheet1',cell_overwrite_ok=True)
#写入数据头
headlist = [u'股票名称',u'代码',u'持有基金数量',u'变化率/%',u'持有市值/亿']
row ,col = 0, 0
for head in headlist:
    sheet.write(row,col,head)
    col += 1

urls = []
r = 0
for num in range(1,5):
    urls = yaml_data['Eastmoney_OrgHoldDataJson']['url_pre'] + str(num) + yaml_data['Eastmoney_OrgHoldDataJson']['url_suf']
    s = requests.get(urls)
    t = s.json()


    for i in range(20):
        r +=1
        c = 0
        SECURITY_NAME_ABBR = t['result']['data'][i]['SECURITY_NAME_ABBR']
        SECURITY_CODE = t['result']['data'][i]['SECURITY_CODE']
        HOULD_NUM = t['result']['data'][i]['HOULD_NUM']
        HOLDCHA_RATIO = t['result']['data'][i]['HOLDCHA_RATIO']
        HOLD_VALUE = t['result']['data'][i]['HOLD_VALUE']
        HOLD_VALUE = int(HOLD_VALUE) / 1e+8
        HOLD_VALUE = round(HOLD_VALUE,2)

        dic = [
            SECURITY_NAME_ABBR,
            SECURITY_CODE,
            HOULD_NUM,
            HOLDCHA_RATIO,
            HOLD_VALUE
            ]

        for _ in dic:
            sheet.write(r,c,_)
            c += 1
        wtbook.save(excelpath)
        print("已经完成" + str(r-1) + "项")