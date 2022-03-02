"""
@Introduce : 图像分类 VGG16模型 tensorflow代码
@File      : vgg16.py
@Time      : 2021/7/18 10:06
@Author    : luhenghui

执行：python vgg16.py
注意：
"""

import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import sklearn
import tensorflow as tf
from tensorflow import keras
import PIL
import IPython
import kerastuner as kt

from keras.models import Model, Input, load_model

from keras.callbacks import ReduceLROnPlateau
from keras.callbacks import ModelCheckpoint
from keras.callbacks import EarlyStopping

from keras.preprocessing.image import ImageDataGenerator
# from keras.callbacks import TensorBoard

# 数据集地址
train_dir = "G:/dataset/dsm/224_224/four grades/train"
test_dir = "G:/dataset/dsm/224_224/four grades/test"
val_dir = "G:/dataset/dsm/224_224/four grades/val"

print(os.path.exists(train_dir))
print(os.path.exists(test_dir))
print(os.path.exists(val_dir))

# print(os.listdir(train_dir))
# print(os.listdir(test_dir))
# print(os.listdir(val_dir))

# 设置参数
width = 224
height = 224
channels = 3

EPOCHS = 40
num_classes = 3
BATCH_SIZE = 16
save_path = './save_weights/VGG16-224_224-4_{epoch:02d}-{val_accuracy:.2f}.h5'

# 数据增强
train_datagen = keras.preprocessing.image.ImageDataGenerator(
#     rescale=1./255,
    preprocessing_function=keras.applications.vgg16.preprocess_input,
#     rotation_range=3,
     width_shift_range=0.02,
#      height_shift_range=0.02,
#     zoom_range=0.1,
    horizontal_flip=True,
    vertical_flip=True,
#     brightness_range = (1, 1.1),
#     fill_mode='nearest'
)
train_generator = train_datagen.flow_from_directory(train_dir,
                                                    target_size=(height, width),
                                                    batch_size=BATCH_SIZE,
                                                    seed=7,
                                                    shuffle=True,
                                                    color_mode="rgb",
                                                    class_mode="categorical")
test_datagen = keras.preprocessing.image.ImageDataGenerator(
    preprocessing_function=keras.applications.vgg16.preprocess_input,
#     rescale=1./255,
)
test_generator = test_datagen.flow_from_directory(test_dir,
                                                    target_size=(height, width),
                                                    batch_size=BATCH_SIZE,
                                                    seed=7,
                                                    shuffle=False,
                                                    color_mode="rgb",
                                                    class_mode="categorical")
val_datagen = keras.preprocessing.image.ImageDataGenerator(
    preprocessing_function=keras.applications.vgg16.preprocess_input,
)
val_generator = val_datagen.flow_from_directory(val_dir,
                                                target_size=(height, width),
                                                batch_size=BATCH_SIZE,
                                                seed=7,
                                                shuffle=False,
                                                color_mode="rgb",
                                                class_mode="categorical")
train_num = train_generator.samples
test_num = test_generator.samples
val_num = val_generator.samples

print(train_num, test_num, val_num)
print(train_generator[0][0].shape)
print(train_generator.class_indices)

class_names = ['0-20', '21-40', '41-60', '61-80']

plt.figure(figsize=(8,8))
for i in range(16):
    x = 1
    plt.subplot(4,4,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow((train_generator[i][0][x]+127.5)/255, cmap=plt.cm.binary)
    plt.xlabel(class_names[np.argmax(train_generator[i][1][x])])
plt.show()