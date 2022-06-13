# -*- coding: utf-8 -*-
import pandas


def read_excel(file, **kwargs):
    # 要安装openpyxl包
    data_dict = []
    try:
        data = pandas.read_excel(file, **kwargs)
        data_dict = data.to_dict("records")
    finally:
        return data_dict


sheet1 = read_excel("WBS_1219063746359296_1654765657044.xlsx")
# sheet2 = read_excel("WBS_1219063746359296_1654765657044.xlsx",sheet_name="Sheet2")
print(sheet1)
# print(sheet2)
