"""
@Introduce : 数据增强
@File      : augmentation.py
@Time      : 2021/7/13 12:11
@Author    : luhenghui

根据数据集大的图片扩增数据
大数据文件数量 2000张
小数据文件数量 500张
导出文件数量 1500张
后续需要移动导出文件到小数据文件
"""
import os
# 数据增强测试
from keras.preprocessing.image import ImageDataGenerator

path = r'G:\卢恒辉lodging\data prepared\features combined\dsm_1\dsm_1_Exr_2-enhance\training and validation'
dst_path = r'G:\卢恒辉lodging\data prepared\features combined\dsm_1\dsm_1_Exr_2-enhance\training and validation\test'
datagen = ImageDataGenerator(
    # rotation_range=3,
    # width_shift_range=0.05,
    # height_shift_range=0.05,
    # shear_range=0.05,
    # zoom_range=0.03,
    horizontal_flip=True,
    vertical_flip=True,
    # brightness_range=(0.95, 1.05),
    #  zca_whitening=True,
    # fill_mode='nearest'
)
gen = datagen.flow_from_directory(path, target_size=(260, 260), batch_size=2,
                                  save_to_dir=dst_path,
                                  shuffle=False,
                                  # classes=['21-40'],
                                  # classes=['41-60'],
                                  # classes=['31-60'],
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