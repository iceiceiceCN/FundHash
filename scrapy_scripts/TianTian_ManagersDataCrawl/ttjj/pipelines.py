# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv
from itemadapter import ItemAdapter
from ttjj.items import TtjjItem


class TtjjPipeline:
    def __init__(self):
        self.f = open("ManagersData_3_18.csv", "a", encoding='utf-8', newline="")
        # 设置表头，要跟spider传过来的字典key名称相同
        self.fieldnames = ["MGRID","TOTALDAYS"]
        self.writer = csv.DictWriter(self.f, fieldnames=self.fieldnames)
        self.writer.writeheader()

    def process_item(self, item, spider):
        self.writer.writerow(item)
        return item

    def close(self, spider):
        self.f.close()
