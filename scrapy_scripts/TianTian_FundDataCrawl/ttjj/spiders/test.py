import scrapy
from ttjj.items import TtjjItem
import time
import json
import os

import os, sys
current_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(current_dir)

import getYAML
yaml_data = getYAML.getyaml_Specifyname('TianTian_FundDataCrawl')

class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = [yaml_data['TianTian_FundDataCrawl']['allowed_domains']]
    start_urls = [yaml_data['TianTian_FundDataCrawl']['start_urls']]


    
    def parse(self, response):
        def getworkdir():
            os.chdir(os.path.dirname(__file__)) 
            print("当前工作路径为：" + str(os.getcwd()))
            path_ = os.getcwd()
            return path_
        getworkdir()
        pre = yaml_data['TianTian_FundDataCrawl']['pre']
        urls = []
        suf = '.json'
        # for line in open(r"../AllFundCode.txt","r",encoding = 'utf-8'):
        for line in open(r"../fundcode_res.txt","r",encoding = 'gbk'):
        # for line in open(r"../ttfundAll(NoZQ).txt","r",encoding = 'utf-8'):
            code = line.strip("\n").split('\t')[0]
            # code = line.strip("\n").split(',')[-1]
            full_add = str(pre) + str(code) + str(suf)
            urls.append(full_add)
        
        for url in urls:
            yield scrapy.Request(url,callback=self.parse_info)            
        
    
    def parse_info(self, response):
        item = TtjjItem()
        sites = json.loads(response.body_as_unicode())
        item['SHORTNAME'] = sites['JJXQ']['Datas']['SHORTNAME']
        item['FCODE'] = sites['JJXQ']['Datas']['FCODE']
        item['MGRID'] = sites['JJJL']['Datas'][0]['MGRID']
        item['MGRNAME'] = sites['JJJL']['Datas'][0]['MGRNAME']
        item['SHARP1'] = sites['JJXQ']['Datas']['SHARP1']
        item['SHARP2'] = sites['JJXQ']['Datas']['SHARP2']
        item['STDDEV1'] = sites['JJXQ']['Datas']['STDDEV1']
        item['STDDEV2'] = sites['JJXQ']['Datas']['STDDEV1']
        item['MAXRETRA1'] = sites['JJXQ']['Datas']['MAXRETRA1']
        
        try:
            item['GP'] = sites['JJCC']['Datas']['AssetAllocation']['2021-03-31'][0]['GP']        #股票
        except:
            item['GP'] = '-1'
        try:    
            item['ZQ'] = sites['JJCC']['Datas']['AssetAllocation']['2021-03-31'][0]['ZQ']        #债券
        except:
            item['ZQ'] = '-1'
        try:
            item['HB'] = sites['JJCC']['Datas']['AssetAllocation']['2021-03-31'][0]['HB']        #现金
        except:
            item['HB'] = '-1'
        try:
            item['JZC'] = sites['JJCC']['Datas']['AssetAllocation']['2021-03-31'][0]['JZC']        #总资产
        except:
            item['JZC'] = '-1'
        
        item['Week_up'] = sites['JDZF']['Datas'][0]['syl']
        item['Week_avg_up'] = sites['JDZF']['Datas'][0]['avg']
        item['Week_hs300_up'] = sites['JDZF']['Datas'][0]['hs300']
        item['Week_rank'] = sites['JDZF']['Datas'][0]['rank']
        item['Week_competitors'] = sites['JDZF']['Datas'][0]['sc']
        
        item['Month_up'] = sites['JDZF']['Datas'][1]['syl']
        item['Month_avg_up'] = sites['JDZF']['Datas'][1]['avg']
        item['Month_hs300_up'] = sites['JDZF']['Datas'][1]['hs300']
        item['Month_rank'] = sites['JDZF']['Datas'][1]['rank']
        item['Month_competitors'] = sites['JDZF']['Datas'][1]['sc']

        item['Year_up'] = sites['JDZF']['Datas'][4]['syl']
        item['Year_avg_up'] = sites['JDZF']['Datas'][4]['avg']
        item['Year_hs300_up'] = sites['JDZF']['Datas'][4]['hs300']
        item['Year_rank'] = sites['JDZF']['Datas'][4]['rank']
        item['Year_competitors'] = sites['JDZF']['Datas'][4]['sc']

        item['NowYear_up'] = sites['JDZF']['Datas'][8]['syl']
        item['NowYear_avg_up'] = sites['JDZF']['Datas'][8]['avg']
        item['NowYear_hs300_up'] = sites['JDZF']['Datas'][8]['hs300']
        item['NowYear_rank'] = sites['JDZF']['Datas'][8]['rank']
        item['NowYear_competitors'] = sites['JDZF']['Datas'][8]['sc']

        item['TwoYear_up'] = sites['JDZF']['Datas'][5]['syl']
        item['TwoYear_avg_up'] = sites['JDZF']['Datas'][5]['avg']
        item['TwoYear_hs300_up'] = sites['JDZF']['Datas'][5]['hs300']
        item['TwoYear_rank'] = sites['JDZF']['Datas'][5]['rank']
        item['TwoYear_competitors'] = sites['JDZF']['Datas'][5]['sc']

        item['ThreeYear_up'] = sites['JDZF']['Datas'][6]['syl']
        item['ThreeYear_avg_up'] = sites['JDZF']['Datas'][6]['avg']
        item['ThreeYear_hs300_up'] = sites['JDZF']['Datas'][6]['hs300']
        item['ThreeYear_rank'] = sites['JDZF']['Datas'][6]['rank']
        item['ThreeYear_competitors'] = sites['JDZF']['Datas'][6]['sc']

        item['FiveYear_up'] = sites['JDZF']['Datas'][7]['syl']
        item['FiveYear_avg_up'] = sites['JDZF']['Datas'][7]['avg']
        item['FiveYear_hs300_up'] = sites['JDZF']['Datas'][7]['hs300']
        item['FiveYear_rank'] = sites['JDZF']['Datas'][7]['rank']
        item['FiveYear_competitors'] = sites['JDZF']['Datas'][7]['sc']

        dic_fundStocks = ['fundStocks_GPDM_','fundStocks_GPJC_','fundStocks_JZBL_','fundStocks_PCTNVCHG_']
        
        for i in range(10):
            try:
                item['fundStocks_GPDM_'+str(i)] = sites['JJCC']['Datas']['InverstPosition']['fundStocks'][i]['GPDM']
                item['fundStocks_GPJC_'+str(i)] = sites['JJCC']['Datas']['InverstPosition']['fundStocks'][i]['GPJC']
                item['fundStocks_JZBL_'+str(i)] = sites['JJCC']['Datas']['InverstPosition']['fundStocks'][i]['JZBL']
                item['fundStocks_PCTNVCHG_'+str(i)] = sites['JJCC']['Datas']['InverstPosition']['fundStocks'][i]['PCTNVCHG']
            except:
                item['fundStocks_GPDM_'+str(i)] = '000000'
                item['fundStocks_GPJC_'+str(i)] = '无数据'
                item['fundStocks_JZBL_'+str(i)] = '0'
                item['fundStocks_PCTNVCHG_'+str(i)] = '0'
        # 无持仓异常处理
        # for i in range(10):
        #     try:
        #         item['fundStocks_GPDM_'+str(i)] = sites['JJCC']['Datas']['InverstPosition']['fundStocks'][i]['GPDM']
        #         item['fundStocks_GPJC_'+str(i)] = sites['JJCC']['Datas']['InverstPosition']['fundStocks'][i]['GPJC']
        #         item['fundStocks_JZBL_'+str(i)] = sites['JJCC']['Datas']['InverstPosition']['fundStocks'][i]['JZBL']
        #         item['fundStocks_PCTNVCHG_'+str(i)] = sites['JJCC']['Datas']['InverstPosition']['fundStocks'][i]['PCTNVCHG']
        #     except:
        #         item['fundStocks_GPDM_'+str(i)] = '-1'
        #         item['fundStocks_GPJC_'+str(i)] = '-1'
        #         item['fundStocks_JZBL_'+str(i)] = '-1'
        #         item['fundStocks_PCTNVCHG_'+str(i)] = '-1'


        # print(item)
        yield item


