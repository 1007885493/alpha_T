# 进行一次完整的数据可视化,包括数据挖掘,清洗和可视化
import xlrd


# 挖掘流程,返回List供清洗或可视化
def dataMining():
    # 基本就是靠爬虫模块,不过今天先不搞
    # 先用Excel(或者说是csv\xls,无所屌谓),说起Excel就是xlrd啦
    data = xlrd.open_workbook(r'D:\alpha_T\files\closureLog_20210125.csv')
    index = 0
    sheet = data.sheets()[index]
    print('当前sheet有:' + str(data.sheet_names()) + '\n当前sheet有效行数为:' + str(sheet.nrows) + '\n当前sheet有效列数为:' + str(
        sheet.ncols))

    #把数据以List的形式传出,但每个元素以dirt的形式存储,看上去不错,我网上抄的.
    dataList = []
    rows = sheet.nrows
    # 获取第0行的所有列值
    colsName = sheet.row_values(0)
    # 遍历行数来获取该行每列的值
    for rowsNum in range(1,rows):
        row = sheet.row_values(rowsNum)
        if rows:
            # 以列数为基础结构的dirt
            dataDirt = {}
            # 遍历该行的每列来填入值
            dataDirt[rowsNum] = row
        dataList.append(dataDirt)

    return dataList


# 清洗流程
def dataCleaning():
    # 同样的,因为先不搞爬虫模块,就用现成的Excel吧!
    # 也不是不搞,主要是还没整合完,原来的那批又老又丑效率又不是最高,啧啧啧.
    pass


# 可视化
def dataVisualization():
    pass

list = dataMining()
for i in range(len(list)):
    print(list[i])
