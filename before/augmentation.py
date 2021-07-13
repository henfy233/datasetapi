"""
@Introduce : 数据增强
@File      : augmentation.py
@Time      : 2021/7/13 12:11
@Author    : luhenghui
"""
import os
# 数据增强测试
from keras.preprocessing.image import ImageDataGenerator

path = 'G:/dataset/rgbdsm/rgdsm/110_400/three grades-newGan/val'
# path='G:/data/global-wheat-detection'
dst_path = 'G:/dataset/rgbdsm/rgdsm/110_400/three grades-newGan/Gan'
# dst_path='G:/data/global-wheat-detection/Gan'
datagen = ImageDataGenerator(
    rotation_range=3,
    #                            width_shift_range=0.05,
    #                            height_shift_range=0.05,
    shear_range=0.05,
    zoom_range=0.03,
    horizontal_flip=True,
    vertical_flip=True,
    brightness_range=(0.95, 1.05),
    #                             zca_whitening=True,
    fill_mode='nearest')
gen = datagen.flow_from_directory(path, target_size=(110, 400), batch_size=2,
                                  save_to_dir=dst_path,
                                  shuffle=False,
                                  #                                 classes=['21-40'],
                                  #                                 classes=['41-60'],
                                  #                                 classes=['61-100'],
                                  #                                 classes=['31-60'],
                                  classes=['61-100'],
                                  save_prefix='gen',
                                  save_format='jpg')

filepath = os.path.join(path, '0-30')
# filepath = os.path.join(path, '0-20')
files = os.listdir(filepath)  # 每个子文件夹的所有文件列表
filelength = len(files)
print("filelength = %d " % filelength)

sum = gen.samples
num = int((filelength - sum) / 2)
print(num)

for i in range(num):
    gen.next()