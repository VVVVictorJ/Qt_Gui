import tkinter as tk
import os
import shutil
# from tkinter import filedialog



# file_path = filedialog.askopenfilenames()
# path = 'C:/Users\\Mr.Chow\\Desktop\\test\\picture'
# filename='123'
# file_path=['C:/Users/Mr.Chow/Desktop/test/picture/20190614_103735.jpg', 'C:/Users/Mr.Chow/Desktop/test/picture/20190621_123202.jpg', 'C:/Users/Mr.Chow/Desktop/test/picture/20190622_130528.jpg', 'C:/Users/Mr.Chow/Desktop/test/picture/20190622_145021.jpg']

def copy_files(dest_dir,file_path,filename):
    """

    :param dest_dir: 目标文件夹地址
    :param file_path:   图片地址
    :param filename:    新建文件夹名
    :return:
    """
    # root = tk.Tk()
    # root.withdraw()
    if not os.path.exists(dest_dir+'/'+filename):
        os.mkdir(dest_dir+'/'+filename)

    for i in file_path:
        filenewname=os.path.split(i)[1]
        shutil.copyfile(i, dest_dir+'/'+filename+'/'+filenewname)

if __name__=='__main__':
    copy_files(path,file_path,filename)