# -*- coding = uft-8 -*-
# @Time : 2022/6/20 21:11
# @Author : 黄立慧
# @File : mctest.py
# @Software : PyCharm
from selenium.webdriver.common.by import By

from selenium import webdriver

dr = webdriver.Chrome()

page_url = 'https://test.mctech.vip'
dr.get(page_url)
# element = [
#     {'name':'search_ipt','desc':'点击账号输入框','by':(By.XPATH,'/html/body/div[1]/div[1]/div[1]/input[1])','ec':'presence_of_element_located','action':'send_keys()'},
#     {'name':'search_ipt','desc':'点击密码输入框','by':(By.XPATH,'/html/body/div[1]/div[1]/div[1]/input[2]','ec':'presence_of_element_located','action':'send_keys()'},
#     {'name':'search_but','desc':'点击登录按钮','by':(By.XPATH,'/html/body/div[1]/div[1]/div[1]/a)','ec':'presence_of_element_located','action':'send_keys()'},
# ]