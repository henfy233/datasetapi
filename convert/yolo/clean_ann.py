"""
@Introduce : 针对自定义数据集，根据文件名类别修改标注分类（我的数据集需要）
@File      : clean_ann.py
@Time      : 2022/4/13 14:18
@Author    : luhenghui

直接运行
"""

import os
import shutil
from tqdm import tqdm
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--root_dir', type=str, default=r'D:\data\xxxanno\labels_test', help="root path of labels")
arg = parser.parse_args()


def yoloClass(root_path, classes):
    print("Loading data from ", root_path)
    assert os.path.exists(root_path)

    indexes = os.listdir(root_path)
    # print('indexes', indexes)

    # 标注的id
    ann_num = 0
    # 修改多少标注
    ann_change_num = 0
    for k, index in enumerate(tqdm(indexes)):
        date = index.split('_')
        # print('date',date)

        file_data = ""
        with open(os.path.join(root_path, index), 'r') as fr:
            labelList = fr.readlines()
            for label in labelList:
                # print('ori', label)
                if classes[date[1]] != label[0]:
                    newLabel = classes[date[1]] + label[1:]
                    label = label.replace(str(label), str(newLabel))
                    ann_change_num += 1
                    # print('chang', label)

                # print('label', label)
                # print('newLabel', newLabel)
                ann_num += 1
                file_data += label
        with open(os.path.join(root_path, index), 'w') as fr:
            fr.write(file_data)
    print('已处理完，总标签数为：', ann_num)
    print('已处理完，修改标签数为：', ann_change_num)
    return


if __name__ == "__main__":
    root_dir = arg.root_dir
    assert os.path.exists(root_dir)
    classes = {'20211011': '0', '20210617': '1', '20210628': '2'}
    # print(root_dir)
    yoloClass(root_dir, classes)
