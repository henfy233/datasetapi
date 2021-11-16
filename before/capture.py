"""
@Introduce : 由于所拍原图较大，截取中间一部分作为训练
@File      : capture.py
@Time      : 2021/7/17 17:46
@Author    : luhenghui

命令行：
python capture.py
"""
import numpy as np
import cv2
import os

def compute_point(sh):
    num = 4
    x1 = int(sh[1] / num)
    x2 = sh[1] - x1
    y1 = int(sh[0] / num)
    y2 = sh[0] - y1
    return y1, y2, x1, x2

def compute_center(sh):
    center_x = int(sh[1] / 2)
    center_y = int(sh[0] / 2)
    return center_y, center_x

"""
切割原图中心图
"""
def capture_center(path, tpath):
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
            y1, y2, x1, x2 = compute_point(img.shape)
            print(y1, y2, x1, x2)
            cutimg = img[y1:y2, x1:x2] # 裁剪坐标为[y0:y1, x0:x1]
            # cv2.imshow('origin', img)
            # cv2.imshow('image', cutimg)
            print(savepath)
            # cv2.imwrite(savepath, cutimg)

"""
切割原图四张图片，上左上右，下左下右
"""
def capture4(path, tpath):
    isExists = os.path.exists(tpath)
    if not isExists:
        os.makedirs(tpath)
    for file in os.listdir(path):
        filepath = os.path.join(path, file)
        print("filepath", filepath)

        img = cv2.imread(filepath)
        print(img.shape)
        center_y, center_x = compute_center(img.shape)
        print(center_y, center_x)
        print("tpath", tpath)
        print("file", file)
        arr = file.split(".")

        cutimg1 = img[0:center_y, 0:center_x]
        cutimg2 = img[0:center_y, center_x:img.shape[1]]
        cutimg3 = img[center_y:img.shape[0], 0:center_x]
        cutimg4 = img[center_y:img.shape[0], center_x:img.shape[1]]
        list = [cutimg1,cutimg2,cutimg3,cutimg4]

        for i in range(1, 5):
            name = arr[0] + '_' + str(i) + '.' + arr[1]
            savepath = os.path.join(tpath, name)
            print("savepath", savepath)
            cv2.imwrite(savepath, list[i-1])

if __name__ == '__main__':
    path = r"D:\data\0628f\nice"
    tpath = r"D:\data\0628f\enhance"
    # capture_center(path, tpath)
    capture4(path, tpath)

    # k = cv2.waitKey(0)  # waitKey代表读取键盘的输入，0代表一直等待
    # if k == 27:  # 键盘上Esc键的键值
    #     cv2.destroyAllWindows()