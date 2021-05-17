# A: 使用时间参数自动获取路径名
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pylab as plt

today = datetime.now()

path_fund = r'D:\基金数据\最新数据\fund_{}_{}_{}.txt'.format(today.year,today.month,today.day)
path_orghold = r'D:\基金数据\最新数据\主力持仓数据_2021_4_27.txt'


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
                    count = count + (dic_orghold[key]/1676) * (dic_fund[key] / 100)
                    count = round(count,4)
            line = line.strip() + '\t' + str(count) + '\n'
        except:
            line = line.strip() + '\t' + '-1' + '\n'
            
        wr.writelines(line)

################################################


# A: 使用时间参数自动获取路径名
from datetime import datetime

today = datetime.now()

path_fund = r'D:\基金数据\最新数据\fund_after1_{}_{}_{}.txt'.format(today.year,today.month,today.day)
path_m = r'D:\基金数据\最新数据\mgers_after0_2021_3_18.txt'

m = open(path_m,'r')
dic={} # days
dic1={} # Pay
keys=[]


m.readline()

for line in m:
#     if len(line.strip().split('\t'))==4:
    ID = line.strip().split('\t')[0]
    Name = line.strip().split('\t')[1]
    Pay = line.strip().split('\t')[2]
    Days = line.strip().split('\t')[-1]
#         print(Pay)
    dic[str(ID)] = int(Days)
    dic1[str(ID)] = Pay
    keys.append(ID)


for key in dic1:
    if dic1[key] == '':
        dic1[key] = 0


# 保存路径名:
# savepath_fund = r"D:\基金数据\最新数据\fund_after1_2021_3_18.txt" # 写死

savepath_fund = r"D:\基金数据\最新数据\fund_after2_{}_{}_{}.txt".format(today.year,today.month,today.day) # 自动获取
print(savepath_fund)


# 只算经理中最大值
f = open(path_fund,'r')
c = 1
with open(savepath_fund,"w") as wr:
    for line in f:
        if c == 1:
            c+=1
            line = line.strip() + '\t' + 'Payback' +'\t' + 'Days' + '\n' 
#             continue
        IDs = line.split('\t')[2]
        IDs = IDs.replace('"','')
        
        if len(IDs.split(',')) == 1:
            ID = IDs
            if ID in dic and ID in dic1:
                line = line.strip() + '\t' + str(dic1[str(ID)]) + '\t' + str(dic[str(ID)]) + '\n'
                
        elif len(IDs.split(',')) == 2:            
            ID0 = IDs.split(',')[0]
            ID1 = IDs.split(',')[1]
            
            if ID0 in dic and ID1 in dic and ID0 in dic1 and ID1 in dic1:
                if float(dic[str(ID0)]) > float(dic[str(ID1)]):
                    maxID = ID0
                else:
                    maxID = ID1
                    
                maxDays = float(dic[str(maxID)])
                maxPay = float(dic1[str(maxID)])
                line = line.strip() + '\t' + str(maxPay) +'\t' + str(maxDays) + '\n'
  
        elif len(IDs.split(',')) == 3:
            ID0 = IDs.split(',')[0]
            ID1 = IDs.split(',')[1]
            ID2 = IDs.split(',')[2]
            
            if ID0 in dic and ID1 in dic and ID2 in dic and ID0 in dic1 and ID1 in dic1 and ID2 in dic1:
                if float(dic[str(ID0)]) > float(dic[str(ID1)]) and float(dic[str(ID0)]) > float(dic[str(ID2)]):
                    maxID = ID0
                elif float(dic[str(ID1)]) > float(dic[str(ID0)]) and float(dic[str(ID1)]) > float(dic[str(ID2)]):
                    maxID = ID1
                elif float(dic[str(ID2)]) > float(dic[str(ID1)]) and float(dic[str(ID2)]) > float(dic[str(ID0)]):
                    maxID = ID2                
                
                maxDays = float(dic[str(maxID)])
                maxPay = float(dic1[str(maxID)])
                line = line.strip() + '\t' + str(maxPay) +'\t' + str(maxDays) + '\n' 
        wr.writelines(line)



###############################################



# A: 使用时间参数自动获取路径名
from datetime import datetime

today = datetime.now()

path = r'D:\基金数据\最新数据\fund_after2_{}_{}_{}.txt'.format(today.year,today.month,today.day)

print(path)

# 要求输入列为：
# SHORTNAME	FCODE	MGRID	MGRNAME	SHARP1	SHARP2	STDDEV1	STDDEV2	MAXRETRA1	GP	ZQ	HB	JZC	Week_up	Week_avg_up	Week_hs300_up	Week_rank	Week_competitors	Month_up	Month_avg_up	Month_hs300_up	Month_rank	Month_competitors	Year_up	Year_avg_up	Year_hs300_up	Year_rank	Year_competitors	NowYear_up	NowYear_avg_up	NowYear_hs300_up	NowYear_rank	NowYear_competitors	TwoYear_up	TwoYear_avg_up	TwoYear_hs300_up	TwoYear_rank	TwoYear_competitors	ThreeYear_up	ThreeYear_avg_up	ThreeYear_hs300_up	ThreeYear_rank	ThreeYear_competitors	FiveYear_up	FiveYear_avg_up	FiveYear_hs300_up	FiveYear_rank	FiveYear_competitors	fundStocks_GPDM_0	fundStocks_GPJC_0	fundStocks_JZBL_0	fundStocks_PCTNVCHG_0	fundStocks_GPDM_1	fundStocks_GPJC_1	fundStocks_JZBL_1	fundStocks_PCTNVCHG_1	fundStocks_GPDM_2	fundStocks_GPJC_2	fundStocks_JZBL_2	fundStocks_PCTNVCHG_2	fundStocks_GPDM_3	fundStocks_GPJC_3	fundStocks_JZBL_3	fundStocks_PCTNVCHG_3	fundStocks_GPDM_4	fundStocks_GPJC_4	fundStocks_JZBL_4	fundStocks_PCTNVCHG_4	fundStocks_GPDM_5	fundStocks_GPJC_5	fundStocks_JZBL_5	fundStocks_PCTNVCHG_5	fundStocks_GPDM_6	fundStocks_GPJC_6	fundStocks_JZBL_6	fundStocks_PCTNVCHG_6	fundStocks_GPDM_7	fundStocks_GPJC_7	fundStocks_JZBL_7	fundStocks_PCTNVCHG_7	fundStocks_GPDM_8	fundStocks_GPJC_8	fundStocks_JZBL_8	fundStocks_PCTNVCHG_8	fundStocks_GPDM_9	fundStocks_GPJC_9	fundStocks_JZBL_9	fundStocks_PCTNVCHG_9	BaoTuan	Payback	Days
df = pd.read_table(path,converters={'FCODE':str,'MGRID':str},encoding='GB18030')


