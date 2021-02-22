# 传入一般的数据表,产出任意列为基准的数据透视表

# 接收数组与对应的基准列
def tableFactory(list,num):
    # 确定基准列,我这边预计的数据结构是每个list第0位元素是列标题
    theBase = list[0][num]
    # 用set储存每个成员
    colsBox = set()
    for i in range(1,len(list)):
        if list[i]:
            colsBox.add(list[i][num])
            pass
        pass
    # 数量比较
        # 获取总行数

        # 遍历该列元素,产出当前元素对应数量,以dictionary形式储存

    # 产出新表格(dict结构),以制图
    return 0