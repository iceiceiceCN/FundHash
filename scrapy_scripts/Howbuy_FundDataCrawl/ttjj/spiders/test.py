import scrapy
from ttjj.items import TtjjItem
import time
import json
import os
from datetime import datetime
import os, sys
current_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(current_dir)
today = datetime.now()

import getYAML

yaml_data = getYAML.getyaml_Specifyname('Howbuy_FundDataCrawl')
# print(yaml_data)

class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = [yaml_data['Howbuy_FundDataCrawl']['allowed_domains']]
    start_urls = [yaml_data['Howbuy_FundDataCrawl']['start_urls']]


    
    def parse(self, response):
        def getworkdir():
            os.chdir(os.path.dirname(__file__)) 
            print("当前工作路径为：" + str(os.getcwd()))
            path_ = os.getcwd()
            return path_
        getworkdir()
        pre = yaml_data['Howbuy_FundDataCrawl']['pre']
        urls = []
        suf = '/'
        for line in open(r"../fundcode_res.txt","r",encoding = 'gbk'):
        # for line in open(r"../fundcode_res_1.txt","r",encoding = 'utf-8'):
        # for line in open(r"../fund_2021_4_27.txt","r",encoding = 'gbk'):
            code = line.strip("\n").split('\t')[0]
            # code = line.strip("\n").split('\t')[1]
            full_add = str(pre) + str(code) + str(suf)
            urls.append(full_add)
        
        for url in urls:
            yield scrapy.Request(url,callback=self.parse_info)            
        
    
    def parse_info(self, response):
        item = TtjjItem()
        print(response.url)
        fundcode = response.url.split('/')[-2]
        # item['code'] = response.xpath("//*[@class='lt']//span[1]/text()").extract()[0].split('(')[-1].split(')')[0]
        try:
            # item['code'] = response.xpath("//*[@class='lt']//span[1]/text()").extract()[0][1:7]
            # item['code'] = response.xpath("//*[@class='lt']//span[1]/text()").extract_first()[1:7]
            item['code'] = fundcode
        except:
            item['code'] = response.xpath("//*[@class='ui-num']/text()").extract()[0]
        
        try:
            # item['date'] = response.xpath("//*[@class='b-0']/text()").extract()[0].split('[')[-1].split(']')[0]
            item['date'] = response.xpath("//*[@class='b-0']/text()").extract_first().split('[')[-1].split(']')[0]
        except:
            item['date'] = "{}-{}".format(today.month, today.day)
        
        try:
            item['jd_20_4'] = response.xpath("//*[@class='file_jjzf']/div[3]//tr[2]//text()").extract()[3]
        except:
            item['jd_20_4'] = "--"

        try:
            item['jd_20_3'] = response.xpath("//*[@class='file_jjzf']/div[3]//tr[2]//text()").extract()[5]
        except:
            item['jd_20_3'] = "--"

        try:
            item['jd_20_2'] = response.xpath("//*[@class='file_jjzf']/div[3]//tr[2]//text()").extract()[7]
        except:
            item['jd_20_2'] = "--"

        try:
            item['jd_20_1'] = response.xpath("//*[@class='file_jjzf']/div[3]//tr[2]//text()").extract()[9]
        except:
            item['jd_20_1'] = "--"

        try:
            item['jd_19_4'] = response.xpath("//*[@class='file_jjzf']/div[3]//tr[2]//text()").extract()[11]
        except:
            item['jd_19_4'] = "--"


        try:
            item['jd_19_3'] = response.xpath("//*[@class='file_jjzf']/div[3]//tr[2]//text()").extract()[13]
        except:
            item['jd_19_3'] = "--"
        
        try:
            item['jd_19_2'] = response.xpath("//*[@class='file_jjzf']/div[3]//tr[2]//text()").extract()[15]
        except:
            item['jd_19_2'] = "--"

        try:
            item['jd_19_1'] = response.xpath("//*[@class='file_jjzf']/div[3]//tr[2]//text()").extract()[17]
        except:
            item['jd_19_1'] = "--"

        try:
            item['nd_20'] = response.xpath("//*[@class='file_jjzf']/div[4]//tr[2]//text()").extract()[3]
        except:
            item['nd_20'] = "--"

        try:
            item['nd_19'] = response.xpath("//*[@class='file_jjzf']/div[4]//tr[2]//text()").extract()[5]
        except:
            item['nd_19'] = "--"
        try:
            item['nd_18'] = response.xpath("//*[@class='file_jjzf']/div[4]//tr[2]//text()").extract()[7]
        except:
            item['nd_18'] = "--"


        try:
            item['nd_17'] = response.xpath("//*[@class='file_jjzf']/div[4]//tr[2]//text()").extract()[9]
        except:
            item['nd_17'] = "--"

        try:
            item['nd_16'] = response.xpath("//*[@class='file_jjzf']/div[4]//tr[2]//text()").extract()[11]
        except:
            item['nd_16'] = "--"

        try:
            item['nd_15'] = response.xpath("//*[@class='file_jjzf']/div[4]//tr[2]//text()").extract()[13]
        except:
            item['nd_15'] = "--"

        try:
            item['nd_14'] = response.xpath("//*[@class='file_jjzf']/div[4]//tr[2]//text()").extract()[15]
        except:
            item['nd_14'] = "--"

        try:
            item['nd_13'] = response.xpath("//*[@class='file_jjzf']/div[4]//tr[2]//text()").extract()[17]
        except:         
            item['nd_13'] = "--"    
                                   
        yield item


