"""
@Introduce : 第三步，划分数据集
@File      : copy_txt.py
@Time      : 2021/09/09 20:40
@Author    : luhenghui

根据Imagests/Main里分好的train、val、test需要的文件名，复制到images目录下，标注txt复制到labels目录下
--root_dir 输入根目录$ROOT_PATH的位置

命令行：
python copy_txt.py
"""

import os
import shutil
from tqdm import tqdm

SPLIT_PATH = "../../../dataset_test/test_f/class3/VOC2007/ImageSets/Main"
IMGS_PATH = "../../../dataset_test/test_f/class3/VOC2007/JPEGImages"
TXTS_PATH = "../../../dataset_test/test_f/class3/VOC2007/txts"

TO_IMGS_PATH = '../../../dataset_test/test_f/class3/YOLO3/images'
TO_TXTS_PATH = '../../../dataset_test/test_f/class3/YOLO3/labels'

data_split = ['train.txt', 'val.txt', 'test.txt']
to_split = ['train', 'val', 'test']

for index, split in enumerate(data_split):
    split_path = os.path.join(SPLIT_PATH, split)

    to_imgs_path = os.path.join(TO_IMGS_PATH, to_split[index])
    if not os.path.exists(to_imgs_path):
        os.makedirs(to_imgs_path)

    to_txts_path = os.path.join(TO_TXTS_PATH, to_split[index])
    if not os.path.exists(to_txts_path):
        os.makedirs(to_txts_path)

    f = open(split_path, 'r')
    count = 1

    for line in tqdm(f.readlines(), desc="{} is copying".format(to_split[index])):
        # 复制图片
        src_img_path = os.path.join(IMGS_PATH, line.strip() + '.jpg')
        dst_img_path = os.path.join(to_imgs_path, line.strip() + '.jpg')
        if os.path.exists(src_img_path):
            shutil.copyfile(src_img_path, dst_img_path)
        else:
            print("error file: {}".format(src_img_path))

        # 复制txt标注文件
        src_txt_path = os.path.join(TXTS_PATH, line.strip() + '.txt')
        dst_txt_path = os.path.join(to_txts_path, line.strip() + '.txt')
        if os.path.exists(src_txt_path):
            shutil.copyfile(src_txt_path, dst_txt_path)
        else:
            print("error file: {}".format(src_txt_path))