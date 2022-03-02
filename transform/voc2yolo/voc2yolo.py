"""
@Introduce : voc转yolo
@File      : voc2yolo.py
@Time      : 2021/09/09 10:40
@Author    : luhenghui

VOC 格式的数据集转化为 YOLO 格式的数据集
--root_dir 输入根目录$ROOT_PATH的位置

命令行：
python voc2yolo.py --root_dir ../../datasets/mask
"""

import os.path
# import argparse
import xml.etree.ElementTree as ET

# parser = argparse.ArgumentParser()
# parser.add_argument('--root_dir', default='./data', type=str,
#                     help="root path of images and labels, include ./images and ./labels and classes.txt")
# arg = parser.parse_args()

# class YOLO2VOCConvert:
#     def __init__(self, txts_path, xmls_path, imgs_path):
#         self.txts_path = txts_path  # 标注的yolo格式标签文件路径
#         self.xmls_path = xmls_path  # 转化为voc格式标签之后保存路径
#         self.imgs_path = imgs_path  # 读取图片的路径和图片名字，存储到xml标签文件中
#         # self.classes = ["panicle"]
#         with open(os.path.join(txts_path, 'classes.txt')) as f:
#             self.classes = f.read().strip().split()

# class_names = ['palm', 'stone', 'scissor', 'awesome', 'heartB', 'OK', 'ROCK', 'one', 'swear', 'thanks', 'heartA',
#                'heartC', 'good', 'bad', 'pray', 'call', 'take_picture', 'salute']
class_names = ['wh', 'hl', 'wl']

xmlpath = '../../../dataset_test/test_f/class3/VOC2007/Annotations/'  # 原xml路径
txtpath = '../../../dataset_test/test_f/class3/YOLO3/labels/'  # 转换后txt文件存放路径
files = []

for root, dirs, files in os.walk(xmlpath):
    None

number = len(files)
print(number)
i = 0
while i < number:

    name = files[i][0:-4]
    xml_name = name + ".xml"
    txt_name = name + ".txt"
    xml_file_name = xmlpath + xml_name
    txt_file_name = txtpath + txt_name

    xml_file = open(xml_file_name)
    tree = ET.parse(xml_file)
    root = tree.getroot()
    filename = root.find('filename').text

    image_name = root.find('filename').text
    w = int(root.find('size').find('width').text)
    h = int(root.find('size').find('height').text)

    f_txt = open(txt_file_name, 'w+')
    content = ""

    first = True

    for obj in root.iter('object'):

        name = obj.find('name').text
        class_num = class_names.index(name)

        xmlbox = obj.find('bndbox')

        x1 = int(xmlbox.find('xmin').text)
        x2 = int(xmlbox.find('xmax').text)
        y1 = int(xmlbox.find('ymin').text)
        y2 = int(xmlbox.find('ymax').text)

        if first:
            content += str(class_num) + " " + \
                       str((x1 + x2) / 2 / w) + " " + str((y1 + y2) / 2 / h) + " " + \
                       str((x2 - x1) / w) + " " + str((y2 - y1) / h)
            first = False
        else:
            content += "\n" + \
                       str(class_num) + " " + \
                       str((x1 + x2) / 2 / w) + " " + str((y1 + y2) / 2 / h) + " " + \
                       str((x2 - x1) / w) + " " + str((y2 - y1) / h)

    # print(str(i / (number - 1) * 100) + "%\n")
    print(content)
    f_txt.write(content)
    f_txt.close()
    xml_file.close()
    i += 1

print("done!")