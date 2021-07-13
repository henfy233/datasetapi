"""
@Introduce : 图片已经传了一部分到验证集，标签数据也要对应传输到验证集
@File      : movetxt.py
@Time      : 2021/7/13 10:46
@Author    : luhenghui
"""

import os, random, shutil

dir = r'G:/data/study/GitHub/test_merge1'
imgdir = dir + "\\images"
labeltdir = dir + "\\labels\\train"
labelvdir = dir + "\\labels\\val"
list = []

if __name__ == '__main__':
    valpath = imgdir + "\\val"
    files = os.listdir(valpath)
#     print(files)
    filelength = len(files)
    print("filelength = %d " % filelength)
    for file in files:
#         print(file)
        name = file.split(".")
        list.append(name[0]+".txt")
    print(list)
    for name in list:
        print("name = %s"%name)
        shutil.move(os.path.join(labeltdir, name), os.path.join(labelvdir, name))