"""
@Introduce : 随机选取一定数量的图片 （不常用）
@File      : random.py
@Time      : 2022年4月23日14:39:35
@Author    : luhenghui

直接运行
"""

import shutil
import os
import random
from tqdm import tqdm


def moveFile(root_dir, save_dir, random_num):
    pathDir = os.listdir(root_dir)  # 取图片的原始路径
    filenumber = len(pathDir)
    # rate = 0.1  # 自定义抽取图片的比例，比方说100张抽10张，那就是0.1
    # picknumber = int(filenumber * rate)  # 按照rate比例从文件夹中取一定数量图片
    picknumber = random_num
    sample = random.sample(pathDir, picknumber)  # 随机选取picknumber数量的样本图片
    print('该文件夹选取', len(sample), '张图片')
    for name in tqdm(sample):
        # print(name)
        shutil.copy(os.path.join(root_dir, name), os.path.join(save_dir, name))
    return

def mulCls():
    # classes = ['1', '2', '3']
    classes = ['2', '3']
    set = 'train'
    random_num = 1800
    root_dir = r'G:\dataset\seedling_classification_400'
    save_dir = r'G:\dataset\seedling_classification_400_3000'
    root_dir = os.path.join(root_dir, set)
    save_dir = os.path.join(save_dir, set)
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    for i in range(len(classes)):
        cls_root_dir = os.path.join(root_dir, classes[i])
        cls_save_dir = os.path.join(save_dir, classes[i])
        print('从文件夹中选取图片', cls_root_dir)
        print('正在保存该文件夹', cls_save_dir)
        if not os.path.exists(cls_save_dir):
            os.mkdir(cls_save_dir)
        moveFile(cls_root_dir, cls_save_dir, random_num)

def sinCls():
    random_num = 1688
    root_dir = r'G:\dataset\seedling_classification_400\train\1'
    save_dir = r'G:\dataset\seedling_classification_400_3000\train\1'
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    print('从文件夹中选取图片', root_dir)
    print('正在保存该文件夹', save_dir)
    moveFile(root_dir, save_dir, random_num)

if __name__ == '__main__':
    # 每个分类的训练集、验证集、测试集随机取一定数量图片
    mulCls()
    # 单个分类随机取一定数量图片
    # sinCls()