# 归一化函数
max_min_scaler = lambda x : (x-np.min(x))/(np.max(x)-np.min(x))

# 将'--'替换为 -1
df.replace('--', -1,inplace=True)





df["SHARP1"] = pd.to_numeric(df["SHARP1"])
df["SHARP2"] = pd.to_numeric(df["SHARP2"])
df["STDDEV1"] = pd.to_numeric(df["STDDEV1"])
df["STDDEV2"] = pd.to_numeric(df["STDDEV2"])
df["ZQ"] = pd.to_numeric(df["ZQ"])
df["HB"] = pd.to_numeric(df["HB"])
df["GP"] = pd.to_numeric(df["GP"])
df["MAXRETRA1"] = pd.to_numeric(df["MAXRETRA1"])
df["Week_rank"] = pd.to_numeric(df["Week_rank"])
df["Week_competitors"] = pd.to_numeric(df["Week_competitors"])

df["Month_rank"] = pd.to_numeric(df["Month_rank"])
df["Month_competitors"] = pd.to_numeric(df["Month_competitors"])

df["Year_rank"] = pd.to_numeric(df["Year_rank"])
df["Year_competitors"] = pd.to_numeric(df["Year_competitors"])

df["NowYear_rank"] = pd.to_numeric(df["NowYear_rank"])
df["NowYear_competitors"] = pd.to_numeric(df["NowYear_competitors"])

df["TwoYear_rank"] = pd.to_numeric(df["TwoYear_rank"])
df["TwoYear_competitors"] = pd.to_numeric(df["TwoYear_competitors"])

df["ThreeYear_rank"] = pd.to_numeric(df["ThreeYear_rank"])
df["ThreeYear_competitors"] = pd.to_numeric(df["ThreeYear_competitors"])

df["FiveYear_rank"] = pd.to_numeric(df["FiveYear_rank"])
df["FiveYear_competitors"] = pd.to_numeric(df["FiveYear_competitors"])


# 增加 收益回撤比 列
df['收益回撤比'] = df['Year_up'] / df['MAXRETRA1']


# 对 BaoTuan 列进行归一化
d = df[['BaoTuan']].apply(max_min_scaler)
# d = df['BaoTuan'].apply(max_min_scaler) 这个写法是错的

df['BaoTuan'] = d

# 获得两份 df 的备份
df1 = df.copy()
df2 = df.copy()

# 将 rank 列 转换为 比率
df2['Week_rank'] = df1['Week_rank'] / df1['Week_competitors']
df2['Month_rank'] = df1['Month_rank'] / df1['Month_competitors']
df2['Year_rank'] = df1['Year_rank'] / df1['Year_competitors']
df2['NowYear_rank'] = df1['NowYear_rank'] / df1['NowYear_competitors']
df2['TwoYear_rank'] = df1['TwoYear_rank'] / df1['TwoYear_competitors']
df2['ThreeYear_rank'] = df1['ThreeYear_rank'] / df1['ThreeYear_competitors']
df2['FiveYear_rank'] = df1['FiveYear_rank'] / df1['FiveYear_competitors']



# 删去 df2 中部分列
df2 = df2.drop(columns=['Week_competitors','Month_competitors','Year_competitors','NowYear_competitors','TwoYear_competitors','ThreeYear_competitors','FiveYear_competitors'
                        ,'Week_hs300_up','Month_hs300_up','Year_hs300_up','NowYear_hs300_up','TwoYear_hs300_up','ThreeYear_hs300_up','FiveYear_hs300_up'
                        ,'Week_avg_up','Month_avg_up','Year_avg_up','NowYear_avg_up','TwoYear_avg_up','ThreeYear_avg_up','FiveYear_avg_up'
                        ,'MGRID','MGRNAME'
                        ,'fundStocks_GPDM_0','fundStocks_GPJC_0','fundStocks_JZBL_0','fundStocks_PCTNVCHG_0'
                       ,'fundStocks_GPDM_1','fundStocks_GPJC_1','fundStocks_JZBL_1','fundStocks_PCTNVCHG_1'
                       ,'fundStocks_GPDM_2','fundStocks_GPJC_2','fundStocks_JZBL_2','fundStocks_PCTNVCHG_2'
                       ,'fundStocks_GPDM_3','fundStocks_GPJC_3','fundStocks_JZBL_3','fundStocks_PCTNVCHG_3'
                       ,'fundStocks_GPDM_4','fundStocks_GPJC_4','fundStocks_JZBL_4','fundStocks_PCTNVCHG_4'
                       ,'fundStocks_GPDM_5','fundStocks_GPJC_5','fundStocks_JZBL_5','fundStocks_PCTNVCHG_5'
                       ,'fundStocks_GPDM_6','fundStocks_GPJC_6','fundStocks_JZBL_6','fundStocks_PCTNVCHG_6'
                       ,'fundStocks_GPDM_7','fundStocks_GPJC_7','fundStocks_JZBL_7','fundStocks_PCTNVCHG_7'
                       ,'fundStocks_GPDM_8','fundStocks_GPJC_8','fundStocks_JZBL_8','fundStocks_PCTNVCHG_8'
                       ,'fundStocks_GPDM_9','fundStocks_GPJC_9','fundStocks_JZBL_9','fundStocks_PCTNVCHG_9'])
