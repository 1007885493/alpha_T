# 进行一次完整的数据可视化,包括数据挖掘,清洗和可视化
import xlrd
import pandas as pd
from pyecharts.charts import Bar

# 挖掘流程,返回List供清洗或可视化
def dataMining():
    # 基本就是靠爬虫模块,不过今天先不搞
    # 先用Excel(或者说是csv\xls,无所屌谓),说起Excel就是xlrd啦
    data = xlrd.open_workbook(r'E:\整合分析工具alpha\files\closureLog_20210125.csv')
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
    for rowsNum in range(rows):
        row = sheet.row_values(rowsNum)
        if rows:
            if rowsNum == 0:
                dataDirt = {}
                dataDirt[rowsNum] = row
            else:
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
    # 得到了相应数据之后,用pyecharts把它们可视化吧,做一个六图合并显示的布局,不同主题或类型的六个图表在一个html上显示
    # 每一千项为一个包,每个包进行一次可视化
    # 数据源
    # list = dataMining()
    # 直方图,基础
    # for i in range(list[0][0]):
    #     bar_01 = Bar().add_xaxis(list[0][0][i])
    # for j in range(1000):
    #     bar_01.add_yaxis()
    pass


pd.read_csv(r'E:\整合分析工具alpha\files\closureLog_20210125.csv')


