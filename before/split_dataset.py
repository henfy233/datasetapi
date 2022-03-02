"""
@Introduce : 随机划分数据集（数据格式的划分），按train:val:test = 6:2:2保存
@File      : split_dataset.py
@Time      : 2021/9/04 10:46
@Author    : luhenghui

执行：python split_dataset.py --root_path $ROOT_PATH
python split_dataset.py --root_path G:/dataset/seedling_classification_224 --class_num 3
python split_dataset.py --root_path G:/dataset/seedling_classification_300 --class_num 3
python split_dataset.py --root_path G:/dataset/seedling_classification_600 --class_num 3
"""

from sklearn.model_selection import train_test_split
import os
import shutil
from tqdm import tqdm
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--root_path',type=str,default='yolo_data', help="root path of images and labels")
parser.add_argument('--class_num',type=int,default=1, help="class number")
arg = parser.parse_args()

def train_test_val_split(dir_paths,class_num,ratio_train,ratio_test,ratio_val):
    assert int(ratio_train+ratio_test+ratio_val) == 1

    # phase = [['train', 'val', 'test'] for _ in range(class_num)]
    phase = ['train', 'val', 'test']
    print('phase', phase)
    # 不同环境下面，listdir读取的顺序不一定相同的！
    dir_name = os.listdir(dir_paths)
    print('dir_name',dir_name)
    for i in range(len(dir_name)):
        img_paths = os.listdir(os.path.join(dir_paths,dir_name[i]))
        # print('img_paths',img_paths)
        train_img, middle_img = train_test_split(img_paths,test_size=1-ratio_train, random_state=233)

        ratio=ratio_val/(1-ratio_train)
        val_img, test_img =train_test_split(middle_img,test_size=ratio, random_state=233)
        print(dir_name[i], '总:', len(img_paths), "nums of train:val:test = {}:{}:{}".format(len(train_img), len(val_img), len(test_img)))

        p2path = {'train':train_img,'val':val_img,'test':test_img}
        print(len(p2path['train']))
        for p in phase:
            # print('p',p)
            dst_path = os.path.join(root_path, p)
            print('dst_path', dst_path)
            if not os.path.exists(dst_path):
                os.mkdir(dst_path)
                for d in dir_name:
                    os.mkdir(os.path.join(dst_path, d))
            for img_name in tqdm(p2path[p]):
                # print('ori path', os.path.join(root_path, 'images', dir_name[i], img_name))
                # print('new path', os.path.join(dst_path, dir_name[i]))
                shutil.copy(os.path.join(root_path, 'images', dir_name[i], img_name), os.path.join(dst_path, dir_name[i]))
    # return train_img, val_img, test_img

if __name__ == '__main__':
    root_path = arg.root_path
    print('root_path', root_path)
    class_num = arg.class_num
    dir_paths = os.path.join(root_path, 'images')
    print('dir_paths', dir_paths)
    train_test_val_split(dir_paths,class_num,0.6,0.2,0.2)
