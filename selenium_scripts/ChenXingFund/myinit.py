import requests
import random
import telnetlib
def getIPs():
    # url = 'http://api.superfastip.com/api/ip?tid=09a25706edeba5b6f30eeca92098c4c5&num=20&port=&an=12&type=0'
    url = 'http://api.superfastip.com/api/ip?tid=3398ba003955f713979d5a189d5e9b64&limit_second=120&type=0'
    # 第二个为动态代理
    resIPs = requests.get(url).text
    resIPs = str(resIPs)
    resIPs = resIPs.strip().split('\r\n')
    global lenIPs
    lenIPs = len(resIPs)
    # print(res.text)
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
    for line in open("fwip.txt","r"): #设置文件对象并读取每一行文件
        line = line.strip("\n")
        data.append(line)
    print(data)
    while resIP in data:
        print("IP已被占用，正在重新尝试")
        resIP = choiceIP()
    ip,port = resIP.split(':')[0],resIP.split(':')[1]
    try:
        telnetlib.Telnet(ip,port,timeout=2)
        print("代理ip有效！")
        with open('fwip.txt','a+') as f:    #设置文件对象
            f.write('\n' + resIP)                 #将字符串写入文件中
        return True,resIP
    except:
        print("代理ip无效！")
        return False,resIP

# 遍历IP池，找到可用IP
def retry():
    flag,resIP = test_ip()
    while flag == False:
        flag,resIP = test_ip()
    
    return resIP

