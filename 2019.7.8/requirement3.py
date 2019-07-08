# -*- coding: utf-8 -*-
# coding=gbk

import exifread
import os
import natsort
import tkinter
import tkinter.messagebox
import time
#
# pic_path='C:/Users/Mr.Chow/Desktop/test/picture'
# num = 0
def display_time(func):
    def wrapper(*args):
        time_star=time.time()
        result=func(*args)
        time_stop=time.time()
        total_time=str("总耗时{:.2f}s".format(time_stop-time_star))
        tkinter.messagebox.showinfo("提示", total_time)
        return result
    return wrapper

def exif_image(filename,mode):
    """

    :param filename: #文件地址
    :param mode:        #文件模式
    :return:
    """

    global num

    with open(filename, 'rb') as f:
        tags = exifread.process_file(f)
        #     if re.match('Image Make', tag):
        #         print('[*] 品牌信息: ' + str(value))
        #     if re.match('Image Model', tag):
        #         print('[*] 具体型号: ' + str(value))
        #     if re.match('EXIF LensModel', tag):
        #         print('[*] 摄像头信息: ' + str(value))
        #     if re.match('EXIF DateTimeOriginal', tag):
        pic_path = os.path.split(filename)[0]


        if mode=="品牌":         #品牌
            ImageModel = str(tags['Image Model'])
            new_name=ImageModel+'0'+ str(num)+os.path.splitext(filename)[1]
            new_name = pic_path + '/' + new_name
        elif mode=="拍摄时间":      #照片时间
            if "EXIF DateTimeOriginal" in tags:
                print(tags['EXIF DateTimeOriginal'])
                DateTime = str(tags['EXIF DateTimeOriginal'])
                new_name = DateTime.replace(':', '').replace(' ', '_') + '0' + str(num) + os.path.splitext(filename)[1]
                new_name = pic_path + '/' + new_name


        elif mode=="作者信息":   #作者信息
            ImageArtist = str(tags['Image Artist'])
            new_name=ImageArtist +'0'+ str(num)+os.path.splitext(filename)[1]
            new_name = pic_path + '/' + new_name
        else:           #系统顺序
            new_name=str(num)+os.path.splitext(filename)[1]
            new_name = pic_path + '/' + new_name
        num+=1
    os.rename(filename, new_name)
@display_time
def rename(pic_path,i):
    global num
    num=0
    for filename in natsort.natsorted(os.listdir(pic_path)):       #遍历地址下文件名
        filename=pic_path+'/'+filename        #获得文件路径
        print(filename)
        if os.path.isfile(filename):
            try:
                exif_image(filename,i)
            except  FileExistsError:
                tkinter.messagebox.showinfo("提示","文件存在 无法重命名  请删除后再试")
                break
            except  KeyError:
                tkinter.messagebox.showinfo("没有关键信息 无法重命名")
                break
if __name__=='__main__':
    pic_path = 'C:/Users/Mr.Chow/Desktop/test/picture'
    rename(pic_path,4)

