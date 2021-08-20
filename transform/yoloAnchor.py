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
python yoloAnchor.py --root_dir ../..
python yoloAnchor.py --root_dir ../../dataset_test/test_merge_f --random_split
python yoloAnchor.py --root_dir ./train --random_split
"""
import os
import argparse
from tqdm import tqdm
from scipy.cluster.vq import kmeans

parser = argparse.ArgumentParser()
parser.add_argument('--root_dir', default='./data', type=str,
                    help="root path of images and labels, include ./images and ./labels and classes.txt")
parser.add_argument('--save_path', type=str, default='./train.json',
                    help="if not split the dataset, give a path to a json file")
parser.add_argument('--random_split', action='store_true', help="random split the dataset, default ratio is 8:1:1")
arg = parser.parse_args()

def yolo2coco(root_path):
    originLabelsDir = os.path.join(root_path, 'labels')
    with open(os.path.join(root_path, 'classes.txt')) as f:
        classes = f.read().strip().split()
    # images dir name
    indexes = os.listdir(originLabelsDir)
    print('classes',classes)
    print('indexes',indexes)

    # dataset = {'categories': [], 'annotations': [], 'images': []}
    # for i, cls in enumerate(classes, 0):
    #     dataset['categories'].append({'id': i, 'name': cls, 'supercategory': 'mark'})

    # 标注的id
    ann_id_cnt = 0
    for k, index in enumerate(tqdm(indexes)):
        # 支持 png jpg 格式的图片。
        txtFile = index.replace('images', 'txt').replace('.jpg', '.txt').replace('.png', '.txt')
        with open(os.path.join(originLabelsDir, txtFile), 'r') as fr:
            labelList = fr.readlines()
            print(index,len(labelList))
            small = 0
            middle = 0
            large = 0
            for label in labelList:
                label = label.strip().split()
                # x = float(label[1])
                # y = float(label[2])
                w = float(label[3])
                h = float(label[4])


                # print('w',w)
                # print('h',h)
                ann_id_cnt += 1
            print('small',small,'middle',middle,'large',large)
    return
    # 保存结果
    # folder = os.path.join(root_path, 'annotations')
    # if not os.path.exists(folder):
    #     os.makedirs(folder)
    # json_name = os.path.join(root_path, 'annotations/{}'.format(arg.save_path))
    # with open(json_name, 'w') as f:
    #     json.dump(dataset, f)
    #     print('Save annotation to {}'.format(json_name))



if __name__ == "__main__":
    root_path = arg.root_dir
    assert os.path.exists(root_path)
    # random_split = arg.random_split
    # print("Loading data from ", root_path, "\nWhether to split the data:", random_split)
    yolo2coco(root_path)