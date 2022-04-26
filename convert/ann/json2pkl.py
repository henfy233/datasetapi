"""
@Introduce : 用于MMdetection中json文件转化为pkl文件，例如经过wbf操作后验证测试集的评估
@File      : json2pkl.py
@Time      : 2022/4/18 10:06
@Author    : luhenghui

需要修改两个文件的路径，直接运行
"""

import pickle
import mmcv
import json
import numpy as np

# json_dir = r'G:/data/study/GitHub/mmdetection/work_dirs/cascade_rcnn_r50_fpn_20e_coco/formal/best/result.json'
# filepath = 'G:/data/study/GitHub/mmdetection/work_dirs/cascade_rcnn_r50_fpn_20e_coco/formal/best/result1.pkl'

# json_dir = r'G:/data/study/GitHub/mmdetection/work_dirs/cascade_rcnn_r50_fpn_20e_coco/ensemble.bbox.json'
# filepath = 'G:/data/study/GitHub/mmdetection/work_dirs/cascade_rcnn_r50_fpn_20e_coco/ensemble/max.5.pkl'

json_dir = r'G:/data/study/GitHub/mmdetection/work_dirs/cascade_rcnn_r50_fpn_20e_coco/ensemble.best.json'
filepath = 'G:/data/study/GitHub/mmdetection/work_dirs/cascade_rcnn_r50_fpn_20e_coco/ensemble.best.pkl'

f = open(json_dir, 'rb')
data = json.load(f)

# num = 0
N = 306  # 测试集数量
C = 3  # 数据集分类
pkl_data = [[[] for i in range(C)] for i in range(N)]
# pkl_data=[[[np.float32([])]for i in range(C)]for i in range(N)]
# np.array(bbox,dtype='float32')
# pkl_data=[[[]]*3]*306
# print(pkl_data[0])
for i in range(len(data)):
    #     print('data[i]', data[i])
    image_id = data[i]['image_id']
    category_id = data[i]['category_id']
    bbox = data[i]['bbox']
    bbox = [
        bbox[0],
        bbox[1],
        bbox[2] + bbox[0],
        bbox[3] + bbox[1],
    ]
    score = data[i]['score']
    bbox.append(score)
    #    bbox = np.array(bbox,dtype='float32')
    #     print('image_id', image_id)
    pkl_data[image_id][category_id].append(bbox)
#     np.append(pkl_data[image_id][category_id], bbox)
# print(pkl_data)
# pickle.dump(pkl_data, open(filepath, 'wb'))

for i in range(N):
    for j in range(C):
        b = np.float32(pkl_data[i][j])
        pkl_data[i][j] = b
#    bbox = np.array(bbox,dtype='float32')
#     print('image_id', image_id)
#     pkl_data[image_id][category_id].append(bbox)
#     np.append(pkl_data[image_id][category_id], bbox)
# print(pkl_data)
# pkl_data
# b = np.float32(pkl_data[image_id][category_id])
# pkl_data[image_id][category_id] = b
# pkl_data


# 直接覆盖文件运行
mmcv.dump(pkl_data, filepath)
# pickle.dump(pkl_data, open(filepath, 'wb'))
print('运行结束，文件保存到', filepath)