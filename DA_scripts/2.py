"""
SHORTNAME	FCODE	SHARP1	SHARP2	STDDEV1	STDDEV2	MAXRETRA1	GP	ZQ	HB	
0           1       2       3       4       5       6           7   8   9 
JZC	Week_up	Week_avg_up	Week_hs300_up	Week_rank	Week_competitors	
10  11      12          13              14          15                 
Month_up	Month_avg_up	Month_hs300_up	Month_rank	Month_competitors	
16          17              18              19          20
Year_up	Year_avg_up	Year_hs300_up	Year_rank	Year_competitors
21      22          23              24          25
"""

# f = open(,'r',encoding='gb18030')
path = r'D:\基金数据-备份\alldata.txt'
data = []
for line in open(path,"r",encoding='gb18030'): #设置文件对象并读取每一行文件
    data.append(line)               #将每一行文件加入到list中
print(data)

