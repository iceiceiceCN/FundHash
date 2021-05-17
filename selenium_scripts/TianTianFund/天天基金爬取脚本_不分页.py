import os
import time
import codecs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import xlrd
import xlwt
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import random
from myinit import *
from chromeset import *


global info  # 全局变量
# driver = webdriver.Chrome(executable_path=r'D:\Anaconda3\chromedriver.exe',chrome_options=chrome_options)
# driver.set_window_size(1000,30000)


def getManagers(url, filename,driver,nums):
    def isExist(xpath):
        try:
            driver.find_element_by_xpath(xpath)
            return True
        except:
            print("未找到 xpath 元素")
            return False
    try:
        global info  # 全局变量
        basePath = getworkdir() + '/data/'

        if not os.path.exists(basePath):
            os.makedirs(basePath)
        scenicFile = os.path.join(basePath, filename)

        if not os.path.exists(scenicFile):
            info = codecs.open(scenicFile, 'w', 'utf-8')
        else:
            info = codecs.open(scenicFile, 'a', 'utf-8')

        driver.get(url)
        time.sleep(5)

        exit_flag = False
        for j in range(1,2):
            time.sleep(5)

            if isExist(xpath='/html/body/div[14]') == True:
                # driver.find_element_by_xpath('/html/body/div[15]/span/a').click()
                time.sleep(60)
                print('已点击刷新')

            time.sleep(5)            

            for i in range(1, nums+1):
                
                
                xpath_code = '//*[@id="dbtable"]/tbody/tr[' + str(i) + ']/td[3]/a'
                xpath_name = '//*[@id="dbtable"]/tbody/tr[' + str(i) + ']/td[4]/a'

                flag_code = isExist(xpath_code)
                flag_name = isExist(xpath_name)

                if flag_code == False or flag_name == False:
                    continue
                elems_name = driver.find_element_by_xpath(xpath_name)
                elems_code = driver.find_element_by_xpath(xpath_code)

                print(elems_name.text + '\t' + elems_code.text + '\r\n')
                info.writelines(elems_name.text + '\t' + elems_code.text + '\r\n')
                print('已经写入' + str(i) + '条信息...\t')

            time.sleep(5)

            # elems_input = driver.find_element_by_xpath('//*[@id="pnum"]')
            # elems_input.send_keys(str(j+1))
            # print("转到" + str(j+1)+ "页")
            # driver.find_element_by_xpath('//*[@id="pagebar"]/input[2]').click()

            # if exit_flag == True:
            #     break
            # time.sleep(10)
    except Exception as e:
        print("Error: ", e)


def main():
    driver = set_Chrome()
    global info
    numslist = [4081,1497,1927,159,331,176,1105]
    gp_url_0 = r'http://fund.eastmoney.com/data/fundranking.html#thh;c0;r;s6yzf;pn10000;ddesc;qsd20200215;qed20210215;qdii;zq;gg;gzbd;gzfs;bbzt;sfbb' # 混合
    gp_url_1 = r'http://fund.eastmoney.com/data/fundranking.html#tgp;c0;r;s6yzf;pn50;ddesc;qsd20200215;qed20210215;qdii;zq;gg;gzbd;gzfs;bbzt;sfbb' # 股票
    gp_url_2 = r'http://fund.eastmoney.com/data/fundranking.html#tzq;c0;r;s1nzf;pn50;ddesc;qsd20200215;qed20210215;qdii;zq;gg;gzbd;gzfs;bbzt;sfbb' # 债券
    gp_url_3 = r'http://fund.eastmoney.com/data/fundranking.html#tfof;c0;r;s1nzf;pn50;ddesc;qsd20200215;qed20210215;qdii;zq;gg;gzbd;gzfs;bbzt;sfbb' # FOF
    gp_url_4 = r'http://fund.eastmoney.com/data/fundranking.html#tlof;c0;r;s1nzf;pn50;ddesc;qsd20200215;qed20210215;qdii;zq;gg;gzbd;gzfs;bbzt;sfbb' # LOF
    gp_url_5 = r'http://fund.eastmoney.com/data/fundranking.html#tqdii;c0;r;s1nzf;pn50;ddesc;qsd20200215;qed20210215;qdii;zq;gg;gzbd;gzfs;bbzt;sfbb' # QDII
    gp_url_6 = r'http://fund.eastmoney.com/data/fundranking.html#tzs;c0;r;s1nzf;pn50;ddesc;qsd20200215;qed20210215;qdii;zq;gg;gzbd;gzfs;bbzt;sfbb' # 指数型
    gp_urls = [gp_url_0,gp_url_1,gp_url_2,gp_url_3,gp_url_4,gp_url_5,gp_url_6]
    filenames = ['天天基金混合型基金数据.txt','天天基金股票型基金数据.txt','天天基金债券型基金数据.txt','天天基金FOF型基金数据.txt','天天基金LOF型基金数据.txt','天天基金QDII型基金数据.txt','天天基金指数型基金数据.txt']
    
    for i in range(len(filenames)):
        nums = numslist[i]
        gp_url = gp_urls[i]
        filename = filenames[i]
    # filename = '天天基金指数型基金数据.txt'
        getManagers(gp_url, filename,driver,nums)
        print("End")
    info.close()
    driver.close()

    # 得到目标区域元素
    # 复制元素
    # 输入到文本文件中


main()


"""
股票型按钮
/html/body/div[2]/div[3]/div[1]/div[1]/p/a[2]

/html/body/div[15]/span/a
混合型按钮
/html/body/div[2]/div[3]/div[1]/div[1]/p/a[3]

3年以上按钮
/html/body/div[2]/div[3]/div[1]/div[3]/p/a[4]
"""