df2




# 将NaN值调补为-1
df4 = pd.DataFrame(df2.fillna(-1))
df4 = df4.drop(columns=['SHORTNAME','FCODE'])
df4

# 得到数据集 df4





from sklearn import preprocessing
X_scaled = preprocessing.scale(df4)  # scale操作之后的数据零均值，单位方差（方差为1）
X_scaled[0:5]



# 进行PCA数据降维
from sklearn.decomposition import PCA
 
# 生成PCA实例
pca = PCA(n_components=3)  # 把维度降至3维
# 进行PCA降维
X_pca = pca.fit_transform(X_scaled)
# 生成降维后的dataframe
X_pca_frame = pd.DataFrame(X_pca, columns=['pca_1', 'pca_2', 'pca_3'])  # 原始数据由(30000, 7)降维至(30000, 3)
# X_pca_frame.head()
X_pca_frame



# 训练简单模型
from sklearn.cluster import KMeans
 
# KMeans算法实例化，将其设置为K=10
est = KMeans(n_clusters=10)
 
# 作用到降维后的数据上
est.fit(X_pca)


KMeans(algorithm='auto', copy_x=True, init='k-means++', max_iter=300,
       n_clusters=10, n_init=10, n_jobs=None, precompute_distances='auto',
       random_state=None, tol=0.0001, verbose=0)



# 取出聚类后的标签
kmeans_clustering_labels = pd.DataFrame(est.labels_, columns=['cluster'])  # 0-9,一共10个标签
 
# 生成有聚类后的dataframe
X_pca_frame = pd.concat([X_pca_frame, kmeans_clustering_labels], axis=1)
 
X_pca_frame.head()


# 对不同的k值进行计算，筛选出最优的K值
from mpl_toolkits.mplot3d import Axes3D  # 绘制3D图形
from sklearn import metrics
 
# KMeans算法实例化，将其设置为K=range(2, 14)
d = {}
fig_reduced_data = plt.figure(figsize=(12, 12))  #画图之前首先设置figure对象，此函数相当于设置一块自定义大小的画布，使得后面的图形输出在这块规定了大小的画布上，其中参数figsize设置画布大小
for k in range(2, 14):
    est = KMeans(n_clusters=k, random_state=111)
    # 作用到降维后的数据上
    y_pred = est.fit_predict(X_pca)
    # 评估不同k值聚类算法效果
    calinski_harabaz_score = metrics.calinski_harabasz_score(X_pca_frame, y_pred)  # X_pca_frame：表示要聚类的样本数据，一般形如（samples，features）的格式。y_pred：即聚类之后得到的label标签，形如（samples，）的格式
    d.update({k: calinski_harabaz_score})
    print('calinski_harabaz_score with k={0} is {1}'.format(k, calinski_harabaz_score))  # CH score的数值越大越好
    # 生成三维图形，每个样本点的坐标分别是三个主成分的值
    ax = plt.subplot(4, 3, k - 1, projection='3d') #将figure设置的画布大小分成几个部分，表示4(row)x3(colu),即将画布分成4x3，四行三列的12块区域，k-1表示选择图形输出的区域在第k-1块，图形输出区域参数必须在“行x列”范围
    ax.scatter(X_pca_frame.pca_1, X_pca_frame.pca_2, X_pca_frame.pca_3, c=y_pred)  # pca_1、pca_2、pca_3为输入数据，c表示颜色序列
    ax.set_xlabel('pca_1')
    ax.set_ylabel('pca_2')
    ax.set_zlabel('pca_3')







# 绘制不同k值对应的score，找到最优的k值
x = []
y = []
for k, score in d.items():
    x.append(k)
    y.append(score)
 
plt.plot(x, y)
plt.xlabel('k value')
plt.ylabel('calinski_harabaz_score')





c1 = df1.pop('收益回撤比')
df1.insert(9,'收益回撤比',c1)

c2 = df1.pop('BaoTuan')
df1.insert(9,'BaoTuan',c2)

c3 = df1.pop('Days')
df1.insert(9,'Days',c3)

c4 = df1.pop('Payback')
df1.insert(9,'Payback',c4)




df1.index = X_pca_frame.index  # 返回：RangeIndex(start=0, stop=30000, step=1)
 
# 合并原数据和三个主成分的数据
X_full = pd.concat([df1, X_pca_frame], axis=1)
X_full = X_full.round(3)
X_full = pd.DataFrame(X_full.fillna(-1))
X_full.head()



# 保存路径名:
# savepath_csv = r"D:\基金数据\最新数据\Data_after3_3_18.csv" # 写死
# savepath_txt = r"D:\基金数据\最新数据\Data_after3_3_18.txt" # 写死

