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
    # 点击 3年按钮 -> 股票型 -> 混合型
    driver.find_element_by_xpath(
        '/html/body/div[6]/div[2]/div/div[2]').click()  # 关闭广告
    time.sleep(1)

    # 3年按钮
    driver.find_element_by_xpath(
        '/html/body/div[2]/div[3]/div[1]/div[3]/p/a[4]').click()
    time.sleep(1)

    # 股票型按钮
    # driver.find_element_by_xpath(
    #     '/html/body/div[2]/div[3]/div[1]/div[1]/p/a[2]').click()
    
    # 混合型按钮
    driver.find_element_by_xpath(
        '/html/body/div[2]/div[3]/div[1]/div[1]/p/a[3]').click()

    time.sleep(1)
    
    # 滚动页面加载js元素
    for _ in range(60):
        driver.execute_script("window.scrollBy(0,5000)")
        time.sleep(1)

def getManagers(url, excelpath, driver):
    try:
        initWeb(url,driver)
        nowIP = requests.get('http://httpbin.org/ip').text
        print(nowIP)

        wtbook = xlwt.Workbook(encoding = 'ascii')
        #新增一个sheet工作表
        sheet = wtbook.add_sheet('Sheet1',cell_overwrite_ok=True)
        #写入数据头
        headlist = [u'序号',u'姓名',u'年份',u'从业年均回报']
        row = 0
        col = 0

        for head in headlist:
            sheet.write(row,col,head)
            col += 1

        r , c = 1 , 0
        exit_flag = False
        for i in range(100, 200):
            c = 0       
            time.sleep(1)
            print("开始定位 xpth_name 与 xpath_years 元素\t")
            xpath_No = '/html/body/div[2]/div[3]/div[3]/table/tbody/tr[' + str(i) + ']/td[1]'
            xpath_name = '/html/body/div[2]/div[3]/div[3]/table/tbody/tr[' + str(i) + ']/td[3]/a'
            xpath_years = '/html/body/div[2]/div[3]/div[3]/table/tbody/tr[' + str(i) + ']/td[5]'

            isExist_name_count = 0
            isExist_name_falg = 0
            for m in range(5):
                if isExist(xpath_name,driver) == True:
                    pass
                else:
                    isExist_name_count += 1
                    if isExist_name_count == 3:
                        isExist_name_falg = 1
                        continue
            
            if isExist_name_falg == 1:
                print("---- isExist_name_falg 跳出 ----")
                continue

                # break
            
            elem_No = driver.find_element_by_xpath(xpath_No)
            elems_name = driver.find_element_by_xpath(xpath_name)
            elems_years = driver.find_element_by_xpath(xpath_years)
            print("正在读取 " + str(elem_No.text) + " 号的信息")
            print("此时序号为 " + str(i))

            sheet.write(r,c,elem_No.text)
            c += 1

            sheet.write(r,c,elems_name.text)
            c += 1

            sheet.write(r,c,elems_years.text)
            c += 1

            # time.sleep(2)
            actions = ActionChains(driver)
            manager_name = driver.find_element_by_xpath(xpath_name)
            # 在新的标签页打开“经理详情”页面
            actions.key_down(Keys.CONTROL).click(manager_name).key_up(Keys.CONTROL).perform()
            print("已打开经理详情页面\t")
            # time.sleep(1)
            # 切换到新标签页
            driver.switch_to.window(driver.window_handles[-1])
            print("已切换至经理详情页面\t")
            time.sleep(1)

            xpath_payback = '//*[@id="experience"]/div[3]/div[2]/table/tbody/tr[3]/td[4]/span'

            isExist_payback_count = 0
            isExist_payback_falg = 0
            for t in range(5):
                if isExist(xpath_payback,driver) == True:
                    pass
                else:
                    isExist_payback_count += 1
                    if isExist_payback_count == 3:
                        isExist_payback_falg = 1
                        continue
            
            if isExist_payback_falg == 1:
                driver.close()
                print("已关闭经理详情页面\t")

                # 不关闭，要移动到上一个页面，我们要移动句柄，否则会报错找不到:target window already closed
                driver.switch_to.window(driver.window_handles[0])
                print("已切换至初始页面，准备开始新一轮爬取\t")

                time.sleep(1)
                print("---- isExist_payback_falg 跳出 ----")
                continue

            elems_payback = driver.find_element_by_xpath(xpath_payback)
            print("已定位到 xpath_payback 元素\t")

            sheet.write(r,c,elems_payback.text)
            wtbook.save(excelpath)

            print('已写入 ' + str(i) + ' 条信息...'+ '\t')
            time.sleep(1)
            driver.close()
            print("已关闭经理详情页面\t")
            # 不关闭，要移动到上一个页面，我们要移动句柄，否则会报错找不到:target window already closed
            driver.switch_to.window(driver.window_handles[0])
            print("已切换至初始页面，准备开始新一轮爬取\t")
            time.sleep(1)
            r += 1

            time.sleep(1)

        wtbook.save(excelpath)
    except Exception as e:
        print("Error: ", e)


def main():
    driver = set_Chrome()
    url = r'https://www.howbuy.com/fund/manager/'
    excelpath = r'howbuy_混合型_100_200.xls'
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
