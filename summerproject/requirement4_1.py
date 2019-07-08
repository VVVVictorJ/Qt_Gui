import numpy
from PIL import Image ,ImageFilter
import natsort
import os
import time
import tkinter
from tkinter import messagebox

# image_path='C:/Users/73497/Desktop/photo'
# image_name='123.jpg'
# imagename=image_path+'/'+image_name
# im = Image.open(imagename).convert('RGB')
# arr = np.array(im)
# print(arr.shape)
# print(arr[0][0])

def display_time(func):
    def wrapper(*args):
        time_star=time.time()
        result=func(*args)
        time_stop=time.time()
        total_time=str("总耗时{:.2f}s".format(time_stop-time_star))
        tkinter.messagebox.showinfo("提示", total_time)
        return result
    return wrapper

def blackWithe(imagename):   #黑白
    # r,g,b = r*0.299+g*0.587+b*0.114
    im = numpy.asarray(Image.open(imagename).convert('RGB'))
    trans = numpy.array([[0.299,0.587,0.114],[0.299,0.587,0.114],[0.299,0.587,0.114]]).transpose()
    im = numpy.dot(im,trans)
    return Image.fromarray(numpy.array(im).astype('uint8'))


def fleeting(imagename,params=10):        #冷色
    im = numpy.asarray(Image.open(imagename).convert('RGB'))
    im1 = numpy.sqrt(im*[1.0,0.0,0.0])*params
    im2 = im*[0.0,1.0,1.0]
    im = im1+im2
    return Image.fromarray(numpy.array(im).astype('uint8'))


def oldFilm(imagename):    #怀旧
    im = numpy.asarray(Image.open(imagename).convert('RGB'))
    # r=r*0.393+g*0.769+b*0.189 g=r*0.349+g*0.686+b*0.168 b=r*0.272+g*0.534b*0.131
    trans = numpy.array([[0.393,0.769,0.189],[0.349,0.686,0.168],[0.272,0.534,0.131]]).transpose()
    # clip 超过255的颜色置为255
    im = numpy.dot(im,trans).clip(max=255)
    return Image.fromarray(numpy.array(im).astype('uint8'))

def warmcolor(imagename,params=12):   #暖色
    im = numpy.asarray(Image.open(imagename).convert('RGB'))
    im1 = numpy.sqrt(im*[0.0,0.0,1.0])*params
    im2 = im*[1.0,1.0,0.0]
    im = im1+im2
    return Image.fromarray(numpy.array(im).astype('uint8'))

def fresh(imagename,params=14):    #清新
    im = numpy.asarray(Image.open(imagename).convert('RGB'))
    im1 = numpy.sqrt(im*[0.0,1.0,1.0])*params
    im2 = im*[1.0,0.0,0.0]
    im = im1+im2
    return Image.fromarray(numpy.array(im).astype('uint8'))

def lunkuo(imagename):  #轮廓滤镜
    im = Image.open(imagename).convert('RGB')
    pic = im.filter(ImageFilter.CONTOUR)
    pic = pic.filter(ImageFilter.EDGE_ENHANCE)

    return pic

def bianjie(imagename):  #边界提取滤镜
    im = Image.open(imagename).convert('RGB')
    pic = im.filter(ImageFilter.FIND_EDGES)
    pic = pic.filter(ImageFilter.EDGE_ENHANCE)

    return pic

def fudiao(imagename):  #浮雕滤镜
    im = Image.open(imagename).convert('RGB')
    pic = im.filter(ImageFilter.EMBOSS)
    pic = pic.filter(ImageFilter.EDGE_ENHANCE_MORE)

    return pic

@display_time
def picsave(image_path,mode):
    """
    :param image_path: 图片文件夹地址
    :param mode:   1：黑白
                   2：冷色
                   3：怀旧
                   4：暖色
                   5：清新
                   6：轮廓
                   7：边界
                   8：浮雕
    :return:
    """
    for filename in natsort.natsorted(os.listdir(image_path)):       #遍历地址下文件名
        filename=image_path+'/'+filename        #获得文件路径
        print(filename)
        if os.path.splitext(filename)[1] == ".jpg":
            if mode is 1:
                blackWithe(filename).save(filename)
            if mode is 2:
                fleeting(filename).save(filename)
            if mode is 3:
                oldFilm(filename).save(filename)
            if mode is 4:
                warmcolor(filename).save(filename)
            if mode is 5:
                fresh(filename).save(filename)
            if mode is 6:
                lunkuo(filename).save(filename)
            if mode is 7:
                bianjie(filename).save(filename)
            if mode is 8:
                fudiao(filename).save(filename)


def picshow(filename,mode):
    if os.path.splitext(filename)[1] == ".jpg":
        if mode is 1:
            blackWithe(filename).show()
        if mode is 2:
            fleeting(filename).show()
        if mode is 3:
            oldFilm(filename).show()
        if mode is 4:
            warmcolor(filename).show()
        if mode is 5:
            fresh(filename).show()
        if mode is 6:
            lunkuo(filename).show()
        if mode is 7:
            bianjie(filename).show()
        if mode is 8:
            fudiao(filename).show()

if __name__=='__main__':
    # img_path='C:/Users/73497/Desktop/photo1/test3'
    # picsave(img_path,7)
    img_dir='C:/Users/73497/Desktop/photo/psb.jpg'
    picshow(img_dir,7)

# img1=fudiao(imagename)
# img2=bianjie(imagename)
# img3=lunkuo(imagename)
# img4=warmcolor(imagename)
# img5=fresh(imagename)
# img6=blackWithe(imagename)
# img7=oldFilm(imagename)
# img8 =fleeting(imagename)
# img9 = Image.open(imagename).convert('RGB')
#
# img1.show()
# img2.show()
# img3.show()
# img4.show()
# img5.show()
# img6.show()
# img7.show()
# img8.show()
# img9.show()

# img1.save(image_path+'/'+'000'+'1'+'.jpg')
# img2.save(image_path+'/'+'000'+'2'+'.jpg')
# img3.save(image_path+'/'+'000'+'3'+'.jpg')
# img4.save(image_path+'/'+'000'+'4'+'.jpg')
# img5.save(image_path+'/'+'000'+'5'+'.jpg')
# img6.save(image_path+'/'+'000'+'6'+'.jpg')
# img7.save(image_path+'/'+'000'+'7'+'.jpg')
# img8.save(image_path+'/'+'000'+'8'+'.jpg')
# img9.save(image_path+'/'+'000'+'9'+'.jpg')





# fig = plt.figure()
# subplot(331)
# imshow(img1)
# title('img1')
# axis('off')
# subplot(332)
# imshow(img2)
# title('img2')
# axis('off')
# subplot(333)
# imshow(img3)
# title('img3')
# axis('off')
# subplot(334)
# imshow(img4)
# title('img4')
# axis('off')
# subplot(335)
# imshow(img4)
# title('img5')
# axis('off')
# subplot(336)
# imshow(img6)
# title('img6')
# axis('off')
# subplot(337)
# imshow(img7)
# title('img7')
# axis('off')
# subplot(338)
# imshow(img8)
# title('img8')
# axis('off')
# subplot(339)
# imshow(img9)
# title('img9')
# axis('off')
# show()

# img2=test2(imagename)
# img3=test1(imagename)
# img.show()
# img2.show()
# img3.show()