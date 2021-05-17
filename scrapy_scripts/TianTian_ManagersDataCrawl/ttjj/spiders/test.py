import scrapy
from ttjj.items import TtjjItem
import time
import json
import xlrd
import xlwt
import os
import os, sys
current_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(current_dir)

import getYAML
yaml_data = getYAML.getyaml_Specifyname('TianTian_ManagersDataCrawl')

class TestSpider(scrapy.Spider):
    name = 'ManagersDataCrawl'
    allowed_domains = [yaml_data['TianTian_ManagersDataCrawl']['allowed_domains']]
    start_urls = [yaml_data['TianTian_ManagersDataCrawl']['start_urls']]


    
    def parse(self, response):
        def getworkdir():
            os.chdir(os.path.dirname(__file__)) 
            print("当前工作路径为：" + str(os.getcwd()))
            path_ = os.getcwd()
            return path_
        getworkdir()
        urls = []

        pre = yaml_data['TianTian_ManagersDataCrawl']['pre']
        suf = yaml_data['TianTian_ManagersDataCrawl']['suf']
        for line in open(r"../managersid.txt","r",encoding = 'utf-8'):
            code = line.strip("\n")
            full_add = str(pre) + str(code) + str(suf)
            urls.append(full_add)

        # excelpath = r'C:\Users\gary\经理详情.xls'
        # #用于读取excel文件
        # tableopen = xlrd.open_workbook(excelpath)
        # table = tableopen.sheet_by_name('Sheet1')
        # h = table.nrows
        # l = table.ncols
        # colValues = table.col_values(0)
        # for i in range(1,h):
        #     num = colValues[i]
        #     full_add = str(pre) + str(num) + str(suf)
        #     urls.append(full_add)
        
        for url in urls:
            yield scrapy.Request(url,callback=self.parse_info)            
        
    
    def parse_info(self, response):
        item = TtjjItem()
        sites = json.loads(response.body_as_unicode())
        item['MGRID'] = sites['Datas']['MGRID']
        item['TOTALDAYS'] = sites['Datas']['TOTALDAYS']
        print(item)
        yield item




