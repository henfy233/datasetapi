"""
@Introduce : 用于MMdetection中pkl文件转化为json文件
@File      : pkl2json.py
@Time      : 2022/4/18 10:06
@Author    : luhenghui

需要修改两个文件的路径，直接运行
"""

from mmdet.datasets.coco import CocoDataset
import os
import json
import pickle

coco = CocoDataset('G:/data/study/GitHub/mmdetection/data/panicle_period/annotations/test.json', pipeline=[])

# pkl_dir = r'G:\data\study\GitHub\mmdetection\work_dirs\cascade_rcnn_r50_fpn_20e_coco\formal\best\nms.5.pkl'
# json_dir = r'G:\data\study\GitHub\mmdetection\work_dirs\cascade_rcnn_r50_fpn_20e_coco\formal\best\nms.5.json'

pkl_dir = r'G:\data\study\GitHub\mmdetection\work_dirs\cascade_rcnn_r50_fpn_20e_coco\best2.pkl'
json_dir = r'G:\data\study\GitHub\mmdetection\work_dirs\cascade_rcnn_r50_fpn_20e_coco\best2.json'

f = open(pkl_dir, 'rb')
results = pickle.load(f)
# 验证集路径
json_results = coco._det2json(results=results)

# if os.path.exists(json_dir):
#     os.remove(json_dir)
#     json.dump(json_results, open(json_dir, 'w'), indent=4)

json.dump(json_results, open(json_dir, 'w'), indent=4)
print('运行结束，文件保存到', json_dir)
