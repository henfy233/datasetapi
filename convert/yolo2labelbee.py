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


def convert(yolo_dir, labelbee_dir, classes, width, height):
    print("Loading data from ", yolo_dir)
    assert os.path.exists(yolo_dir)

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
        print(dataset)
        # 支持 jpg 格式的图片。
        jsonFile = index.replace('.txt', '.jpg') + '.json'
        # print(jsonFile)
        json_path = os.path.join(labelbee_dir, jsonFile)
        with open(json_path, 'w') as f:
            json.dump(dataset, f)
            print('Save annotation to {}'.format(json_path))


if __name__ == '__main__':
    yolo_dir = r'D:\data\xxxanno\test'
    labelbee_dir = r'D:\data\xxxanno\labelbee'
    width, height = 1066, 800
    classes = {'0': '孕穗期', '1': '抽穗期', '2': '灌浆期'}
    convert(yolo_dir, labelbee_dir, classes, width, height)
