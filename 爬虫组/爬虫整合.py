# 将之前验证可用的爬虫们进行整理与合并,提高便捷性
import requests


def spiderFactory(url, cookies):
    # requests链接
    data_R = requests.get(url,cookies).text
    # 正则筛选_根据不同需求

    # 数据打包
    dataPackage = object
    pass

