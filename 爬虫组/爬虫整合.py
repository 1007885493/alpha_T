# 将之前验证可用的爬虫们进行整理与合并,提高便捷性
import datetime

import requests
import re
from 杂项工具.myTools import cookieProcessing

# 全局变量
oneday = datetime.timedelta(days=1)
today = datetime.date.today()
yesterday = today - oneday
cookie = 'PHPSESSID=6a36028dafed5e8be60e3444c7dbf9cc; ' \
         'AUC=a%3A2%3A%7Bs%3A5%3A%22token%22%3Bs%3A84%3A' \
         '%22MjM2NDE1NzMwfDE2MDYzNTAxMjF8d2VueHVodWl8YWQ0ZmZlMTY2MjEwMjM0NGM3MDJmOTY5MWJkZjAyMTY%3D%22%3Bs%3A2%3A' \
         '%22_s%22%3Bs%3A32%3A%2225b5ce6ec203d83acc6fff0ff8d5551a%22%3B%7D; AreaMoneyFlag=-1 '
cookies = cookieProcessing(cookie)
GameBox = ['tjb', 'zsgl', 'tsxf']
BranchBox = [['mix_mob1', 'mix_mob1ios', 'mix_mob2', 'mix_mob3', 'mix_mailiang', 'mix_4ios', 'mix_4ios2', ],
             ['android_cn', 'ios_cn', ],
             ['mix_mob1', 'ios_cn', 'mix_mob2', ],
             ]


# 筛选表,根据state返回已过滤的粗数据
# 返回格式统一的数据包以供分析
def filterBox(state, flag) :
    # 根据游戏名获取最新区服
    # ServiceNum = balabala
    # 返回的数据包
    dataPackage = []
    dataPackageBox = []
    if state == 'chat' :
        dataPackage = filter_chat(cookies, GameBox[flag], BranchBox[flag][0])
    if state == 'ban' :
        dataPackage = filter_ban(cookies)
    if state == 'login' :
        dataPackage = filter_login(cookies)

    return dataPackageBox


# 聊天日志
def filter_chat(cookies, Game, Branch, ServiceNum, time, num) :
    url_sd = 'http://t.4399data.com/report/?r=log/gameLog/index&platform=' + Branch + '&game=' + Game + '&p=' + Branch + '&channel=&server=S' + ServiceNum + '&tab=&begin=' + today.isoformat() + '%20' + time + ':00&end=' + today.isoformat() + '%2023:59:59&lock=on&type=chat&account_name=&role_id=&target_role_id=&role_name=&msg=&user_ip=&did=&min_dim_level=&max_dim_level=&chatType=&contentType=&dataSource=slave&banTypeSel=all&gsInfo=0&getListForAjax=1&page=1&length=' + num

    data_sd = requests.get(url=url_sd, cookies=cookies).text.encode('utf-8').decode(
        'unicode_escape').replace('{', '').split('},')
    data_dirt = {}
    data_outPut = []
    for i in range(len(data_sd)) :
        strT = str(data_sd[i]).replace('"', '').split(',')
        for line in range(len(strT)) :
            try :
                key, value = strT[line].split(':', 1)
                data_dirt[key] = value
            except :
                continue
        try :
            # print(data_dirt)
            data_outPut.append([data_dirt['banType'], data_dirt['server_id'],
                                data_dirt['account_name'], data_dirt['happend_time'],
                                data_dirt['role_id'], data_dirt['role_name'],
                                data_dirt['msg']])
        except :
            continue

    return data_outPut


# 登录日志
def filter_login(cookies, Game, Branch, ServiceNum, time, num) :
    url_batch = 'http://t.4399data.com/report/?r=log/gameLog/index&platform=' + Branch + '&game=' + Game + '&p=' + Branch + '&channel=&server=S' + ServiceNum + '&tab=&begin=' + today.isoformat() + '%2000:00:00&end=' + today().isoformat() + '%2023:59:59&lock=on&type=login&user_ip=&device=&did=&screen=&account_name=&role_id=&role_name=&version_not_in=&is_remove_role_id=on&dataSource=slave&gsInfo=0&getListForAjax=1&page=1&length=' + num
    # 登录日志爬取
    data_batch = requests.get(url=url_batch, cookies=cookieProcessing(cookies)).text.encode('utf-8').decode(
        'unicode_escape')
    # 数据粗筛选
    data_batch = data_batch[data_batch.find('"data":[') :data_batch.find('"count":"')]
    data_batch = data_batch.split('}')
    data_batch.remove(data_batch[len(data_batch) - 1])

    for i in range(len(data_batch)) :
        strT = str(data_batch[i]).replace('\"', '').replace('data:[{', '').split(',')
        data_dirt = {}
        for line in range(len(strT)) :
            try :
                key, value = strT[line].split(':', 1)
                data_dirt[key] = value
            except :
                continue
    return data_dirt


# 封禁记录-身份信息\游戏简称\专区\区服\时间\数量
def filter_ban(cookies, Game, Branch, ServiceNum, time, num) :
    url_sd = 'http://t.4399data.com/report/?r=log/gameLog/index&platform=' + Branch + '&game=' + Game + '&p=' + Branch + '&channel=&server=S' + ServiceNum + '&tab=&begin=' + today.isoformat() + '%20' + time + ':00&end=' + today.isoformat() + '%2023:59:59&lock=on&type=chat&account_name=&role_id=&target_role_id=&role_name=&msg=&user_ip=&did=&min_dim_level=&max_dim_level=&chatType=&contentType=&dataSource=slave&banTypeSel=all&gsInfo=0&getListForAjax=1&page=1&length=' + num
    data_sd = requests.get(url=url_sd, cookies=cookies).text.encode('utf-8').decode('unicode_escape').replace('{',
                                                                                                              '').split(
        '},')
    data_dirt = {}
    for i in range(len(data_sd)) :
        strT = str(data_sd[i]).replace('"', '').split(',')
        for line in range(len(strT)) :
            try :
                key, value = strT[line].split(':', 1)
                data_dirt[key] = value
            except :
                continue
    return data_dirt


# 新服获取
def getNewestService(Game, Branch, num) :
    url = 'http://t.4399data.com/home/?r=index/getServer&game=' + Game + '&platform=' + Branch
    nsD = requests.get(url=url, cookies=cookieProcessing(cookies)).text.encode('utf-8').decode('unicode_escape').split(
        '>')

    i = 3
    # print(nsD)
    nsOutput = nsD[i][1 :num]

    while nsOutput.find('AREA') != -1 or nsOutput.find('ADMIN') != -1 or nsOutput.find('LOGIN') != -1 :
        i = i + 2
        nsOutput = nsD[i][1 :num]
    return nsOutput
