path_flag = 0


if path_flag == 0:
    # A: 使用时间参数自动获取路径名
    from datetime import datetime

    today = datetime.now()

    path_fund = r'D:\基金数据\最新数据\fund_{}_{}_{}.txt'.format(today.year,today.month,today.day)
    path_orghold = r'D:\基金数据\最新数据\主力持仓数据_2021_4_27.txt'

    print(path_fund)
    print(path_orghold)
elif path_flag == 1:
    # B: 指定路径名
    path_fund = r'D:\基金数据\最新数据\fund_2021_3_18.txt'
    path_orghold = r'D:\基金数据\最新数据\主力持仓数据_2021_2_24.txt'

    print(path_fund)
    print(path_orghold)


w = open(path_orghold,'r')

dic_orghold = {}
for line in w:
    code = line.split('\t')[1]
    nums = line.split('\t')[2]
    
    dic_orghold[code] = int(nums)



f = open(path_fund,'r')


# 保存路径名:
# savepath_fund = r"D:\基金数据\最新数据\fund_after1_2021_3_18.txt" # 写死

savepath_fund = r"D:\基金数据\最新数据\fund_after1_{}_{}_{}.txt".format(today.year,today.month,today.day) # 自动获取
print(savepath_fund)


dic_fund = {}
b = 1
with open(savepath_fund,"w") as wr:
    for line in f:
        if b == 1:
            b += 1
            line = line.strip() + '\t' + 'BaoTuan' + '\n'
            wr.writelines(line)
            continue
        keys = []
        CODE = [line.split('\t')[-40],line.split('\t')[-36],line.split('\t')[-32],line.split('\t')[-28],line.split('\t')[-24],
                line.split('\t')[-20],line.split('\t')[-16],line.split('\t')[-12],line.split('\t')[-8],line.split('\t')[-4]]

        JZBL = [line.split('\t')[-38],line.split('\t')[-34],line.split('\t')[-30],line.split('\t')[-26],line.split('\t')[-22],
               line.split('\t')[-18],line.split('\t')[-14],line.split('\t')[-10],line.split('\t')[-6],line.split('\t')[-2]]
        # 会有纯债基金或者无持仓基金，所以做异常处理
        try:
            for i in range(10):
                dic_fund[CODE[i]] = float(JZBL[i])
                keys.append(CODE[i])

            count = 0
            for key in keys:
                if key in dic_orghold:
                    count = count + (dic_orghold[key]/1791) * (dic_fund[key] / 100)
                    count = round(count,4)
            line = line.strip() + '\t' + str(count) + '\n'
        except:
            line = line.strip() + '\t' + '-1' + '\n'
            
        wr.writelines(line)


