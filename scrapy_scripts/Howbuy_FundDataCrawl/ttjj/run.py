from scrapy import cmdline

from datetime import datetime

# 文件及路径，log目录需要先建好
today = datetime.now()
json_file_path = "data/howbuyfund_{}_{}_{}.json".format(today.year, today.month, today.day)

s = 'scrapy crawl test -o ' + json_file_path

cmdline.execute(s.split())
# cmdline.execute('scrapy crawl test -o fund_2_24.json'.split())