savepath_csv = r"D:\基金数据\最新数据\Data_after3_{}_{}_{}.csv".format(today.year,today.month,today.day) # 自动获取
savepath_txt = r"D:\基金数据\最新数据\Data_after3_{}_{}_{}.txt".format(today.year,today.month,today.day) # 自动获取
print(savepath_csv)
print(savepath_txt)


X_full.to_csv(savepath_csv,encoding='GB18030')
X_full.to_csv(savepath_txt,sep='\t',index=False,encoding='GB18030')


############################


# A: 使用时间参数自动获取路径名
from datetime import datetime

today = datetime.now()

path_ttfund = r"D:\基金数据\最新数据\Data_after3_{}_{}_{}.txt".format(today.year,today.month,today.day)
path_hbfund = r"D:\基金数据\最新数据\howbuyfund_{}_{}_{}.txt".format(today.year,today.month,today.day)
# 要求输入列为：
# SHORTNAME	FCODE	MGRID	MGRNAME	SHARP1	SHARP2	STDDEV1	STDDEV2	MAXRETRA1	GP	ZQ	HB	JZC	Week_up	Week_avg_up	Week_hs300_up	Week_rank	Week_competitors	Month_up	Month_avg_up	Month_hs300_up	Month_rank	Month_competitors	Year_up	Year_avg_up	Year_hs300_up	Year_rank	Year_competitors	NowYear_up	NowYear_avg_up	NowYear_hs300_up	NowYear_rank	NowYear_competitors	TwoYear_up	TwoYear_avg_up	TwoYear_hs300_up	TwoYear_rank	TwoYear_competitors	ThreeYear_up	ThreeYear_avg_up	ThreeYear_hs300_up	ThreeYear_rank	ThreeYear_competitors	FiveYear_up	FiveYear_avg_up	FiveYear_hs300_up	FiveYear_rank	FiveYear_competitors	fundStocks_GPDM_0	fundStocks_GPJC_0	fundStocks_JZBL_0	fundStocks_PCTNVCHG_0	fundStocks_GPDM_1	fundStocks_GPJC_1	fundStocks_JZBL_1	fundStocks_PCTNVCHG_1	fundStocks_GPDM_2	fundStocks_GPJC_2	fundStocks_JZBL_2	fundStocks_PCTNVCHG_2	fundStocks_GPDM_3	fundStocks_GPJC_3	fundStocks_JZBL_3	fundStocks_PCTNVCHG_3	fundStocks_GPDM_4	fundStocks_GPJC_4	fundStocks_JZBL_4	fundStocks_PCTNVCHG_4	fundStocks_GPDM_5	fundStocks_GPJC_5	fundStocks_JZBL_5	fundStocks_PCTNVCHG_5	fundStocks_GPDM_6	fundStocks_GPJC_6	fundStocks_JZBL_6	fundStocks_PCTNVCHG_6	fundStocks_GPDM_7	fundStocks_GPJC_7	fundStocks_JZBL_7	fundStocks_PCTNVCHG_7	fundStocks_GPDM_8	fundStocks_GPJC_8	fundStocks_JZBL_8	fundStocks_PCTNVCHG_8	fundStocks_GPDM_9	fundStocks_GPJC_9	fundStocks_JZBL_9	fundStocks_PCTNVCHG_9	BaoTuan	Payback	Days
df_tt = pd.read_table(path_ttfund,converters={'FCODE':str,'MGRID':str},encoding='GB18030')
df_hb = pd.read_table(path_hbfund,converters={'code':str,'date':str},encoding='GB18030')
print(path_ttfund)
print(path_hbfund)

keys = df_hb.code.values



shuzi = []
notin = []
mykeys_tt = []
for i in range(len(df_tt['FCODE'])):
    mykeys_tt.append(str(df_tt['FCODE'][i]))

for i in range(len(df_hb['code'])):
    if str(df_hb['code'][i]) in mykeys_tt:
        shuzi.append(1)
    else:
        notin.append(str(df_hb['code'][i]))



# for i in range(len(df_hb['code'])):
#     if str(df_tt['FCODE'][i]) in str(df_hb['code']):
#         print(df_tt['FCODE'][i])
#         shuzi.append(1)
#     else:
#         shuzi.append(0)
        

a = shuzi.count(1)
a

df_merge = pd.merge(df_tt,df_hb,left_on="FCODE",right_on="code")


df_merge.columns.values



# 保存路径名:
# savepath_csv = r"D:\基金数据\最新数据\Data_after3_3_18.csv" # 写死
# savepath_txt = r"D:\基金数据\最新数据\Data_after3_3_18.txt" # 写死
from datetime import datetime

today = datetime.now()

savepath_csv = r"D:\基金数据\最新数据\Data_after4_{}_{}_{}.csv".format(today.year,today.month,today.day) # 自动获取
savepath_txt = r"D:\基金数据\最新数据\Data_after4_{}_{}_{}.txt".format(today.year,today.month,today.day) # 自动获取
print(savepath_csv)
print(savepath_txt)

df_merge.to_csv(savepath_csv,encoding='GB18030')
df_merge.to_csv(savepath_txt,sep='\t',index=False,encoding='GB18030')


##########################################

# A: 使用时间参数自动获取路径名
from datetime import datetime

today = datetime.now()

