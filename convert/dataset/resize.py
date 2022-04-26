"""
@Introduce : 把数据集（图片）统一resize一定尺寸
@File      : resize.py
@Time      : 2022年4月13日01:37:27
@Author    : luhenghui

直接运行
"""

from PIL import Image
import os
from tqdm import tqdm


def convert(root_dir, save_dir, width, height):
    for i in tqdm(os.listdir(root_dir)):
        # print('i', i)
        im = Image.open(os.path.join(root_dir, i))
        (x, y) = im.size
        # 根据宽度改高度
        # x_s = width
        # y_s = y * x_s / x
        # 根据高度改宽度
        y_s = height
        x_s = int(x * y_s / y)
        # print('w', im.size[0], 'h', im.size[1])
        # im.show()
        out = im.resize((x_s, y_s), Image.ANTIALIAS)
        # print('w', out.size[0], 'h', out.size[1])
        # out.show()
        out.save(os.path.join(save_dir, i))


if __name__ == '__main__':
    root_dir = r'G:\data\study\GitHub\dataset_test\panicle_period\images\test'
    save_dir = r'G:\data\study\GitHub\dataset_test\panicle_period\images\test1'
    convert(root_dir, save_dir, 1066, 800)
    print('resize完成')
