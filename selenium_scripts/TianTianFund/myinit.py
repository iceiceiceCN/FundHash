import os
import requests
import random
import telnetlib


#获得当前工作目录 
def getworkdir():
    os.chdir(os.path.dirname(__file__)) 
    print("当前工作路径为：" + str(os.getcwd()))
    path_ = os.getcwd()
    return path_


def getIPs():
    # 公开代理
    # url = 'http://api.superfastip.com/api/ip?tid=09a25706edeba5b6f30eeca92098c4c5&num=20&port=&an=12&type=0'
    
    # 动态代理
    url = 'http://api.superfastip.com/api/ip?tid=3398ba003955f713979d5a189d5e9b64&limit_second=120&type=0'
    resIPs = requests.get(url).text
    resIPs = str(resIPs)
    resIPs = resIPs.strip().split('\r\n')
    global lenIPs
    lenIPs = len(resIPs)
    return resIPs

# 随机挑选一个IP
def choiceIP():
    global resIP
    resIP = random.choice(getIPs())
    return resIP

# 得到的IP池可能有无效IP，所以要进行判断
def test_ip():
    # 每次挑选一个ip出来测试
    resIP = choiceIP()
    data = []
    getworkdir()
    for line in open("data/fwip.txt","r"): #设置文件对象并读取每一行文件
        line = line.strip("\n")
        data.append(line)
    print("当前废弃 ip 池为：")
    print(data)
    while resIP in data:
        print("ip 已被占用，正在重新尝试...")
        resIP = choiceIP()
    ip,port = resIP.split(':')[0],resIP.split(':')[1]
    try:
        telnetlib.Telnet(ip,port,timeout=2)
        print("代理 ip 有效！")
        with open('data/fwip.txt','a+') as f:          #设置文件对象
            f.write(resIP + '\n')                 #将字符串写入文件中
        return True,resIP
    except:
        print("代理 ip 无效！")
        return False,resIP

# 遍历IP池，找到可用IP
def retry():
    flag,resIP = test_ip()
    while flag == False:
        flag,resIP = test_ip()
    print("得到 ip 为:" + str(resIP))
    return resIP

