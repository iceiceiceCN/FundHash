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

def set_Chrome():
    # 有头 = 1
    # 无头 = 0
    headchoise = 1

    # 得到IP
    proxy = retry()
    option_proxy = '--proxy-server=http://' + str(proxy)
    print(option_proxy)

    prefs = {'profile.managed_default_content_settings.images': 2}

    # Chrome Headless（无头模式）下Element is not clickable,则添加一下四行代码
    chrome_nohead_options = Options()
    chrome_ips_options = Options()

    # 更换头部
    user_agent = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) " +
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36"
    )

    chrome_nohead_options.add_argument('user-agent=%s'%user_agent)
    chrome_nohead_options.add_argument('--headless')
    chrome_nohead_options.add_argument("--window-size=1920,1080")
    chrome_nohead_options.add_argument("--start-maximized")
    # chrome_nohead_options.add_argument(option_proxy)
    
    # chrome_ips_options.add_experimental_option('prefs',prefs)
    chrome_ips_options.add_argument('user-agent=%s'%user_agent)
    # chrome_ips_options.add_argument(option_proxy)

    if headchoise == 1:
        # 有头模式
        driver = webdriver.Chrome(executable_path=r'D:\Anaconda3\chromedriver.exe',chrome_options=chrome_ips_options)
    elif headchoise == 0:
        # 无头模式
        driver = webdriver.Chrome(executable_path=r'D:\Anaconda3\chromedriver.exe',chrome_options=chrome_nohead_options)
    
    return driver