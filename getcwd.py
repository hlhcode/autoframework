# -*- coding = uft-8 -*-
import os
import sys

curParh = os.path.abspath(os.path.dirname(__file__))
rootPath = os.split(curParh[0])
sys.path.append(rootPath)

def get_cwd():
    path = os.path.dirname(os.path.abspath(__file__))
    # 当前文件的绝对路径
    return path
