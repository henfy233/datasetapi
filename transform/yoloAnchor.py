"""
@Introduce : 根据标注尺寸大小分类
@File      : yoloAnchor.py
@Time      : 2021/8/19 10:40
@Author    : luhenghui

YOLO 格式的数据集转化为 COCO 格式的数据集
--root_dir 输入根目录$ROOT_PATH的位置
--save_path 如果不进行随机划分，可利用此参数指定输出文件的名字，默认保存为train.json
--random_split 为划分参数，如果没有这个参数则只保存train.json文件

命令行：
python yoloAnchor.py --root_dir ../../merge_full

--random_split
"""
import os
import argparse
from tqdm import tqdm
from scipy.cluster.vq import kmeans

parser = argparse.ArgumentParser()
parser.add_argument('--root_dir', default='./data', type=str,
                    help="root path of images and labels, include ./images and ./labels and classes.txt")
arg = parser.parse_args()


def yolo2coco(root_path):
    originLabelsDir = os.path.join(root_path, 'labels')
    with open(os.path.join(originLabelsDir, 'classes.txt')) as f:
        classes = f.read().strip().split() # 获取类别
    print('originLabelsDir', originLabelsDir)
    # 图片文件夹名字
    indexes = os.listdir(originLabelsDir)[1:]  # 排除 classes.txt 文件
    # print('classes', classes)
    # print('indexes', indexes)

    # 标注的id
    ann_id_cnt = 0
    wl = 0  # width long
    wh = 0  # width height
    hl = 0  # height long
    new_class = 0  # 分类
    for k, index in enumerate(tqdm(indexes)):
        # 支持 png jpg 格式的图片。
        txtFile = index.replace('images', 'txt').replace('.jpg', '.txt').replace('.png', '.txt')
        file_data = ""
        with open(os.path.join(originLabelsDir, txtFile), 'r') as fr:
            labelList = fr.readlines()
            # print(index, len(labelList)) # 输出文件名，标注数
            for label in labelList:
                labels = label.strip().split()
                old_class = int(labels[0])
                # x = float(labels[1])
                # y = float(labels[2])
                w = float(labels[3])
                h = float(labels[4])
                ratio = w / h
                if ratio > 2:
                    wl += 1
                    new_class = 2
                elif ratio < 0.5:
                    hl += 1
                    new_class = 0
                else:
                    wh += 1
                    new_class = 1
                label = label.replace(str(old_class) + ' ', str(new_class) + ' ')
                # print('label', label)
                ann_id_cnt += 1
                file_data += label
        with open(os.path.join(originLabelsDir, txtFile), 'w') as fr:
            fr.write(file_data)
    print('总类别数')
    print('wl宽长', wl, 'wh中等', wh, 'hl高长', hl)
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
    root_path = arg.root_dir
    assert os.path.exists(root_path)
    # random_split = arg.random_split
    # print("Loading data from ", root_path, "\nWhether to split the data:", random_split)
    yolo2coco(root_path)
