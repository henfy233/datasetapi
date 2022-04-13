"""
@Introduce : 
@File      : yolo2csv.py
@Time      : 2021/7/14 0:37
@Author    : luhenghui

https://zhuanlan.zhihu.com/p/341801502
YOLO 格式的数据集转化为 COCO 格式的数据集
--root_dir 输入根目录$ROOT_PATH的位置
--save_path 如果不进行随机划分，可利用此参数指定输出文件的名字，默认保存为train.json
--random_split 为划分参数，如果没有这个参数则只保存train.json文件

需要把classes.txt放在根目录下

命令行：
python yolo2csv.py

"""

import os
import cv2
import json
from tqdm import tqdm
from sklearn.model_selection import train_test_split
import argparse

parser = argparse.ArgumentParser()
# parser.add_argument('--root_dir', default='./data', type=str,
#                     help="root path of images and labels, include ./images and ./labels and classes.txt")
parser.add_argument('--save_path', type=str, default='./train.json',
                    help="if not split the dataset, give a path to a json file")
arg = parser.parse_args()


def yolo2coco(root_path):
    originImagesDir = os.path.join(root_path, 'images')
    originLabelsDir = os.path.join(root_path, 'labels')
    with open(os.path.join(root_path, 'classes.txt')) as f:
        classes = f.read().strip().split()
    # images dir name
    indexes = os.listdir(originImagesDir)

    csv_labels = open("csv_labels.csv", "w")

    # 标注的id
    ann_id_cnt = 0
    for k, index in enumerate(tqdm(indexes)):
        # 支持 png jpg 格式的图片。
        txtFile = index.replace('images', 'txt').replace('.jpg', '.txt').replace('.png', '.txt')
        # 读取图像的宽和高
        im = cv2.imread(os.path.join(root_path, 'images/') + index)
        height, width, _ = im.shape

        # 添加图像的信息

        if not os.path.exists(os.path.join(originLabelsDir, txtFile)):
            # 如没标签，跳过，只保留图片信息。
            continue
        with open(os.path.join(originLabelsDir, txtFile), 'r') as fr:
            labelList = fr.readlines()
            for label in labelList:
                label = label.strip().split()
                x = float(label[1])
                y = float(label[2])
                w = float(label[3])
                h = float(label[4])

                # convert x,y,w,h to x1,y1,x2,y2
                H, W, _ = im.shape
                x1 = (x - w / 2) * W
                y1 = (y - h / 2) * H
                x2 = (x + w / 2) * W
                y2 = (y + h / 2) * H
                # 标签序号从0开始计算, coco2017数据集标号混乱，不管它了。
                cls_id = int(label[0])
                width = max(0, x2 - x1)
                height = max(0, y2 - y1)
                # print(format(x1, '.2f'))
                # print(x1)
                jpgFile = txtFile.replace('txt', 'jpg')
                csv_labels.write(
                    jpgFile + "," + "\"[" + format(x1, '.2f')+ "," + format(y1, '.2f')+"," +format(x2, '.2f')+ "," +format(y2, '.2f') + "]\"" + "," + str(cls_id) + "," + str(H) + "," + str(W) + "\n")
                # print(csv_labels)
                ann_id_cnt += 1

    csv_labels.close()



if __name__ == "__main__":
    # root_path = arg.root_dir
    # assert os.path.exists(root_path)
    root_path = r"G:\data\study\GitHub\mmdetection\data\panicle_period"

    print("Loading data from ", root_path)
    yolo2coco(root_path)