"""
@Introduce : 评估生成的结果，针对yolov5生成的检测结果（test中的--save-json参数，会生成best_predictions.json)，但是这个不适应cocoapi，需要用脚本来修改适应
@File      : coco_eval.py
@Time      : 2021/7/14 10:13
@Author    : luhenghui

--gt json格式，用于指定测试集的结果，如果没有，可以利用前面的yolo2coco.py进行转换。
--dt 同样检测网络生成的预测，使用cocoapi中loadRes来加载，所以需要有相应格式的检测结果。
--yolov5 将官方代码中生成的结果转换成适配cocoapi的结果。

执行：
python coco_eval.py --gt $GT_PATH --dt $DT_PATH --yolov5
"""
import json
import argparse
from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval
import os
import time

def transform_yolov5_result(result, filename2id):
    f = open(result ,'r',encoding='utf-8')
    dts = json.load(f)
    output_dts = []
    for dt in dts:
        dt['image_id'] = filename2id[dt['image_id']+'.jpg']
        dt['category_id'] # id对应好，coco格式和yolo格式的category_id可能不同。
        output_dts.append(dt)
    with open('temp.json', 'w') as f:
        json.dump(output_dts, f)

def coco_evaluate(gt_path, dt_path, yolov5_flag):
    cocoGt = COCO(gt_path)
    imgIds = cocoGt.getImgIds()
    gts = cocoGt.loadImgs(imgIds)
    filename2id = {}

    for gt in gts:
        filename2id[gt['file_name']] = gt['id']
    print("NUM OF TEST IMAGES: ",len(filename2id))

    if yolov5_flag:
        transform_yolov5_result(dt_path, filename2id)
        cocoDt = cocoGt.loadRes('temp.json')
    else:
        cocoDt = cocoGt.loadRes(dt_path)
    cocoEval = COCOeval(cocoGt, cocoDt, "bbox")
    cocoEval.evaluate()
    cocoEval.accumulate()
    cocoEval.summarize()
    if yolov5_flag:
        os.remove('temp.json')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--gt", type=str, help="Assign the groud true path.", default=None)
    parser.add_argument("--dt", type=str, help="Assign the detection result path.", default=None)
    parser.add_argument("--yolov5",action='store_true',help="fix yolov5 output bug", default=None)

    args = parser.parse_args()
    gt_path = args.gt
    dt_path = args.dt
    if args.yolov5:
        coco_evaluate(gt_path, dt_path, True)
    else:
        coco_evaluate(gt_path, dt_path, False)