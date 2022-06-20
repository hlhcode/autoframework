# -*- coding = uft-8 -*-
import logging
import os
from datetime import time
from envs import autoframework
from selenium import webdriver


class BasePage:
    def __int__(self, driver):
        self.deriver = driver

    def get_img(self):
        # 截图
        # img文件夹路径
        img_path = os.path.join(autoframework.getcwd.get_cwd(),'img/')
        # img文件夹不存在，新建改文件夹
        if not os.path.exists(img_path):
            os.makedirs(img_path)
        # 获取当前日期
        local_date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        # 日期文件夹路径
        date_file_path = os.path.join(img_path,local_date)
        # 日期文件夹不存在，新建该文件夹
        if not os.path.exists(date_file_path):
            os.makedirs(date_file_path)
        # 截图存放路径
        local_time = time.strftime('%Y-%m-%d %H%M%S',time.localtime(time.time()))
        jt_name = local_time+'.png'
        jt_path = os.path.join(date_file_path,jt_name)
        try:
            self.deriver.get_screenshot_as_file(jt_path)
            logging.info('截图保存成功')
        except BaseException:
            logging.error('截图失败',exc_info=1)
        print('Screenshot_path:',jt_path)
    # 元素定位
    def locator(self, *loc):
        return self.deriver.find_element(*loc)

    # 清空
    def clear(self, *loc):
        self.locator(*loc).clear()

    # 输入
    def input(self, test, *loc):
        self.locator(*loc).send_keys(test)

    # 点击
    def click(self, *loc):
        self.locator(*loc).click()

    # 滑动（上下左右滑动）
    def swip(self, start_x, start_y, end_x, end_y, duration=0):
        # 获取屏幕的尺寸
        window_size = self.driver.get_window_size()
        x = window_size['width']
        y = window_size['height']
        self.driver.swipe(start_x=x * start_x,
                          start_y=y * start_y,
                          end_x=x * end_x,
                          end_y=y * end_y,
                          duration=duration)
