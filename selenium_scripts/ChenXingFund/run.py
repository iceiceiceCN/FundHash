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


def isExist(xpath, driver):
    try:
        driver.find_element_by_xpath(xpath)
        return True
    except:
        return False

def initWeb(url, driver):
    driver.get(url)
    time.sleep(1)

def restartWeb(url,driver):
    print("restartWeb(url,driver) ---- 开始重置页面和驱动")
    driver.quit()
    # 抓取50个后重置IP
    driver = set_Chrome()
    driver.get(url)
    time.sleep(1)
    return driver

def getManagers(url, excelpath, driver):
    try:
        initWeb(url,driver)
        time.sleep(30)
        nowIP = requests.get('http://httpbin.org/ip').text
        print(nowIP)

        wtbook = xlwt.Workbook(encoding = 'ascii')
        #新增一个sheet工作表
        sheet = wtbook.add_sheet('Sheet1',cell_overwrite_ok=True)
        #写入数据头
        headlist = [u'code',u'url']
        row = 0
        col = 0

        for head in headlist:
            sheet.write(row,col,head)
            col += 1

        r , c = 1 , 0
        exit_flag = False

        for _ in range(1, 478):
            for i in range(2, 27):
                c = 0       
                print("(1/5) 开始定位 xpth_name 与 xpath_years 元素\t")
                xpath_code = '//*[@id="ctl00_cphMain_gridResult"]/tbody/tr['+str(i)+']/td[3]/a'
                xpath_url = '//*[@id="ctl00_cphMain_gridResult"]/tbody/tr['+str(i)+']/td[4]/a'
                xpath_class = '//*[@id="ctl00_cphMain_gridResult"]/tbody/tr['+str(i)+']/td[5]'
                
                

                elem_code = driver.find_element_by_xpath(xpath_code)
                elem_url = driver.find_element_by_xpath(xpath_url).get_attribute("href")
                elem_class = driver.find_element_by_xpath(xpath_class)


                print("(2/5) 正在读取 " + str(elem_code.text) + " 号的信息")
                print("(3/5) 此时序号为 " + str(i))

                sheet.write(r,c,elem_code.text)
                c += 1

                sheet.write(r,c,elem_url)
                c += 1

                sheet.write(r,c,elem_class.text)
                c += 1

                wtbook.save(excelpath)

                print('(4/5) 已写入 ' + str(i) + ' 条信息...'+ '\t')
                r += 1

            xpath_nextpage = '//*[@id="ctl00_cphMain_AspNetPager1"]/a[12]'
            driver.find_element_by_xpath(xpath_nextpage).click()
            print("(5/5) 已切换至初始页面，准备开始新一轮爬取\t")
            time.sleep(2)
        wtbook.save(excelpath)
    except Exception as e:
        print("Error: ", e)


def main():
    driver = set_Chrome()
    url = r'https://www.morningstar.cn/quickrank/default.aspx'
    excelpath = r'晨星网数据.xls'
    getManagers(url, excelpath, driver)
    print("End")
    driver.close()

    # 得到目标区域元素
    # 复制元素
    # 输入到文本文件中


main()


"""
股票型按钮
/html/body/div[2]/div[3]/div[1]/div[1]/p/a[2]

混合型按钮
/html/body/div[2]/div[3]/div[1]/div[1]/p/a[3]

3年以上按钮
/html/body/div[2]/div[3]/div[1]/div[3]/p/a[4]
"""
