"""
@Introduce : 由于所拍原图较大，截取中间一部分作为训练
@File      : capture.py
@Time      : 2021/7/17 17:46
@Author    : luhenghui
"""
import numpy as np
import cv2
import os

def compute_size(sh):
    num = 4
    x1 = int(sh[1] / num)
    x2 = sh[1] - x1
    y1 = int(sh[0] / num)
    y2 = sh[0] - y1
    return y1, y2, x1, x2

if __name__ == '__main__':
    path = r"D:\data\210711"
    tpath = r"D:\data\test0711_4\images"
    # path = "D:/Pycharm/45"
    for fpath in os.listdir(path):
        filepath = os.path.join(path, fpath)
        print("filepath", filepath)
        testpath = os.path.join(tpath, fpath)
        isExists = os.path.exists(testpath)
        if not isExists:
            os.makedirs(testpath)
        print("testpath", testpath)
        for file in os.listdir(filepath):
            savepath = os.path.join(testpath, file)
            file = os.path.join(filepath, file)
            print(file)
            img = cv2.imread(file)
            print(img.shape)
            y1, y2, x1, x2 = compute_size(img.shape)
            print(y1, y2, x1, x2)
            cutimg = img[y1:y2, x1:x2] # 裁剪坐标为[y0:y1, x0:x1]
            # cv2.imshow('origin', img)
            # cv2.imshow('image', cutimg)
            print(savepath)
            cv2.imwrite(savepath, cutimg)
            # k = cv2.waitKey(0)  # waitKey代表读取键盘的输入，0代表一直等待
            # if k == 27:  # 键盘上Esc键的键值
            #     cv2.destroyAllWindows()