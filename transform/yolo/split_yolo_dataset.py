"""
@Introduce : 随机划分数据集（yolo数据格式的划分），按train:val:test = 7:2:1保存
@File      : split_yolo_dataset.py
@Time      : 2021/7/14 10:06
@Author    : luhenghui

执行：python split_yolo_dataset.py --root_path $ROOT_PATH
python split_yolo_dataset.py --root_path G:/data/study/GitHub/dataset_test/test_f/class3
python split_yolo_dataset.py --root_path ../../../dataset_test/panicle
python split_yolo_dataset.py --root_path G:/data/study/GitHub/dataset_test/panicle_period
python split_yolo_dataset.py --root_path G:/data/study/GitHub/mmdetection/data/panicle_period
python split_yolo_dataset.py --root_path G:/data/study/GitHub/dataset_test/panicle_side

注意：文件标签需在images和labels文件夹中单独存储
"""

from sklearn.model_selection import train_test_split
import os
import shutil
from tqdm import tqdm
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--root_path', type=str, default='yolo_data', help="root path of images and labels")
arg = parser.parse_args()


def train_test_val_split(img_paths, ratio_train, ratio_val, ratio_test):
    assert int(ratio_train+ratio_test+ratio_val) == 1

    phase = ['train', 'val', 'test']
    # 不同环境下面，listdir读取的顺序不一定相同的！
    train_img, middle_img = train_test_split(img_paths,test_size=1-ratio_train, random_state=233)
    ratio=ratio_val/(1-ratio_train)
    val_img, test_img =train_test_split(middle_img, test_size=1-ratio, random_state=233)

    print("nums of train:val:test = {}:{}:{}".format(len(train_img), len(val_img), len(test_img)))
    p2path = {'train': train_img, 'val': val_img, 'test': test_img}
    # print(len(p2path['train']))
    # new_path = os.path.join(root_path, 'trainval')
    # if not os.path.exists(new_path):
    #     os.mkdir(new_path)
    if not os.path.exists(os.path.join(root_path, 'images')):
        os.mkdir(os.path.join(root_path, 'images'))
    if not os.path.exists(os.path.join(root_path, 'labels')):
        os.mkdir(os.path.join(root_path, 'labels'))
    img_path = os.path.join(root_path, 'images')
    for p in phase:
        dst_path = os.path.join(img_path, p)
        lab_path = os.path.join(root_path, 'labels', p)
        print('dst_path', dst_path)
        if not os.path.exists(dst_path):
            os.mkdir(dst_path)
            os.mkdir(lab_path)
        for img_name in tqdm(p2path[p]):
            # print(os.path.join(root_path, 'images1', img_name))
            # print(os.path.join(dst_path, 'images'))
            shutil.copy(os.path.join(root_path, 'ori_images', img_name), os.path.join(dst_path))
            if os.path.exists(os.path.join(root_path, 'ori_labels', img_name.replace('jpg','txt'))):
                shutil.copy(os.path.join(root_path, 'ori_labels', img_name.replace('jpg','txt')), os.path.join(lab_path))

    return train_img, val_img, test_img

if __name__ == '__main__':
    root_path = arg.root_path
    print('root_path', root_path)
    img_paths = os.listdir(os.path.join(root_path, 'ori_images'))
    label_paths = os.listdir(os.path.join(root_path, 'ori_labels'))
    train_test_val_split(img_paths, 0.7, 0.2, 0.1)