import requests

r = open(r'D:\基金数据\最新数据\fundcode.txt','r')

a = r.readline()

x = a.split("[")[-1].split("]")[0].split("\"")

res = []
res_code = []


for i in range(1,len(x),2):
    res.append(x[i])


with open(r"D:\基金数据\最新数据\fundcode_res.txt","w") as r:
    for i in range(len(res)):
        line = ''
        code = res[i].split(',')[0]
        name = res[i].split(',')[1]
        line = str(code) + '\t' + str(name) + '\n'
        r.writelines(line)




