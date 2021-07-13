"""
@Introduce : 
@File      : class.py
@Time      : 2021/7/13 10:53
@Author    : luhenghui
"""

# 每个日期的图片都要分20%给验证集 2021-4-20

# 1. 把每个分组的不同日期的图片分别归类到每个分组
import os, random, shutil

dir = r'G:/dataset/rgbdsm/rgdsm/110_400/three grades'

datename = ['20160607', '170707', '2018.05.14', '2018.05.23', '2018.05.29', '2018.06.08', '2018.06.12',
            '180625', '200528', '200603', '200612']

trainpath = dir + "\\train"
for file in os.listdir(trainpath):
    filepath = os.path.join(trainpath, file)  # 每个子文件夹
    print("filepath = %s " % filepath)

    files = os.listdir(filepath)  # 每个子文件夹的所有文件列表

    for date in datename:
        testpath = filepath + "\\" + date
        print("testpath = %s " % testpath)
        isExists = os.path.exists(testpath)
        if not isExists:
            os.makedirs(testpath)
    # 输出所有文件和文件夹
    for file in files:
        if os.path.splitext(file)[1] == '.jpg':
            split = file[0:10]  # 截取文件名前十个字符
            for date in datename:
                if date in split:
                    shutil.move(os.path.join(filepath, file), os.path.join(filepath, date))
#                     print(date)

# 2. 把训练集每个分组的图片分20%到验证集val文件夹下

rate = 0.2

for classname in os.listdir(trainpath):
    filepath = os.path.join(trainpath, classname)
    print(filepath)
    print("filepath = %s " % filepath)
    for datename in os.listdir(filepath):
        datepath = os.path.join(filepath, datename)  # 每个子文件夹
        print("datepath = %s " % datepath)

        files = os.listdir(datepath)  # 每个子文件夹的所有文件列表
        filelength = len(files)
        print("filelength = %d " % filelength)

        picklength = int(filelength * rate)
        print("picklength = %d " % picklength)
        sample = random.sample(files, picklength)  # 从每个子文件夹中随机选取
        print("len-sample = %d " % len(sample))

        list = filepath.split("\\")
        valpath = dir + "\\val\\" + str(list[len(list) - 1])
        print("valpath = %s" % valpath)
        isExists = os.path.exists(valpath)
        if not isExists:
            os.makedirs(valpath)

        for name in sample:
            print("originpath = %s" % os.path.join(datepath, name))
            print("afterpath = %s" % os.path.join(valpath, name))
            shutil.move(os.path.join(datepath, name), os.path.join(valpath, name))

# 3. 把训练集每个分组的图片提取出来，并删除文件夹
for classname in os.listdir(trainpath):
    filepath = os.path.join(trainpath, classname)
    print(filepath)
    print("filepath = %s " % filepath)

    print(os.path.isdir(filepath))

    for datename in os.listdir(filepath):
        datepath = os.path.join(filepath, datename)  # 每个子文件夹
        print("datepath = %s " % datepath)

        files = os.listdir(datepath)  # 每个子文件夹的所有文件列表
        filelength = len(files)
        print("filelength = %d " % filelength)

        for name in files:
            print("originpath = %s" % os.path.join(datepath, name))
            print("afterpath = %s" % os.path.join(filepath, name))
            shutil.move(os.path.join(datepath, name), os.path.join(filepath, name))

        if os.path.isdir(datepath):
            os.rmdir(datepath)