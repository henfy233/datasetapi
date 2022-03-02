# train下有多类文件夹，在不同文件夹选随机的比例放进test文件夹多类中
# import os, random, shutil
#
# # 将 dir 目录下 train 中的各个文件夹中的文件随机移动到 dir 创建的 val 同名目录
# dir = r'G:/data/study/GitHub/test_merge1/images'
# rate = 0.2  # 选取的比例
#
# if __name__ == '__main__':
#
#     trainpath = dir + "\\train"
#     #     print(trainpath)
#     for file in os.listdir(trainpath):
#         #          print(file)
#         filepath = os.path.join(trainpath, file)  # 每个子文件夹
#         #         print("filepath = %s " %  filepath)
#
#         files = os.listdir(filepath)  # 每个子文件夹的所有文件列表
#         filelength = len(files)
#         #         print("filelength = %d " % filelength)
#
#         picklength = int(filelength * rate)
#         print("picklength = %d " % picklength)
#         sample = random.sample(files, picklength)  # 从每个子文件夹中随机选取
#         #         print("len-sample = %d " % len(sample))
#
#         list = filepath.split("\\")
#         testpath = dir + "\\val\\" + str(list[len(list) - 1])
#         #         print("valpath = %s"%valpath)
#         isExists = os.path.exists(testpath)
        # if not isExists:
        #     os.makedirs(testpath)
        #
        # for name in sample:
        #     #             print("name = %s"%name)
        #     shutil.move(os.path.join(filepath, name), os.path.join(testpath, name))

"""
这里是传输测试集的代码，暂时未修改
"""

# rate = 0.25  # 选取的比例
#
# if __name__ == '__main__':
#
#     trainpath = dir + "\\train"
#     #     print(trainpath)
#     for file in os.listdir(trainpath):
#         #          print(file)
#         filepath = os.path.join(trainpath, file)  # 每个子文件夹
#         #         print("filepath = %s " %  filepath)
#
#         files = os.listdir(filepath)  # 每个子文件夹的所有文件列表
#         filelength = len(files)
#         #         print("filelength = %d " % filelength)
#
#         picklength = int(filelength * rate)
#         print("picklength = %d " % picklength)
#         sample = random.sample(files, picklength)  # 从每个子文件夹中随机选取
#         #         print("len-sample = %d " % len(sample))
#
#         list = filepath.split("\\")
#         valpath = dir + "\\test\\" + str(list[len(list) - 1])
#         #         print("valpath = %s"%valpath)
#         isExists = os.path.exists(valpath)
#         if not isExists:
#             os.makedirs(valpath)
#
#         for name in sample:
#             #             print("name = %s"%name)
#             shutil.move(os.path.join(filepath, name), os.path.join(valpath, name))