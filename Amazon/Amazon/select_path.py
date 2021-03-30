#!-*-coding:utf-8 -*-
# python3.7
# @Author:fuq666@qq.com
# Update time:2021.03.28
# Filename:选择数据保存路径

import time
import tkinter as tk
from tkinter import filedialog
import os


#选择路径
def SelectPath():
    print('\n请选择数据保存路径···')
    root = tk.Tk()
    root.withdraw()
    Folderpath = filedialog.askdirectory()
    if not Folderpath:
        Folderpath = os.getcwd()

    path = Folderpath + '\\亚马逊'
    if os.path.exists(path):
        pass
    else:
        os.makedirs(path)
    print('保存在{}'.format(path))
    return path

if __name__ == "__main__":
    pass
    SelectPath()