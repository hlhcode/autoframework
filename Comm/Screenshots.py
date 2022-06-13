#-*- coding:UTF-8 -*-
import time
import os
from Comm.Log import BaseHome, log_path
from PIL import ImageGrab

#先定义截图文件的存放路径，这里在Log目录下建个Screen目录，按天存放截图

today = time.strftime("%Y%m%d")
screen_path = os.path.join(BaseHome,log_path,'screen',today)

#再使用PIL的ImageGrab实现截图
def screen(name):
    t = time.time()
    print(t)
    png = ImageGrab.grab()
    print(png)
    if not os.path.exists(screen_path):
        os.makedirs(screen_path)
    image_name = os.path.join(screen_path, name)
    png.save('%s_%s.png' % (image_name, str(round(t * 1000))))  # 文件名后面加了个时间戳，避免重名

    folder_list = os.listdir(log_path(screen))
    print(folder_list)
    png_list= os.listdir(screen_path)
    print(png_list)

    # if num >10:
    #     pass

screen(name='testScreen')