"""
@Introduce : yolo标注，设为同一类
@File      : yoloClass.py
@Time      : 2021/7/14 10:06
@Author    : luhenghui

执行：python yoloClass.py
python yoloClass.py --root_dir G:/data/study/GitHub/dataset_test/panicle_period/test/tmp
"""

import os
import shutil
from tqdm import tqdm
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--root_dir', type=str,
                    default='G:/data/study/GitHub/mmdetection/data/labels',
                    help="root path of images and labels")
arg = parser.parse_args()


def yoloClass(root_path):
    print('root_path', root_path)
    # originLabelsDir = os.path.join(root_path, 'labels')
    # with open(os.path.join(originLabelsDir, 'classes.txt')) as f:
    #     classes = f.read().strip().split()  # 获取类别
    # print('originLabelsDir', originLabelsDir)
    # 图片文件夹名字
    # indexes = os.listdir(root_path)[1:]  # 排除 classes.txt 文件
    indexes = os.listdir(root_path)
    # print('classes', classes)
    print('indexes', indexes)

    # 标注的id
    ann_id_cnt = 0
    wl = 0  # width long
    wh = 0  # width height
    hl = 0  # height long
    new_class = 0  # 分类
    for k, index in enumerate(tqdm(indexes)):
        file_data = ""
        with open(os.path.join(root_path, index), 'r') as fr:
            labelList = fr.readlines()
            # print(index, len(labelList)) # 输出文件名，标注数
            for label in labelList:
                # labels = label.strip().split()
                newLabel = '0' + label[1:]

                # print('label', label)
                # print('newLabel', newLabel)
                label = label.replace(str(label), str(newLabel))
                # print('label', label)
                ann_id_cnt += 1
                file_data += label
        with open(os.path.join(root_path, index), 'w') as fr:
            fr.write(file_data)
    print('总标签数', ann_id_cnt)
    return

    # 保存结果
    # folder = os.path.join(root_path, 'class3')
    # if not os.path.exists(folder):
    #     os.makedirs(folder)
    # json_name = os.path.join(root_path, 'class3/{}'.format(arg.save_path))
    # with open(json_name, 'w') as f:
    #     json.dump(dataset, f)
    #     print('Save annotation to {}'.format(json_name))


if __name__ == "__main__":
    root_dir = arg.root_dir
    assert os.path.exists(root_dir)
    # random_split = arg.random_split
    # print("Loading data from ", root_dir, "\nWhether to split the data:", random_split)
    yoloClass(root_dir)
