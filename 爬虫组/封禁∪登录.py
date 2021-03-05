import re
import requests
import datetime


from 杂项工具.myTools import cookieProcessing



cookie = ''
cookies = cookieProcessing(cookie)

# 封禁记录爬虫
def cloSpider():
    urlC = ''
    cloBox = []
    data = requests.get(url=urlC, cookies=cookies).text
    # 正则清洗
    # 分装
    # 返回数个要素
    return cloBox


# 登录日志爬虫
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



