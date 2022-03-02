"""
@Introduce : MMClassification 根据文件夹内容输出文件名以及标签
@File      : autoPrint.py
@Time      : 2022年2月28日16:16:46
@Author    : luhenghui

执行：python autoPrint.py --root_path G:/data/study/GitHub/mmclassification/data/seedling_classification
"""

from tqdm import tqdm
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--root_path', type=str, default='yolo_data', help="root path of images and labels")
parser.add_argument('--class_num', type=int, default=1, help="class number")
arg = parser.parse_args()


def AutoPrint(root_path):
    res = ['train', 'val', 'test']
    for index in res:
        print('开始处理',index,'文件夹')
        file_path = os.path.join(root_path, index)
        print('file_path', file_path)
        txtFile = os.path.join(file_path, index + '.txt')
        print('txtFile', txtFile)
        file_data = ""
        open(txtFile, "w")
        for i in os.listdir(file_path)[:-1]:  # 排除最后一个train.txt
            print('i', i)
            class_path = os.path.join(file_path, i)
            for j in tqdm(os.listdir(class_path)):
                # print(i+'/'+j+' '+i)
                file_data += i + '/' + j + ' ' + i + '\n'
        # 写入文件
        with open(txtFile, 'w') as fr:
            fr.write(file_data)


if __name__ == '__main__':
    root_path = arg.root_path
    print('root_path', root_path)
    # print(os.listdir(root_path))

    AutoPrint(root_path)
