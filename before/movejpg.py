"""
@Introduce : 图片已经挑选过，需要重新从原图挑选
@File      : movejpg.py
@Time      : 2021/11/14 10:34
@Author    : luhenghui

python movejpg.py
"""

import os, random, shutil

imgdir = r'D:\AliDownloads\0628f'
# imgdir = r'D:\data\test211011-change\nice'
oridir = r'D:\data\0628f\origin'
afterdir = r'D:\data\0628f\nice'
list = []

if __name__ == '__main__':
    files = os.listdir(imgdir)
    print(files)
    filelength = len(files)
    print("filelength = %d " % filelength)
    for name in files:
        print("name = %s"%name)
        shutil.copy(os.path.join(oridir, name), os.path.join(afterdir, name))