path = r"D:\基金数据\最新数据\Data_after4_{}_{}_{}.txt".format(today.year,today.month,today.day) # 自动获取
# 要求输入列为：
# SHORTNAME	FCODE	MGRID	MGRNAME	SHARP1	SHARP2	STDDEV1	STDDEV2	MAXRETRA1	GP	ZQ	HB	JZC	Week_up	Week_avg_up	Week_hs300_up	Week_rank	Week_competitors	Month_up	Month_avg_up	Month_hs300_up	Month_rank	Month_competitors	Year_up	Year_avg_up	Year_hs300_up	Year_rank	Year_competitors	NowYear_up	NowYear_avg_up	NowYear_hs300_up	NowYear_rank	NowYear_competitors	TwoYear_up	TwoYear_avg_up	TwoYear_hs300_up	TwoYear_rank	TwoYear_competitors	ThreeYear_up	ThreeYear_avg_up	ThreeYear_hs300_up	ThreeYear_rank	ThreeYear_competitors	FiveYear_up	FiveYear_avg_up	FiveYear_hs300_up	FiveYear_rank	FiveYear_competitors	fundStocks_GPDM_0	fundStocks_GPJC_0	fundStocks_JZBL_0	fundStocks_PCTNVCHG_0	fundStocks_GPDM_1	fundStocks_GPJC_1	fundStocks_JZBL_1	fundStocks_PCTNVCHG_1	fundStocks_GPDM_2	fundStocks_GPJC_2	fundStocks_JZBL_2	fundStocks_PCTNVCHG_2	fundStocks_GPDM_3	fundStocks_GPJC_3	fundStocks_JZBL_3	fundStocks_PCTNVCHG_3	fundStocks_GPDM_4	fundStocks_GPJC_4	fundStocks_JZBL_4	fundStocks_PCTNVCHG_4	fundStocks_GPDM_5	fundStocks_GPJC_5	fundStocks_JZBL_5	fundStocks_PCTNVCHG_5	fundStocks_GPDM_6	fundStocks_GPJC_6	fundStocks_JZBL_6	fundStocks_PCTNVCHG_6	fundStocks_GPDM_7	fundStocks_GPJC_7	fundStocks_JZBL_7	fundStocks_PCTNVCHG_7	fundStocks_GPDM_8	fundStocks_GPJC_8	fundStocks_JZBL_8	fundStocks_PCTNVCHG_8	fundStocks_GPDM_9	fundStocks_GPJC_9	fundStocks_JZBL_9	fundStocks_PCTNVCHG_9	BaoTuan	Payback	Days
df = pd.read_table(path,converters={'FCODE':str,'MGRID':str},encoding='GB18030')

print(path)




df1 = df.copy()

datalen = len(df1)
datalen

# x = df1['SHARP1']
# x.dtypes
s = df1['SHARP1'][0]
s.dtype
# if x.dtypes == 'float64':
#     print('0')
# y = df1['nd_16']
# y.dtypes



def getSortedList(colName):
    x = df1[colName]
    x = x.replace('--',-100)
    if type(x[0]) == str: # 如果为字符串
        x1 = x.str.strip('%').astype(float)/100
        x_res = x1.sort_values(ascending=False).tolist() 
        return x_res
    if x.dtypes == 'float64':
        x_res = x.sort_values(ascending=False).tolist()
        return x_res

#     return x_res



def getSortedListASCE(colName):
    x = df1[colName]
    x = x.replace('--',-100)
    if type(x) == str:
        x1 = x.str.strip('%').astype(float)/100
        x_res = x1.sort_values(ascending=True).tolist()
        return x_res
    if x.dtypes == 'float64':
        x_res = x.sort_values(ascending=True).tolist()
        return x_res

#     return x_res





def getData(colName,index):
    x = df1[colName][index]
    if x == '--':
        return -1
    if type(x) == str:
        data = float(x.strip('%'))/100
        return data
    if x.dtype == 'float64':
        data = x
        return data
    else:
        return -1
    
#     return data


def searchInsert(nums, target):
    left = 0
    right = len(nums)
    while left < right:
        mid = (left + right) // 2

        if target < nums[mid]: ## 修改了大于小于号
            left = mid + 1 # 位置变化
        else:
            right = mid

    return left




def getRanking(SortedList,data):
#     index = searchInsert(SortedList,data) # 二分搜索查找插入位置，值可以不在列表内
    try:
        if data == -1:
            # return len(SortedList)
            return datalen
    #     rank = np.where(np.array(SortedList) == float(data))[0][0] # 值必须在列表内
        rank = SortedList.index(data)
        rank_ = int(rank) + 1
        return rank_
    except:
        return datalen
#     return index


df1 = df.copy()
df1.head(5)


def insertRank(colname,df):
    tmp_RankList = []
    for i in range(len(df['FCODE'])):
        tmp_SortedList = getSortedList(colname)
        tmp_data = getData(colname,i)
        tmp_Rank = getRanking(tmp_SortedList,tmp_data)
        tmp_RankList.append(tmp_Rank)
    name = colname + '_rank'
    df[name] = tmp_RankList
#     return df



def insertRankASCE(colname,df):
    tmp_RankList = []
    for i in range(len(df['FCODE'])):
        tmp_SortedList = getSortedListASCE(colname)
        tmp_data = getData(colname,i)
        tmp_Rank = getRanking(tmp_SortedList,tmp_data)
        tmp_RankList.append(tmp_Rank)
    name = colname + '_rank'
    df[name] = tmp_RankList
#     return df

# 越大越好
insertRank('SHARP1',df1)
insertRank('SHARP2',df1)
insertRank('收益回撤比',df1)
insertRank('Days',df1)
insertRank('Payback',df1)

# 越小越好
insertRank('STDDEV1',df1)
insertRank('STDDEV2',df1)
insertRank('MAXRETRA1',df1) # 越大 排名越靠前 所以应该反过来


insertRank('jd_20_4',df1)
insertRank('jd_20_3',df1)
insertRank('jd_20_2',df1)
insertRank('jd_20_1',df1)


