"""
@Introduce : yolo标注转换labelbee，单张图片转换
@File      : yolo2labelbee.py
@Time      : 2022/4/13 12:59
@Author    : luhenghui

默认图片大小统一自己设置
直接运行
"""

import os
import json
from tqdm import tqdm
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--yolo_dir', type=str, default=r'D:\data\xxxanno\labels', help="root path of yolo")
parser.add_argument('--labelbee_dir', type=str, default=r'D:\data\xxxanno\labelbee', help="root path of labelbee")
parser.add_argument('--size', type=str, default=(1066, 800), help="image size")
parser.add_argument('--classes', type=str, default={'0': '孕穗期', '1': '抽穗期', '2': '灌浆期'}, help="dataset classes")
arg = parser.parse_args()


def convert(yolo_dir, labelbee_dir, classes, size):

    (width, height) = size
    indexes = os.listdir(yolo_dir)
    for k, index in enumerate(tqdm(indexes)):
        # for k, index in enumerate(indexes):
        #     print(k, index)
        dataset = {'width': width, 'height': height, 'valid': True, 'rotate': 0,
                   'step_1': {'toolName': "rectTool", 'result': []}}
        # 标注的id
        ann_id_cnt = 0
        with open(os.path.join(yolo_dir, index), 'r') as fr:
            labelList = fr.readlines()
            for label in labelList:
                # print(label)
                label = label.strip().split()
                c = str(label[0])
                x = float(label[1])
                y = float(label[2])
                w = float(label[3])
                h = float(label[4])
                dataset['step_1']['result'].append({
                    'x': round((x - w / 2) * width, 13),
                    'y': round((y - h / 2) * height, 13),
                    'width': round(w * width, 13),
                    'height': round(h * height, 13),
                    'attribute': classes[c],
                    'valid': True,
                    # 'id': "%6d"%ann_id_cnt,
                    'id': str(ann_id_cnt).zfill(6),
                    'sourceID': "",
                    'textAttribute': "",
                    'order': ann_id_cnt,
                })
                ann_id_cnt += 1
        # print(dataset)
        # 支持 jpg 格式的图片。
        jsonFile = index.replace('.txt', '.jpg') + '.json'
        # print(jsonFile)
        json_path = os.path.join(labelbee_dir, jsonFile)
        with open(json_path, 'w') as f:
            json.dump(dataset, f)
            # print('Save annotation to {}'.format(json_path))


if __name__ == '__main__':
    yolo_dir = arg.yolo_dir
    print("Loading data from ", yolo_dir)
    assert os.path.exists(yolo_dir)
    labelbee_dir = arg.labelbee_dir
    assert os.path.exists(labelbee_dir)
    size = arg.size
    classes = arg.classes
    # print(arg)
    convert(yolo_dir, labelbee_dir, classes, size)
