import re
import requests
import datetime

from 杂项工具.myTools import cookieProcessing, getNewestService

cookie = 'PHPSESSID=6a36028dafed5e8be60e3444c7dbf9cc;' \
               'AUC=a%3A2%3A%7Bs%3A5%3A%22token%22%3Bs%3A84%3A' \
               '%22MjM2NDE1NzMwfDE2MDYzNTAxMjF8d2VueHVodWl8YWQ0ZmZlMTY2MjEwMjM0NGM3MDJmOTY5MWJkZjAyMTY%3D%22%3Bs%3A2' \
               '%3A%22_s%22%3Bs%3A32%3A%2225b5ce6ec203d83acc6fff0ff8d5551a%22%3B%7D; AreaMoneyFlag=-1'
cookies = cookieProcessing(cookie)


# 封禁记录爬虫
def cloSpider(Game, Platform, beginTime, endTime):
    Server = int(getNewestService(Game,Platform,5))
    # while True:
    print(Server)
    urlC = 'http://t.4399data.com/oss/?r=ban/record&platform='+Platform+'&p='+ Platform +'&game='+Game+'&channel=&server=S'+str(Server)+'&StartTime='+beginTime+'&EndTime='+endTime+'&BanType=all&BanAdmin=&Data=&role_id=&account_name=&device=&Reason=&getListForAjax=1&page=1&length=100000'
    cloBox = []
    data = requests.get(url=urlC, cookies=cookies).text.encode('utf-8').decode('unicode_escape')
    # 正则清洗
    # 分装
    # 返回数个要素
    # Server = Server-1
    data = data.split(',')
    for i in range(len(data)):
        print(data[i])
    return cloBox


# 登录日志爬虫+混合数据产出
def loginSpider(cloBox):
    urlL = ''
    loginBox = []
    fixData = []
    data = requests.get(url=urlL, cookies=cookies).text
    # 正则清洗
    # 分装
    # 混合产出
    # 返回
    return fixData

cloSpider('tjb', 'mix_mob1', '2021-02-01', '2021-03-12',)