insertRank('jd_19_4',df1)
insertRank('jd_19_3',df1)
insertRank('jd_19_2',df1)
insertRank('jd_19_1',df1)


insertRank('nd_20',df1)
insertRank('nd_19',df1)
insertRank('nd_18',df1)
insertRank('nd_17',df1)

insertRank('nd_16',df1)
insertRank('nd_15',df1)
insertRank('nd_14',df1)
insertRank('nd_13',df1)

df_10 = df1[['MAXRETRA1','MAXRETRA1_rank']]
df_10[['MAXRETRA1_rank']]  = df_10[['MAXRETRA1_rank']].apply(pd.to_numeric)
df_10[['MAXRETRA1','MAXRETRA1_rank']].sort_values(by = ['MAXRETRA1'],ascending=False)

df2 = df1.iloc[:,-16:-1]

table1 = ['SHORTNAME','FCODE','date','cluster','MGRID','MGRNAME',
        'Days','Days_rank',
        'Payback','Payback_rank',
        'SHARP1','SHARP1_rank',
        'SHARP2','SHARP2_rank',
        'STDDEV1','STDDEV1_rank',
        'STDDEV2','STDDEV2_rank',
        'MAXRETRA1','MAXRETRA1_rank',
        'BaoTuan',
         '收益回撤比','收益回撤比_rank',
          'GP', 'ZQ', 'HB', 'JZC',
         'Week_up', 'Week_avg_up',
       'Week_hs300_up', 'Week_rank', 'Week_competitors', 'Month_up',
       'Month_avg_up', 'Month_hs300_up', 'Month_rank',
       'Month_competitors', 'Year_up', 'Year_avg_up', 'Year_hs300_up',
       'Year_rank', 'Year_competitors', 'NowYear_up', 'NowYear_avg_up',
       'NowYear_hs300_up', 'NowYear_rank', 'NowYear_competitors',
       'TwoYear_up', 'TwoYear_avg_up', 'TwoYear_hs300_up', 'TwoYear_rank',
       'TwoYear_competitors', 'ThreeYear_up', 'ThreeYear_avg_up',
       'ThreeYear_hs300_up', 'ThreeYear_rank', 'ThreeYear_competitors',
       'FiveYear_up', 'FiveYear_avg_up', 'FiveYear_hs300_up',
       'FiveYear_rank', 'FiveYear_competitors', 'fundStocks_GPDM_0',
       'fundStocks_GPJC_0', 'fundStocks_JZBL_0', 'fundStocks_PCTNVCHG_0',
       'fundStocks_GPDM_1', 'fundStocks_GPJC_1', 'fundStocks_JZBL_1',
       'fundStocks_PCTNVCHG_1', 'fundStocks_GPDM_2', 'fundStocks_GPJC_2',
       'fundStocks_JZBL_2', 'fundStocks_PCTNVCHG_2', 'fundStocks_GPDM_3',
       'fundStocks_GPJC_3', 'fundStocks_JZBL_3', 'fundStocks_PCTNVCHG_3',
       'fundStocks_GPDM_4', 'fundStocks_GPJC_4', 'fundStocks_JZBL_4',
       'fundStocks_PCTNVCHG_4', 'fundStocks_GPDM_5', 'fundStocks_GPJC_5',
       'fundStocks_JZBL_5', 'fundStocks_PCTNVCHG_5', 'fundStocks_GPDM_6',
       'fundStocks_GPJC_6', 'fundStocks_JZBL_6', 'fundStocks_PCTNVCHG_6',
       'fundStocks_GPDM_7', 'fundStocks_GPJC_7', 'fundStocks_JZBL_7',
       'fundStocks_PCTNVCHG_7', 'fundStocks_GPDM_8', 'fundStocks_GPJC_8',
       'fundStocks_JZBL_8', 'fundStocks_PCTNVCHG_8', 'fundStocks_GPDM_9',
       'fundStocks_GPJC_9', 'fundStocks_JZBL_9', 'fundStocks_PCTNVCHG_9',
        'jd_20_4','jd_20_4_rank',
          'jd_20_3','jd_20_3_rank',
          'jd_20_2', 'jd_20_2_rank',
          'jd_20_1', 'jd_20_1_rank',
          'jd_19_4', 'jd_19_4_rank',
          'jd_19_3','jd_19_3_rank',
          'jd_19_2','jd_19_2_rank',
          'jd_19_1', 'jd_19_1_rank',
          'nd_20', 'nd_20_rank',
          'nd_19','nd_19_rank',
          'nd_18','nd_18_rank',
          'nd_17', 'nd_17_rank',
          'nd_16', 'nd_16_rank',
          'nd_15','nd_15_rank',
          'nd_14', 'nd_14_rank',
          'nd_13','nd_13_rank']

df_table1 = df1[table1]


# 保存路径名:
# savepath_csv = r"D:\基金数据\最新数据\Data_after3_3_18.csv" # 写死
# savepath_txt = r"D:\基金数据\最新数据\Data_after3_3_18.txt" # 写死
from datetime import datetime

today = datetime.now()

savepath_csv = r"D:\基金数据\最新数据\Data_after4.5_{}_{}_{}.csv".format(today.year,today.month,today.day) # 自动获取
savepath_txt = r"D:\基金数据\最新数据\Data_after4.5_{}_{}_{}.txt".format(today.year,today.month,today.day) # 自动获取
print(savepath_csv)
print(savepath_txt)

df_table1.to_csv(savepath_csv,encoding='GB18030')
df_table1.to_csv(savepath_txt,sep='\t',index=False,encoding='GB18030')

