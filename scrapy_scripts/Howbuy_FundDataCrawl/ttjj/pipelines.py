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
csv_file_path = "data/howbuyfund_{}_{}_{}.csv".format(today.year, today.month, today.day)

write_flag = 0
class TtjjPipeline:
    def __init__(self):
        self.f = open(csv_file_path, "a", encoding='utf_8_sig', newline="")
        # self.f = open("fund_2_24.csv", "a", encoding='utf-8', newline="")
        # 设置表头，要跟spider传过来的字典key名称相同
        self.fieldnames = [
        "code","date"
        ,"jd_20_4","jd_20_3","jd_20_2","jd_20_1"
        ,"jd_19_4","jd_19_3","jd_19_2","jd_19_1"
        ,"nd_20","nd_19","nd_18","nd_17","nd_16","nd_15","nd_14","nd_13"
        ]
        self.writer = csv.DictWriter(self.f, fieldnames=self.fieldnames)
        self.writer.writeheader()

    def process_item(self, item, spider):
        global write_flag
        self.writer.writerow(item)
        # base_dir = os.getcwd()
        base_dir = os.path.abspath(os.path.dirname(os.getcwd()))
        txt_file_path = "/data/howbuyfund_{}_{}_{}.txt".format(today.year, today.month, today.day)
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
