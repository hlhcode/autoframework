# -*- coding: utf-8 -*-
import pandas

# 读取Excel文件内容，将结果转为字典形式
def read_excel(file, **kwargs):
    # 要安装openpyxl包
    data_dict = []
    try:
        data = pandas.read_excel(file, **kwargs)
        data_dict = data.to_dict("records")
    finally:
        return data_dict


# 在Excel文件中添加内容，写动态cookie等,不保存到文件中，临时写入
def addDate_excel(file):
    data = pandas.read_excel(file)
    # print(type(data.astype(str)["编码"]))
    # 将series所有值转变为字符串类型
    data['sign'] = data.astype(str)["编码"]+".hellowd." + data.astype(str)["名称"]
    data_dict = data.to_dict("records")
    print(data_dict)

sheet1 = read_excel("WBS_1219063746359296_1654765657044.xlsx")
# # sheet2 = read_excel("WBS_1219063746359296_1654765657044.xlsx",sheet_name="Sheet2")
print(sheet1)
# # print(sheet2)
# addDate_excel("WBS_1219063746359296_1654765657044.xlsx")