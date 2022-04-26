"""
@Introduce : 通过pkl文件获取图片标注信息
@File      : get_meta_in_pkl.py
@Time      : 2022/4/18 10:06
@Author    : luhenghui

需要修改文件的路径，直接运行
"""

from copy import deepcopy
import pickle
import csv
from mmdet.datasets.coco import CocoDataset
from mmdet.apis import (async_inference_detector, inference_detector,
                        init_detector, show_result_pyplot)
from mmdet.datasets import (build_dataloader, build_dataset)


def returnDiv(myDict):
    for i in myDict:
        myDict[i] = '{:.2%}'.format(myDict[i] / sum)
    return myDict


pkl_dir = r'G:\data\study\GitHub\mmdetection\work_dirs\cascade_rcnn_r50_fpn_20e_coco\formal\best\softnms.5.pkl'
config = r'G:\data\study\GitHub\mmdetection\work_dirs\cascade_rcnn_r50_fpn_20e_coco\formal\best\cascade_rcnn_r50_fpn_20e_coco.py'
checkpoint = r'G:\data\study\GitHub\mmdetection\work_dirs\cascade_rcnn_r50_fpn_20e_coco\formal\best\latest.pth'
# 测试集路径
coco = CocoDataset('G:/data/study/GitHub/mmdetection/data/panicle_period/annotations/test.json', pipeline=[])
csv_file = open(r'G:\data\study\GitHub\mmdetection\work_dirs\cascade_rcnn_r50_fpn_20e_coco\formal\best\softnms.5.csv', 'w', newline='', encoding='gbk')
writer = csv.writer(csv_file)
writer.writerow(['ID', '文件名', '预测', '预测比例', '总共', '判断'])

score_thr = 0.3
device = 'cuda:0'

f = open(pkl_dir, 'rb')
results = pickle.load(f)

data_infos = coco.data_infos

cl = {0: '孕穗期', 1: '抽穗期', 2: '灌浆期', }



for x in range(len(results)):
    # for x in range(5):
    # print('读取第', x, '个文件')
    result = results[x]
    sum = 0
    num = {0: 0, 1: 0, 2: 0}
    for i in range(len(result)):
        for j in range(len(result[i])):
            if result[i][j][-1] > score_thr:
                num[i] += 1
                # print(result[i][j][-1])
            # num[i] += len(result[i])
            # print(cl[i], '有', num[i], '个')
        sum += num[i]
    # print('总共有', sum, '个')
    # print('num', num)

    key, val = max(num.items(), key=lambda x: x[1])
    # print(cl[key], val)

    tmp = deepcopy(num)
    # print('tmp', tmp)

    pre_ratio = returnDiv(tmp)
    # print(pre_ratio)

    ######################################
    writer.writerow([x, data_infos[x]['file_name'], num, pre_ratio, sum, cl[key]])

csv_file.close()
