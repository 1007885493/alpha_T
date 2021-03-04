#从封禁记录爬虫中获取区服和uid

from 爬虫组.爬虫整合 import getNewestService
#根据区服量循环获取指定时间内的封禁记录(服务器-rid-封禁操作者-解禁时间),并根据解禁时间来排除已解除的封禁项
def getBanInfo():
    banInfo = []
    return banInfo
#上一步骤的数据(服务器-rid)作为参数传入登录日志爬虫进行查询
def getLoginInfo(banInfo):
    dataPackage = []
#筛选和对总容器填充后,返回必要数据(充值[待定]-设备名-分辨率-操作系统版本-联网方式)
    return dataPackage