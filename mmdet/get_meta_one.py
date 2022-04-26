"""
@Introduce : 通过模型预测获取单张图片标注信息
@File      : get_meta_one.py
@Time      : 2022/4/18 10:06
@Author    : luhenghui

需要修改文件的路径，直接运行
"""
import csv
from copy import deepcopy
from mmdet.apis import (inference_detector, init_detector)

# img = r'G:\data\study\GitHub\mmdetection\feature_map\image.jpg'

img = r'G:\data\study\GitHub\mmdetection\data\panicle_period\images\IMG_20210628_093129.jpg'
config = r'G:\data\study\GitHub\mmdetection\work_dirs\cascade_rcnn_r50_fpn_20e_coco\formal\best\cascade_rcnn_r50_fpn_20e_coco.py'
checkpoint = r'G:\data\study\GitHub\mmdetection\work_dirs\cascade_rcnn_r50_fpn_20e_coco\formal\best\latest.pth'
show_dir = r'G:\data\study\GitHub\mmdetection\feature_map\IMG_20210628_093129.jpg'
csv_file = open(r'G:\data\study\GitHub\mmdetection\feature_map\IMG_20210628_093129.csv', 'w', newline='', encoding='gbk')
PALETTE = [(255, 0, 0), (0, 0, 0), (0, 0, 255)]
score_thr = 0.3
device = 'cuda:0'

def main():
    # build the model from a config file and a checkpoint file
    model = init_detector(config, checkpoint, device=device)
    # test a single image
    result = inference_detector(model, img)
    # show the results
    # show_result_pyplot(
    #     model,
    #     args.img,
    #     result,
    #     palette=args.palette,
    #     score_thr=args.score_thr)
    model.show_result(
        img,
        result,
        score_thr=score_thr,
        bbox_color=PALETTE,
        text_color='white',
        thickness=6,
        #     palette=palette,
        show=True,
        out_file=show_dir)
    print('运行结束，文件保存到', show_dir)

    ######################################

    sum = 0
    num = {0: 0, 1: 0, 2: 0}
    cl = {0: '孕穗期', 1: '抽穗期', 2: '灌浆期', }
    for i in range(len(result)):
        for j in range(len(result[i])):
            if result[i][j][-1] > score_thr:
                num[i] += 1
                # print(result[i][j][-1])
            # num[i] += len(result[i])
            # print(cl[i], '有', num[i], '个')
        sum += num[i]
    # print('总共有',sum,'个，孕穗期有',num[0]/sum,'个，抽穗期有',num[1]/sum,'个，灌浆期有',num[2]/sum,'个')
    print('总共有', sum, '个')
    print('num', num)
    key, val = max(num.items(), key=lambda x: x[1])
    print(cl[key], val)

    tmp = deepcopy(num)
    print('tmp', tmp)

    def returnDiv(myDict):
        for i in myDict:
            myDict[i] = '{:.2%}'.format(myDict[i] / sum)
        return myDict

    pre_ratio = returnDiv(tmp)
    print(pre_ratio)

    ######################################
    # 保存文件
    writer = csv.writer(csv_file)
    writer.writerow(['文件名', '路径', '预测', '预测比例', '总共', '判断'])
    writer.writerow(['image.jpg', img, num, pre_ratio, sum, cl[key]])
    csv_file.close()

if __name__ == '__main__':
    main()