###################################

# A: 使用时间参数自动获取路径名
from datetime import datetime

today = datetime.now()

path = r"D:\基金数据\最新数据\Data_after4.5_{}_{}_{}.txt".format(today.year,today.month,today.day) # 自动获取
# 要求输入列为：
# SHORTNAME	FCODE	MGRID	MGRNAME	SHARP1	SHARP2	STDDEV1	STDDEV2	MAXRETRA1	GP	ZQ	HB	JZC	Week_up	Week_avg_up	Week_hs300_up	Week_rank	Week_competitors	Month_up	Month_avg_up	Month_hs300_up	Month_rank	Month_competitors	Year_up	Year_avg_up	Year_hs300_up	Year_rank	Year_competitors	NowYear_up	NowYear_avg_up	NowYear_hs300_up	NowYear_rank	NowYear_competitors	TwoYear_up	TwoYear_avg_up	TwoYear_hs300_up	TwoYear_rank	TwoYear_competitors	ThreeYear_up	ThreeYear_avg_up	ThreeYear_hs300_up	ThreeYear_rank	ThreeYear_competitors	FiveYear_up	FiveYear_avg_up	FiveYear_hs300_up	FiveYear_rank	FiveYear_competitors	fundStocks_GPDM_0	fundStocks_GPJC_0	fundStocks_JZBL_0	fundStocks_PCTNVCHG_0	fundStocks_GPDM_1	fundStocks_GPJC_1	fundStocks_JZBL_1	fundStocks_PCTNVCHG_1	fundStocks_GPDM_2	fundStocks_GPJC_2	fundStocks_JZBL_2	fundStocks_PCTNVCHG_2	fundStocks_GPDM_3	fundStocks_GPJC_3	fundStocks_JZBL_3	fundStocks_PCTNVCHG_3	fundStocks_GPDM_4	fundStocks_GPJC_4	fundStocks_JZBL_4	fundStocks_PCTNVCHG_4	fundStocks_GPDM_5	fundStocks_GPJC_5	fundStocks_JZBL_5	fundStocks_PCTNVCHG_5	fundStocks_GPDM_6	fundStocks_GPJC_6	fundStocks_JZBL_6	fundStocks_PCTNVCHG_6	fundStocks_GPDM_7	fundStocks_GPJC_7	fundStocks_JZBL_7	fundStocks_PCTNVCHG_7	fundStocks_GPDM_8	fundStocks_GPJC_8	fundStocks_JZBL_8	fundStocks_PCTNVCHG_8	fundStocks_GPDM_9	fundStocks_GPJC_9	fundStocks_JZBL_9	fundStocks_PCTNVCHG_9	BaoTuan	Payback	Days
df = pd.read_table(path,converters={'FCODE':str,'MGRID':str},encoding='GB18030')

print(path)


df_test = df.copy()
df.head(5)

# 去除表中 '--' 值，然后算四分位数

df9 = df.copy()

condition1 = df9['jd_20_4'] != '--'
condition2 = df9['jd_20_3'] != '--'
condition3 = df9['jd_20_2'] != '--'
condition4 = df9['jd_20_1'] != '--'

condition5 = df9['jd_19_4'] != '--'
condition6 = df9['jd_19_3'] != '--'
condition7 = df9['jd_19_2'] != '--'
condition8 = df9['jd_19_1'] != '--'

condition9 = df9['nd_20'] != '--'
condition10 = df9['nd_19'] != '--'
condition11 = df9['nd_18'] != '--'
condition12 = df9['nd_17'] != '--'
condition13 = df9['nd_16'] != '--'
condition14 = df9['nd_15'] != '--'
condition15 = df9['nd_14'] != '--'
condition16 = df9['nd_13'] != '--'

con = [condition1,condition2,condition3,condition4,condition5,condition6,condition7,condition8,condition9,condition10,
      condition11,condition12,condition13,condition14,condition15,condition16]
# df9_ = [df9_jd_20_4,df9_jd_20_3,df9_jd_20_2,df9_jd_20_1,
#        df9_jd_19_4,df9_jd_19_3,df9_jd_19_2,df9_jd_19_1,
#        nd_20,nd_19,nd_18,nd_17,nd_16,nd_15,nd_14,nd_13]

df9_=[]
for i in range(16):
    df9_.append(df9[con[i]])


# 将每列数据的百分制转为小数
df9_jd_20_4 = df9_[0].jd_20_4.str.strip('%').astype(float)/100
df9_jd_20_3 = df9_[1].jd_20_3.str.strip('%').astype(float)/100
df9_jd_20_2 = df9_[2].jd_20_2.str.strip('%').astype(float)/100
df9_jd_20_1 = df9_[3].jd_20_1.str.strip('%').astype(float)/100

df9_jd_19_4 = df9_[4].jd_19_4.str.strip('%').astype(float)/100
df9_jd_19_3 = df9_[5].jd_19_3.str.strip('%').astype(float)/100
df9_jd_19_2 = df9_[6].jd_19_2.str.strip('%').astype(float)/100
df9_jd_19_1 = df9_[7].jd_19_1.str.strip('%').astype(float)/100

df9_nd_20 = df9_[8].nd_20.str.strip('%').astype(float)/100
df9_nd_19 = df9_[9].nd_19.str.strip('%').astype(float)/100
df9_nd_18 = df9_[10].nd_18.str.strip('%').astype(float)/100
df9_nd_17 = df9_[11].nd_17.str.strip('%').astype(float)/100
df9_nd_16 = df9_[12].nd_16.str.strip('%').astype(float)/100
df9_nd_15 = df9_[13].nd_15.str.strip('%').astype(float)/100

