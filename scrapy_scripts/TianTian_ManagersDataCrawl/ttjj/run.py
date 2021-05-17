from scrapy import cmdline
from datetime import datetime

# 文件及路径，log目录需要先建好
today = datetime.now()
json_file_path = "data/ManagersData_{}_{}_{}.json".format(today.year, today.month, today.day)

s = 'scrapy crawl ManagersDataCrawl -o ' + json_file_path
cmdline.execute(s.split())
# cmdline.execute('scrapy crawl ManagersDataCrawl -o ManagersData_4.json'.split())