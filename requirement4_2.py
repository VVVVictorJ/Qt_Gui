import cv2 as cv
import numpy as np
import natsort
import os

def contrast_Ratio_brightness(args):
    # global trackbarName1,trackbarName2,trackbarName3,windowName
    # arg参数：为接收新变量地址
    # a为对比度，g为亮度 ,p为锐度
    # cv.getTrackbarPos获取滑动条位置处的值
    # 第一个参数为滑动条1的名称，第二个参数为窗口的名称。
    a = 0.1*cv.getTrackbarPos(trackbarName1, windowName)
    g = cv.getTrackbarPos(trackbarName2, windowName)-30
    p = cv.getTrackbarPos(trackbarName3, windowName)/3+1
    h, w, c = image.shape
    mask = np.zeros([h, w, c], image.dtype)
    kernel_sharpen_1 = np.array([
        [-1, -1, -1, -1, -1],
        [-1, 2, 2, 2, -1],
        [-1, 2, p, 2, -1],
        [-1, 2, 2, 2, -1],
        [-1, -1, -1, -1, -1]]) / float(p)
    # cv.addWeighted函数对两张图片线性加权叠加
    dstImage = cv.addWeighted(image, a, mask, 1 - a, g)
    dstImage = cv.filter2D(dstImage, -1, kernel_sharpen_1)
    cv.namedWindow("dstImage", 0)
    # cv.resizeWindow("dstImage", 640, 480)
    cv.imshow("dstImage", dstImage)

def picshow(img_dir):
    global trackbarName1, trackbarName2, trackbarName3, windowName,image
    # cv.namedWindow("Saber",0)
    # cv.resizeWindow("Saber", 640, 480)
    # cv.imshow("Saber", image)
    image = cv.imread(img_dir)
    trackbarName1 = "Ratio"
    trackbarName2 = "Bright"
    trackbarName3 = "Sharpness"
    windowName = "dstImage"
    a = 10  # 设置a的初值。
    g = 30  # 设置g的初值。
    p = 50
    count1 = 20  # 设置a的最大值
    count2 = 100  # 设置g的最大值
    count3 = 50
    # 给滑动窗口命名，该步骤不能缺少！而且必须和需要显示的滑动条窗口名称一致。
    cv.namedWindow(windowName,0)
    # cv.resizeWindow(windowName, 640, 480)

    # 第一个参数为滑动条名称，第二个参数为窗口名称，
    # 第三个参数为滑动条参数，第四个为其最大值，第五个为需要调用的函数名称。
    cv.createTrackbar(trackbarName1, windowName, a, count1, contrast_Ratio_brightness)
    cv.createTrackbar(trackbarName2, windowName, g, count2, contrast_Ratio_brightness)
    cv.createTrackbar(trackbarName3, windowName, p, count3, contrast_Ratio_brightness)

    # 下面这步调用函数，也不能缺少。
    contrast_Ratio_brightness(0)

    cv.waitKey(0)
    cv.destroyAllWindows()


def picsave(image_path,a,g,p):
    """

    :param image_path: 文件夹地址
    :param a:   对比去
    :param g:   亮度
    :param p:   锐度
    :return:
    """
    a = 0.1 * a
    g = g - 30
    p = p / 3 + 1
    for filename in natsort.natsorted(os.listdir(image_path)):       #遍历地址下文件名
        filename=image_path+'/'+filename
        kernel_sharpen_1 = np.array([
            [-1, -1, -1, -1, -1],
            [-1, 2, 2, 2, -1],
            [-1, 2, p, 2, -1],
            [-1, 2, 2, 2, -1],
            [-1, -1, -1, -1, -1]]) / float(p)
        #获得文件路径
        if os.path.splitext(filename)[1] == ".jpg":
            image= cv.imread(filename)
            h, w, c = image.shape
            mask = np.zeros([h, w, c], image.dtype)
            # cv.addWeighted函数对两张图片线性加权叠加
            dstImage = cv.addWeighted(image, a, mask, 1 - a, g)
            dstImage = cv.filter2D(dstImage, -1, kernel_sharpen_1)
            cv.imwrite(filename,dstImage,[int(cv.IMWRITE_JPEG_QUALITY),100])


if __name__=='__main__':
    image_dir = 'C:/Users/73497/Desktop/photo/1.jpg'
    picshow(image_dir)
    # image_dir='C:/Users/73497/Desktop/photo1/test3'
    # a=6
    # g=10
    # p=10
    # picsave(image_dir,a,g,p)
