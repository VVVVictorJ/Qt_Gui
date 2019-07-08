# -*- coding: utf-8 -*-

import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from MainUI import Ui_MainWindow
import os
import tkinter
import requirement1
import requirement2
import requirement3
import requirement4
import requirement4_1
import requirement4_2
import requirement4_3
import requirement4_4
import tkinter
#import requirement7


#


class  MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        # 让图片自适应label大小
        self.label_15.setScaledContents(True)
        self.label_22.setScaledContents(True)
        # 设置计数器上下限
        self.spinBox.setRange(0, 1000)
        self.spinBox_2.setRange(1, 1000)
        self.spinBox_3.setRange(0, 20)
        self.spinBox_4.setRange(0, 100)
        self.spinBox_5.setRange(12, 24)
        self.spinBox_6.setRange(1, 5)
        self.spinBox_7.setRange(0, 50)

        # tab1
        self.spinBox.valueChanged.connect(self.Valuechange)
        self.spinBox_2.valueChanged.connect(self.Valuechange_2)
        self.SelectFileBtn.clicked.connect(self.slot_btn_chooseDir)
        self.SaveFileBtn.clicked.connect(self.slot_btn_chooseMutiFile)
        self.SelectSaveAdressBtn.clicked.connect(self.slot_btn_choosesave)
        self.NameBtn.clicked.connect(self.selectName)
        self.ConfirmBtn.clicked.connect(self.Confirm)

        # tab2
        self.SelectFileBtn_2.clicked.connect(self.slot_btn_chooseDir_2)
        self.SelectTypeBtn.clicked.connect(self.selectStyle)
        self.ConfirmBtn_2.clicked.connect(self.Confirm_2)

        # tab3
        self.SelectPhoto.clicked.connect(self.OpenImage)
        self.SelectFileBtn_3.clicked.connect(self.slot_btn_chooseDir_3)
        self.radioButton.clicked.connect(self.Filter_1)
        self.radioButton_2.clicked.connect(self.Filter_2)
        self.radioButton_3.clicked.connect(self.Filter_3)
        self.radioButton_4.clicked.connect(self.Filter_4)
        self.radioButton_5.clicked.connect(self.Filter_5)
        self.radioButton_6.clicked.connect(self.Filter_6)
        self.radioButton_7.clicked.connect(self.Filter_7)
        self.radioButton_8.clicked.connect(self.Filter_8)
        self.AdjustBtn.clicked.connect(self.Process)
        self.spinBox_3.valueChanged.connect(self.Valuechange_3)
        self.spinBox_4.valueChanged.connect(self.Valuechange_4)
        self.spinBox_7.valueChanged.connect(self.Valuechange_7)
        self.ConfirmBtn_4.clicked.connect(self.Confirm_3)
        self.ConfirmBtn_8.clicked.connect(self.Confirm_3_1)

        # tab 4
        self.SelectPhoto_3.clicked.connect(self.slot_btn_chooseFile)
        self.SelectPhoto_4.clicked.connect(self.slot_btn_chooseFile_2)
        self.SelectFileBtn_5.clicked.connect(self.slot_btn_chooseDir_5)
        self.SelectSaveAdressBtn_4.clicked.connect(self.slot_btn_choosesave_3)
        self.SelectPhoto_6.clicked.connect(self.slot_btn_chooseFile_3)
        self.SelectSaveAdressBtn_5.clicked.connect(self.slot_btn_choosesave_4)
        self.ConfirmBtn_9.clicked.connect(self.Process_2)
        self.ConfirmBtn_10.clicked.connect(self.Process_3)
        #self.ConfirmBtn_5.clicked.connect(self.Process_4)

        # tab 5
        self.SelectFileBtn_4.clicked.connect(self.slot_btn_chooseDir_4)
        self.NameBtn_2.clicked.connect(self.selectName_2)
        self.SelectSaveAdressBtn_3.clicked.connect(self.slot_btn_choosesave_2)
        self.spinBox_5.valueChanged.connect(self.Valuechange_5)
        self.spinBox_6.valueChanged.connect(self.Valuechange_6)
        self.ConfirmBtn_7.clicked.connect(self.Confirm_4)

        #tab 6
        self.SelectVideo.clicked.connect(self.slot_btn_chosseFile_3)
        self.SelectVideo_2.clicked.connect(self.slot_btn_chosseFile_4)
        self.SelectPhoto_5.clicked.connect(self.slot_btn_chooseFile_5)
        self.SelectLogo.clicked.connect(self.slot_btn_chooseFile_6)



    #tab1
    def Valuechange(self, value):
        self.lineEdit_4.setText(str(self.spinBox.value()))

    def Valuechange_2(self, value):
        self.lineEdit_5.setText(str(self.spinBox_2.value()))

    def slot_btn_chooseDir(self, dir_choose):
        dir_choose = QFileDialog.getExistingDirectory(self, "选取文件夹", os.getcwd())
        if dir_choose == "":
            print("\n取消选择")
            return
        if (len(dir_choose) != 0):
            self.lineEdit.setText(dir_choose)
            print(dir_choose)

        requirement1.traverse_photo(dir_choose, self.spinBox.value(), self.spinBox_2.value())

    def slot_btn_chooseMutiFile(self):
        dir_files, ok = QFileDialog.getOpenFileNames(None,
                                                     "多文件选择", os.getcwd(),"All Files (*);;PDF Files (*.pdf);;Text Files (*.txt)")
        print(ok)
        if ok and len(dir_files) == 0:
            print("\n取消选择")
            return
        if (len(dir_files) != 0):
            self.lineEdit_3.setText(' '.join(dir_files))
            print(dir_files)
            print(self.lineEdit_3.text())

    def slot_btn_choosesave(self):
        dir_save = QFileDialog.getExistingDirectory(self, "选择文件夹", os.getcwd())
        if dir_save == "":
            print("\n取消选择")
            return
        if (len(dir_save) != 0):
            self.lineEdit_2.setText(dir_save)
            print(dir_save)

    def selectName(self):
        name,ok = QInputDialog.getText(self, "输入名字", "输入新建文件夹名称:",
                                        QLineEdit.Normal)
        if name == "":
            print("\n取消命名")
            return
        if ok and (len(name) != 0):
            self.lineEdit_8.setText(name)
            print(name)
    def Confirm(self):
        dest_dir=self.lineEdit_2.text()
        file_path=self.lineEdit_3.text()
        file_path=file_path.split(" ")              #list 转 str
        filename=self.lineEdit_8.text()
        requirement2.copy_files( dest_dir,  file_path, filename)

    # tab2
    def slot_btn_chooseDir_2(self):
        dir_choose = QFileDialog.getExistingDirectory(self, "选择文件夹", os.getcwd())
        if dir_choose == "":
            print("\n取消选择")
            return
        if (len(dir_choose) != 0):
            self.lineEdit_6.setText(dir_choose)
            print(dir_choose)

    def selectStyle(self, mode):
        list = ["品牌", "拍摄时间", "作者信息", "系统排序"]
        style, ok = QInputDialog.getItem(self, "排序方式", "请选择照片排序方式", list)
        if style == "":
            print("\n取消选择")
            return
        if ok:
            self.lineEdit_7.setText(style)
            print(style)

    def Confirm_2(self):
        filename = self.lineEdit_6.text()
        mode = self.lineEdit_7.text()
        requirement3.rename(filename, mode)

    # tab 3
    def slot_btn_chooseDir_3(self, dir_choose):
        dir_choose = QFileDialog.getExistingDirectory(self, "选取文件夹", os.getcwd())
        if dir_choose == "":
            print("\n取消选择")
            return
        if (len(dir_choose) != 0):
            self.lineEdit_15.setText(dir_choose)


    def OpenImage(self):
        imgName, imgType = QFileDialog.getOpenFileName(None,
                                                       "打开图片",os.getcwd(), "", "*.jpg;;*.png;;All Files(*)")
        jpg = QPixmap(imgName)
        self.label_15.setPixmap(jpg)
        if imgName == "":
            print("\n取消选择")
        if (len(imgName)!=0):
            self.lineEdit_16.setText(imgName)

    #调整锐度、饱和度按钮
    def Process(self):
        img_dir = self.lineEdit_16.text()
        requirement4_2.picshow(img_dir)

    #输入对比度，亮度，锐度
    def Valuechange_3(self, value):
        self.lineEdit_11.setText(str(self.spinBox_3.value()))

    def Valuechange_4(self, value):
        self.lineEdit_12.setText(str(self.spinBox_4.value()))

    def Valuechange_7(self, value):
        self.lineEdit_23.setText(str(self.spinBox_7.value()))

    #滤镜按钮
    def Filter_1(self):
        imagename =self.lineEdit_16.text()
        requirement4_1.picshow(imagename,1)

    def Filter_2(self):
        imagename = self.lineEdit_16.text()
        requirement4_1.picshow(imagename, 2)

    def Filter_3(self):
        imagename = self.lineEdit_16.text()
        requirement4_1.picshow(imagename, 3)

    def Filter_4(self):
        imagename = self.lineEdit_16.text()
        requirement4_1.picshow(imagename, 4)

    def Filter_5(self):
        imagename = self.lineEdit_16.text()
        requirement4_1.picshow(imagename, 5)

    def Filter_6(self):
        imagename = self.lineEdit_16.text()
        requirement4_1.picshow(imagename, 6)

    def Filter_7(self):
        imagename = self.lineEdit_16.text()
        requirement4_1.picshow(imagename, 7)

    def Filter_8(self):
        imagename = self.lineEdit_16.text()
        requirement4_1.picshow(imagename, 8)

    def Confirm_3(self):                                  #isChecked()返回单选按钮的状态，返回值True或False
        image_path = self.lineEdit_15.text()
        if self.radioButton.isChecked():
            requirement4_1.picsave(image_path, 1)
        if self.radioButton_2.isChecked():
            requirement4_1.picsave(image_path, 2)
        if self.radioButton_3.isChecked():
            requirement4_1.picsave(image_path, 3)
        if self.radioButton_4.isChecked():
            requirement4_1.picsave(image_path, 4)
        if self.radioButton_5.isChecked():
            requirement4_1.picsave(image_path, 5)
        if self.radioButton_6.isChecked():
            requirement4_1.picsave(image_path, 6)
        if self.radioButton_7.isChecked():
            requirement4_1.picsave(image_path, 7)
        if self.radioButton_8.isChecked():
            requirement4_1.picsave(image_path, 8)
        print("OK")

    def Confirm_3_1(self):
        image_path = self.lineEdit_15.text()
        a = self.spinBox_3.value()
        g = self.spinBox_4.value()
        p = self.spinBox_7.value()
        requirement4_2.picsave(image_path, a, g, p)
        print("OK")

    # tab 4
    def slot_btn_chooseFile(self):
        imgName, imgType = QFileDialog.getOpenFileName(None,
                                                           "打开图片", os.getcwd(), "", "*.jpg;;*.png;;All Files(*)")
        jpg = QPixmap(imgName)
        self.label_22.setPixmap(jpg)

        if imgName == "":
                print("\n取消选择")
                return
        if (len(imgName) != 0):
                self.lineEdit_17.setText(imgName)

    def slot_btn_chooseFile_2(self):
        imgName, imgType = QFileDialog.getOpenFileName(None,
                                                           "选择图片", os.getcwd(), "", "*.jpg;;*.png;;All Files(*)")

        jpg = QPixmap(imgName)
        self.label_22.setPixmap(jpg)
        if imgName == "":
                print("\n取消选择")
                return
        if (len(imgName) != 0):
                self.lineEdit_18.setText(str(imgName))

    def slot_btn_chooseDir_5(self):
        dir_choose = QFileDialog.getExistingDirectory(self, "选择文件夹", os.getcwd())
        if dir_choose == "":
            print("\n取消选择")
            return
        if (len(dir_choose) != 0):
            self.lineEdit_24.setText(dir_choose)

    def slot_btn_choosesave_3(self):
        dir_save = QFileDialog.getExistingDirectory(self, "选择文件夹", os.getcwd())
        if dir_save == "":
            print("\n取消选择")
            return
        if (len(dir_save) != 0):
            self.lineEdit_25.setText(dir_save)

    def slot_btn_chooseFile_3(self):
        imgName, imgType = QFileDialog.getOpenFileName(None,
                                                           "打开图片", os.getcwd(), "", "*.jpg;;*.png;;All Files(*)")
        jpg = QPixmap(imgName)
        self.label_22.setPixmap(jpg)

        if imgName == "":
                print("\n取消选择")
                return
        if (len(imgName) != 0):
                self.lineEdit_26.setText(imgName)

    def slot_btn_choosesave_4(self):
        dir_save = QFileDialog.getExistingDirectory(self, "选择文件夹", os.getcwd())
        if dir_save == "":
            print("\n取消选择")
            return
        if (len(dir_save) != 0):
            self.lineEdit_27.setText(dir_save)

    #防抖处理
    def  Process_2(self):
        img_path = self.lineEdit_24.text()
        save_path = self.lineEdit_25.text()
        requirement4_3.warpaffine(img_path, save_path)

    #图片裁剪
    def Process_3(self):
        file_path = self.lineEdit_26.text()
        save_path = self.lineEdit_27.text()
        requirement4_4.main(file_path, save_path)

    #图片扣绿
    # def Process_4(self):
    #     image_path1 = self.lineEdit_17.text()
    #     image_path2 = self.lineEdit_18.text()
    #     requirement7.delgreen(image_path1, image_path2)


    # tab 5
    def slot_btn_chooseDir_4(self):
        dir_choose = QFileDialog.getExistingDirectory(self, "选择文件夹", os.getcwd())
        if dir_choose == "":
            print("\n取消选择")
            return
        if (len(dir_choose) != 0):
            self.lineEdit_9.setText(dir_choose)

    def selectName_2(self):
        name, ok = QInputDialog.getText(self, "输入名称", "输入视频名称:",
                                        QLineEdit.Normal)
        if ok and (len(name) != 0):
            self.lineEdit_10.setText(name)

    def slot_btn_choosesave_2(self):
        dir_save = QFileDialog.getExistingDirectory(self, "选择文件夹", os.getcwd())
        if dir_save == "":
            print("\n取消选择")
            return
        if (len(dir_save) != 0):
            self.lineEdit_45.setText(dir_save)

    def Valuechange_5(self, value):
        self.lineEdit_13.setText(str(self.spinBox_5.value()))

    def Valuechange_6(self, value):
        self.lineEdit_14.setText(str(self.spinBox_6.value()))

    def Confirm_4(self):
        im_dir = self.lineEdit_9.text()
        save_dir = self.lineEdit_45.text()
        VideoName = self.lineEdit_10.text()
        fps = self.spinBox_5.value()
        num = self.spinBox_6.value()
        requirement4.CompositeVideo(im_dir, save_dir, VideoName, fps, num)

    #tab 6
    def slot_btn_chosseFile_3(self):
        fileName_choose, filetype = QFileDialog.getOpenFileName(self,
                                                               "选取文件",os.getcwd(),"All Files (*);;Text Files (*.txt)")
        if fileName_choose == "":
            print("\n取消选择")
            return
        if(len(fileName_choose)!=0):
            self.lineEdit_22.setText(fileName_choose)

    def slot_btn_chosseFile_4(self):
        fileName_choose, filetype = QFileDialog.getOpenFileName(self,
                                                               "选取文件",os.getcwd(),"All Files (*);;Text Files (*.txt)")
        if fileName_choose == "":
            print("\n取消选择")
            return
        if(len(fileName_choose)!=0):
            self.lineEdit_21.setText(fileName_choose)

    def slot_btn_chooseFile_5(self):
        imgName, imgType = QFileDialog.getOpenFileName(None,
                                                       "打开图片", os.getcwd(), "", "*.jpg;;*.png;;All Files(*)")
        if imgName == "":
            print("\n取消选择")
            return
        if (len(imgName) != 0):
            self.lineEdit_19.setText(imgName)

    def slot_btn_chooseFile_6(self):
        imgName, imgType = QFileDialog.getOpenFileName(None,
                                                       "打开图片", os.getcwd(), "", "*.jpg;;*.png;;All Files(*)")

        if imgName == "":
            print("\n取消选择")
            return
        if (len(imgName) != 0):
            self.lineEdit_20.setText(imgName)


if __name__ == '__main__':
    root = tkinter.Tk()
    root.withdraw()  # 隐藏主窗口
    root.wm_attributes('-topmost', 1)  # 消息框置顶
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())