df9_jd_20 = [df9_jd_20_4,df9_jd_20_3,df9_jd_20_2,df9_jd_20_1]
df9_jd_19 = [df9_jd_19_4,df9_jd_19_3,df9_jd_19_2,df9_jd_19_1]
df9_nd    = [df9_nd_20,df9_nd_19,df9_nd_18,df9_nd_17,df9_nd_16,df9_nd_15]

# 每个四个为一组

df9_jd_20_q = []
for i in range(len(df9_jd_20)):
    tmp = []
    tmp.append(round(df9_jd_20[i].quantile(0.5),3))
    tmp.append(round(df9_jd_20[i].quantile(0.7),3))
    tmp.append(round(df9_jd_20[i].quantile(0.9),3))
    tmp.append(round(df9_jd_20[i].quantile(1),3))
    df9_jd_20_q.append(tmp)
    
df9_jd_19_q = []
for i in range(len(df9_jd_19)):
    tmp = []
    tmp.append(round(df9_jd_19[i].quantile(0.5),3))
    tmp.append(round(df9_jd_19[i].quantile(0.7),3))
    tmp.append(round(df9_jd_19[i].quantile(0.9),3))
    tmp.append(round(df9_jd_19[i].quantile(1),3))
    df9_jd_19_q.append(tmp)
    
df9_nd_q = []
for i in range(len(df9_nd)):
    tmp = []
    tmp.append(round(df9_nd[i].quantile(0.5),3))
    tmp.append(round(df9_nd[i].quantile(0.7),3))
    tmp.append(round(df9_nd[i].quantile(0.9),3))
    tmp.append(round(df9_nd[i].quantile(1),3))
    df9_nd_q.append(tmp)


def getFloatData(data):
    if data == '--':
        return float(-1)
    res = float(data.strip('%'))/100
    return res


# 部分特征参与排序
for i in range(len(df['FCODE'])):
    count = 0
    
    count += 1 -(df['jd_20_4_rank'] / len(df['FCODE'])) * 1 * 0.8
    count += 1 -(df['jd_20_3_rank'] / len(df['FCODE'])) * 1 * 0.8
    count += 1 -(df['jd_20_2_rank'] / len(df['FCODE'])) * 1 * 0.8
    count += 1 -(df['jd_20_1_rank'] / len(df['FCODE'])) * 1 * 0.8
   
    count += 1 -(df['jd_19_4_rank'] / len(df['FCODE'])) * 1 * 0.8
    count += 1 -(df['jd_19_3_rank'] / len(df['FCODE'])) * 1 * 0.8
    count += 1 -(df['jd_19_2_rank'] / len(df['FCODE'])) * 1 * 0.8
    count += 1 -(df['jd_19_1_rank'] / len(df['FCODE'])) * 1 * 0.8
    
#     count += 1 -(df['nd_20_rank'] / len(df['FCODE'])) * 1
#     count += 1 -(df['nd_19_rank'] / len(df['FCODE'])) * 1    
    count += 1 -(df['nd_18_rank'] / len(df['FCODE'])) * 1    
    count += 1 -(df['nd_17_rank'] / len(df['FCODE'])) * 1
    count += 1 -(df['nd_16_rank'] / len(df['FCODE'])) * 1    
    count += 1 -(df['nd_15_rank'] / len(df['FCODE'])) * 1    
#     count += 1 -(df['nd_14_rank'] / len(df['FCODE'])) * 1
#     count += 1 -(df['nd_13_rank'] / len(df['FCODE'])) * 1
    
    count += (1 -(df['收益回撤比_rank'] / len(df['FCODE'])) * 1) * 1.1
    count += 1 -(df['SHARP1_rank'] / len(df['FCODE'])) * 1    
    count += 1 -(df['SHARP2_rank'] / len(df['FCODE'])) * 1    
    count += 1 -(df['Days_rank'] / len(df['FCODE'])) * 1  
    count += 1 -(df['Payback_rank'] / len(df['FCODE'])) * 1  
    
    # 注重回撤版本
    if float(df['MAXRETRA1'][i]) != -1:
        count += (df['MAXRETRA1_rank'] / len(df['FCODE'])) * 1 * 1.1
    else:
        count += 0
    
    # 原始版本
    # if float(df['MAXRETRA1'][i]) != -1:
    #     count += (df['MAXRETRA1_rank'] / len(df['FCODE'])) * 1
    # else:
    #     count += 0
    
    if float(df['STDDEV1'][i]) != -1:
        count += (df['STDDEV1_rank'] / len(df['FCODE'])) * 1 
    else:
        count += 0

    if float(df['STDDEV2'][i]) != -1:
        count += (df['STDDEV2_rank'] / len(df['FCODE'])) * 1
    else:
        count += 0        
    
df.insert(2,'count',count)

# 保存路径名:
# savepath_csv = r"D:\基金数据\最新数据\Data_after3_3_18.csv" # 写死
# savepath_txt = r"D:\基金数据\最新数据\Data_after3_3_18.txt" # 写死
from datetime import datetime

today = datetime.now()

savepath_csv = r"D:\基金数据\最新数据\Data_after5.1_{}_{}_{}_弱化季度版.csv".format(today.year,today.month,today.day) # 自动获取
savepath_txt = r"D:\基金数据\最新数据\Data_after5.1_{}_{}_{}_弱化季度版.txt".format(today.year,today.month,today.day) # 自动获取
print(savepath_csv)
print(savepath_txt)

df.to_csv(savepath_csv,encoding='GB18030')
df.to_csv(savepath_txt,sep='\t',index=False,encoding='GB18030')


