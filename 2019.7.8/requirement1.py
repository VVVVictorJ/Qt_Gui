import os
import os.path
import time
import shutil
import tkinter
import tkinter.messagebox

# path = 'C:\\Users\\73497\\Desktop\\photo'


def traverse_photo(src_dir ,number,t):
    """

    :param src_dir:            #指定路径
    :param number:              #照片最低数量
    :return:
    """

    for i in range(t):
        PhotoNumber = 0
        flag=0
        dirs = os.listdir(src_dir)                       # 获取指定路径下的文件
        for name in dirs:                             # 循环读取路径下的文件并筛选输出
            if os.path.splitext(name)[1] == ".jpg":   # 筛选jpg文件
                PhotoNumber+=1
        if(PhotoNumber>=number):
            tkinter.messagebox.showinfo('提示', '照片达到阈值')
            flag=1
            break
        time.sleep(1)
    if(flag!=1):
        shutil.rmtree(src_dir)                         #删除文件夹内所有文件
        os.mkdir(src_dir)                              #删除文件夹内所有文件
        tkinter.messagebox.showinfo('提示', '文件夹已清空')

if __name__=='__main__':
    path = 'C:\\Users\\73497\\Desktop\\新建文件夹 (2)'
    traverse_photo(path ,1,1)