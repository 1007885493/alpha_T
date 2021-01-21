import re
import pypinyin

# cookies处理块
def cookieProcessing(cookie_str):
    cookies = {}
    for line in cookie_str.split(';') :
        key, value = line.split('=', 1)
        cookies[key] = value
        # cookies['name'] = key
        # cookies['value'] = value

    return cookies

# 打包地域数据
def localDataPackaging(localData):

    localDataPackage = []

    localDataPackage.append(['河北省', localData.count('河北省')])
    localDataPackage.append(['陕西省', localData.count('陕西省')])
    localDataPackage.append(['辽宁省', localData.count('辽宁省')])
    localDataPackage.append(['吉林省', localData.count('吉林省')])
    localDataPackage.append(['黑龙江省', localData.count('黑龙江省')])
    localDataPackage.append(['江苏省', localData.count('江苏省')])
    localDataPackage.append(['浙江省', localData.count('浙江省')])
    localDataPackage.append(['安徽省', localData.count('安徽省')])
    localDataPackage.append(['福建省', localData.count('福建省')])
    localDataPackage.append(['江西省', localData.count('江西省')])
    localDataPackage.append(['山东省', localData.count('山东省')])
    localDataPackage.append(['河南省', localData.count('河南省')])
    localDataPackage.append(['湖北省', localData.count('湖北省')])
    localDataPackage.append(['湖南省', localData.count('湖南省')])
    localDataPackage.append(['广东省', localData.count('广东省')])
    localDataPackage.append(['广西省', localData.count('广西省')])
    localDataPackage.append(['海南省', localData.count('海南省')])
    localDataPackage.append(['四川省', localData.count('四川省')])
    localDataPackage.append(['贵州省', localData.count('贵州省')])
    localDataPackage.append(['云南省', localData.count('云南省')])
    localDataPackage.append(['陕西省', localData.count('陕西省')])
    localDataPackage.append(['甘肃省', localData.count('甘肃省')])
    localDataPackage.append(['青海省', localData.count('青海省')])
    localDataPackage.append(['北京市', localData.count('北京市')])
    localDataPackage.append(['天津市', localData.count('天津市')])
    localDataPackage.append(['重庆市', localData.count('上海市')])
    localDataPackage.append(['山西省', localData.count('山西省')])
    localDataPackage.append(['台湾', localData.count('台湾省')])
    localDataPackage.append(['内蒙古', localData.count('内蒙古自治区')])
    localDataPackage.append(['西藏', localData.count('西藏自治区')])
    localDataPackage.append(['宁夏', localData.count('宁夏回族自治区')])
    localDataPackage.append(['新疆', localData.count('新疆维吾尔自治区')])
    localDataPackage.append(['香港', localData.count('香港特别行政区')])
    localDataPackage.append(['澳门', localData.count('澳门特别行政区')])

    return localDataPackage

def takeSecond(elem):
    return elem[1]

# 根据isYJ的值判断是否需要音节
def getPinYin(strs, isYJ):
    NormalPY = ''
    if isYJ == 0:
        for i in pypinyin.pinyin(strs, style=pypinyin.NORMAL):
            NormalPY += str(i).replace('[\'', '').replace('\']','')
            NormalPY += '-'
    if isYJ == 1:
        for i in pypinyin.pinyin(strs, heteronym=True):
            NormalPY = NormalPY + "-".join(i) + ' '

    return NormalPY

print(getPinYin('猥馨',0))
if re.search('jie-tu|duo-shao.*-jia|^dian$|w.{1,2}-x.{1,3}$|dian.{0,3}-hua$', getPinYin('猥馨',0)) is not None:
    print('1')

# 花里胡哨组
huahua = ['▼', '▶', '◀', '◆', '▲', '●', '♦', '■']

def getNewestService(Game,Branch,num) :
    url = 'http://t.4399data.com/home/?r=index/getServer&game='+Game+'&platform=' + Branch
    nsD = requests.get(url=url, cookies=cookieProcessing(cookieT)).text.encode('utf-8').decode('unicode_escape').split(
        '>')

    i = 3
    # print(nsD)
    nsOutput = nsD[i][1 :num]

    while nsOutput.find('AREA')  != -1 or nsOutput.find('ADMIN') != -1 or nsOutput.find('LOGIN') != -1 or nsOutput.find('91000') != -1:
        i = i + 2
        nsOutput = nsD[i][1 :num]
    return nsOutput