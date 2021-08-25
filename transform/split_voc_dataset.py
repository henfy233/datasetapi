"""
@Introduce : 随机划分数据集（voc数据格式的划分），按train:val:test = 8:1:1保存
@File      : split_voc_dataset.py
@Time      : 2021/8/20 10:06
@Author    : luhenghui

记得要填 class名字
--root_dir 输入根目录$ROOT_PATH的位置
--random_split 为划分参数，如果没有这个参数则只保存train.json文件

bug: 还没修改好random_split参数用法

执行：
python split_voc_dataset.py --root_dir ../../mmdetection/data/test_f/class3 --random_split
"""

import os
import random
import argparse
from tqdm import tqdm
import xml
import xml.dom.minidom

parser = argparse.ArgumentParser()
parser.add_argument('--root_dir', default='./data', type=str,
                    help="root path of images and labels, include ./images and ./labels and classes.txt")
parser.add_argument('--random_split', action='store_true', help="random split the dataset, default ratio is 8:1:1")
arg = parser.parse_args()

VOC_CLASSES = ['hl', 'wh', 'wl']


def generate_train_val_test_txt(xml_file_path, save_Path):
    trainval_percent = 0.9
    train_percent = 0.8
    total_xml = os.listdir(xml_file_path)  # 得到文件夹下所有文件名称
    num = len(total_xml)
    list = range(num)
    tv = int(num * trainval_percent)
    tr = int(tv * train_percent)
    trainval = random.sample(list, tv)
    train = random.sample(trainval, tr)
    print("train and val size", tv)
    print("train size", tr)
    """
    将信息写入test.txt、train.txt、val.txt、trainval.txt
    """
    ftrainval = open(os.path.join(save_Path, 'trainval.txt'), 'w')
    ftest = open(os.path.join(save_Path, 'test.txt'), 'w')
    ftrain = open(os.path.join(save_Path, 'train.txt'), 'w')
    fval = open(os.path.join(save_Path, 'val.txt'), 'w')
    for i in tqdm(list):  # 第i个xml文件
        xml_name = total_xml[i][:-4]
        if i in trainval:
            ftrainval.write(xml_name + "\n")
            if i in train:
                ftrain.write(xml_name + "\n")
            else:
                fval.write(xml_name + "\n")
        else:
            ftest.write(xml_name + "\n")
    ftrainval.close()
    ftrain.close()
    fval.close()
    ftest.close()
    ######################################################################
    """
     将信息写入(class_name)_test.txt、(class_name)_train.txt、(class_name)_val.txt、(class_name)_trainval.txt
     """
    for idx in range(len(VOC_CLASSES)):  # 每一个类单独处理
        class_name = VOC_CLASSES[idx]
        # 创建txt
        class_trainval = open(os.path.join(save_Path, str(class_name) + '_trainval.txt'), 'w')
        class_test = open(os.path.join(save_Path, str(class_name) + '_test.txt'), 'w')
        class_train = open(os.path.join(save_Path, str(class_name) + '_train.txt'), 'w')
        class_val = open(os.path.join(save_Path, str(class_name) + '_val.txt'), 'w')
        for k in tqdm(list):
            xml_name = total_xml[k][:-4]  # xml的名称
            # print(xml_name)
            xml_path = os.path.join(xml_file_path, xml_name + '.xml')
            ##################################################
            # 将获取的xml文件名送入到dom解析
            dom = xml.dom.minidom.parse(xml_path)  # 输入xml文件具体路径
            root = dom.documentElement
            # 获取xml object标签<name>
            object_name = root.getElementsByTagName('name')
            if len(object_name) > 0 and xml_name in object_name:  # 存在object（矩形框并且class_name在object_name列表中
                if k in trainval:
                    class_trainval.write(xml_name + ' ' + str(1) + "\n")
                    if k in train:
                        class_train.write(xml_name + ' ' + str(1) + "\n")
                    else:
                        class_val.write(xml_name + ' ' + str(1) + "\n")
                else:
                    class_test.write(xml_name + ' ' + str(1) + "\n")
            else:
                if k in trainval:
                    class_trainval.write(xml_name + ' ' + str(-1) + "\n")
                    if k in train:
                        class_train.write(xml_name + ' ' + str(-1) + "\n")
                    else:
                        class_val.write(xml_name + ' ' + str(-1) + "\n")
                else:
                    class_test.write(xml_name + ' ' + str(-1) + "\n")
        class_trainval.close()
        class_test.close()
        class_train.close()
        class_val.close()  # 1类的.txt编辑好了
    #################################################


if __name__ == "__main__":
    root_path = arg.root_dir
    assert os.path.exists(root_path), 'not found root_path'
    xml_file_path = os.path.join(root_path, 'VOC/Annotations')  # xml文件路径
    save_Path = os.path.join(root_path, 'VOC/ImageSets/Main')
    if not os.path.exists(save_Path):
        os.makedirs(save_Path)
    random_split = arg.random_split
    print("Loading data from ", root_path, "\nWhether to split the data:", random_split)
    generate_train_val_test_txt(xml_file_path, save_Path)
