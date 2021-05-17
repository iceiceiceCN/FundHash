# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv
import os
from itemadapter import ItemAdapter
from ttjj.items import TtjjItem

from datetime import datetime

# 文件及路径，目录需要先建好
today = datetime.now()
csv_file_path = "data/fund_{}_{}_{}.csv".format(today.year, today.month, today.day)


write_flag = 0
class TtjjPipeline:
    def __init__(self):
        self.f = open(csv_file_path, "a", encoding='utf_8_sig', newline="")
        # self.f = open("fund_2_24.csv", "a", encoding='utf-8', newline="")
        # 设置表头，要跟spider传过来的字典key名称相同
        self.fieldnames = ["SHORTNAME","FCODE","MGRID","MGRNAME","SHARP1","SHARP2","STDDEV1","STDDEV2","MAXRETRA1",
        "GP","ZQ","HB","JZC",
        "NowYear_up","NowYear_avg_up","NowYear_hs300_up","NowYear_rank","NowYear_competitors",
        "Week_up","Week_avg_up","Week_hs300_up","Week_rank","Week_competitors",
        "Month_up","Month_avg_up","Month_hs300_up","Month_rank","Month_competitors",
        "Year_up","Year_avg_up","Year_hs300_up","Year_rank","Year_competitors",
        "TwoYear_up","TwoYear_avg_up","TwoYear_hs300_up","TwoYear_rank","TwoYear_competitors",
        "ThreeYear_up","ThreeYear_avg_up","ThreeYear_hs300_up","ThreeYear_rank","ThreeYear_competitors",
        "FiveYear_up","FiveYear_avg_up","FiveYear_hs300_up","FiveYear_rank","FiveYear_competitors",
        "fundStocks_GPDM_0","fundStocks_GPJC_0","fundStocks_JZBL_0","fundStocks_PCTNVCHG_0",
        "fundStocks_GPDM_1","fundStocks_GPJC_1","fundStocks_JZBL_1","fundStocks_PCTNVCHG_1",
        "fundStocks_GPDM_2","fundStocks_GPJC_2","fundStocks_JZBL_2","fundStocks_PCTNVCHG_2",
        "fundStocks_GPDM_3","fundStocks_GPJC_3","fundStocks_JZBL_3","fundStocks_PCTNVCHG_3",
        "fundStocks_GPDM_4","fundStocks_GPJC_4","fundStocks_JZBL_4","fundStocks_PCTNVCHG_4",
        "fundStocks_GPDM_5","fundStocks_GPJC_5","fundStocks_JZBL_5","fundStocks_PCTNVCHG_5",
        "fundStocks_GPDM_6","fundStocks_GPJC_6","fundStocks_JZBL_6","fundStocks_PCTNVCHG_6",
        "fundStocks_GPDM_7","fundStocks_GPJC_7","fundStocks_JZBL_7","fundStocks_PCTNVCHG_7",
        "fundStocks_GPDM_8","fundStocks_GPJC_8","fundStocks_JZBL_8","fundStocks_PCTNVCHG_8",
        "fundStocks_GPDM_9","fundStocks_GPJC_9","fundStocks_JZBL_9","fundStocks_PCTNVCHG_9",
        ]
        self.writer = csv.DictWriter(self.f, fieldnames=self.fieldnames)
        self.writer.writeheader()

    def process_item(self, item, spider):
        global write_flag
        self.writer.writerow(item)
        # base_dir = os.getcwd()
        base_dir = os.path.abspath(os.path.dirname(os.getcwd()))
        txt_file_path = "/data/fund_{}_{}_{}.txt".format(today.year, today.month, today.day)
        filename = base_dir + txt_file_path
        with open(filename,'a') as f:
            if write_flag == 0:
                for key in self.fieldnames:
                    f.write(key + '\t')
                f.write('\n')
                write_flag = 1
            for key in self.fieldnames:
                f.write(item[key] + '\t')
            f.write('\n')
        return item

    def close(self, spider):
        self.f.close()
