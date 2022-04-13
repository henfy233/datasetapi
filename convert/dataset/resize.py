"""
@Introduce : 把数据集（图片）统一resize一定尺寸
@File      : resize.py
@Time      : 2022年4月13日01:37:27
@Author    : luhenghui

直接运行
"""

import PIL
from PIL import Image
import os


def convert(root_dir, save_dir, width, height):
    for i in os.listdir(root_dir):
        print('i', i)
        im = Image.open(os.path.join(root_dir, i))
        (x, y) = im.size
        # 根据宽度改高度
        # x_s = width
        # y_s = y * x_s / x
        # 根据高度改宽度
        y_s = height
        x_s = int(x * y_s / y)
        print('w', im.size[0], 'h', im.size[1])
        # im.show()
        out = im.resize((x_s, y_s), Image.ANTIALIAS)
        print('w', out.size[0], 'h', out.size[1])
        # out.show()
        out.save(save_dir+i)


if __name__ == '__main__':
    root_dir = r'G:\data\study\GitHub\mmdetection\data\panicle_period\images'
    save_dir = r'G:\data\study\GitHub\mmdetection\data\panicle_period\xxxtest/'
    convert(root_dir, save_dir, 1066, 800)
