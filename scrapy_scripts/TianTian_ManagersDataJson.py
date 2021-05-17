"""
通过分析得到的Json数据，获取所有基金经理的各项数据
"""

import json
import requests
import xlrd
import xlwt
from datetime import datetime
from getYAML import *
filename = os.path.basename(__file__).split('.')[0]
yaml_data = getyaml(filename)
# 文件及路径，目录需要先建好
today = datetime.now()
mgers_file_path = "D:\基金数据\最新数据\mgers_{}_{}_{}.xls".format(today.year, today.month, today.day)



s = requests.get(yaml_data['TianTian_ManagersDataJson']['url'])
t = s.json()
excelpath = mgers_file_path
wtbook = xlwt.Workbook(encoding = 'ascii')
#新增一个sheet工作表
sheet = wtbook.add_sheet('Sheet1',cell_overwrite_ok=True)
#写入数据头

headlist = [u'ID',u'姓名',u'年化回报',u'周收益',u'月收益',u'季度收益',u'半年收益',u'年收益',u'代表基金代码',u'代表基金名称']

row = 0
col = 0

for head in headlist:
    sheet.write(row,col,head)
    col += 1


for i in range(2534):
    r = i +1
    c = 0
    MGRID = t['Datas'][i]['MGRID']              #ID
    MGRNAME = t['Datas'][i]['MGRNAME']          #姓名
    YIELDSE = t['Datas'][i]['YIELDSE']          #年化回报
    W = t['Datas'][i]['W']
    M = t['Datas'][i]['M']
    Q = t['Datas'][i]['Q']
    HY = t['Datas'][i]['HY']
    Y = t['Datas'][i]['Y']
    PRECODE = t['Datas'][i]['PRECODE']          #代表基金代码
    SHORTNAME = t['Datas'][i]['SHORTNAME']      #代表基金名称

    dic = [MGRID,MGRNAME,YIELDSE,W,M,Q,HY,Y,PRECODE,SHORTNAME]

    for _ in dic:
        sheet.write(r,c,_)
        c += 1
    wtbook.save(excelpath)
    print("已经完成" + str(i) + "项")