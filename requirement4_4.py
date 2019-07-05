import cv2
import os
import natsort


def on_mouse(event, x, y, flags, param):
    global img, point1, point2,min_x,min_y,width,height
    img2 = img.copy()
    if event == cv2.EVENT_LBUTTONDOWN:         #左键点击
        point1 = (x,y)
        cv2.circle(img2, point1, 10, (0,255,0), 5)
        cv2.imshow('image', img2)
    elif event == cv2.EVENT_MOUSEMOVE and (flags & cv2.EVENT_FLAG_LBUTTON):               #按住左键拖曳
        cv2.rectangle(img2, point1, (x,y), (255,0,0), 5)
        cv2.imshow('image', img2)
    elif event == cv2.EVENT_LBUTTONUP:         #左键释放
        point2 = (x,y)
        cv2.rectangle(img2, point1, point2, (0,0,255), 5)
        cv2.imshow('image', img2)
        if point1[0]<0:
            point1 = list(point1)
            point1[0] = 0
            point1= tuple(point1)
        if point2[0]<0:
            point2 = list(point1)
            point2[0] = 0
            point2 = tuple(point2)
        if point1[1]<0:
            point1 = list(point1)
            point1[1] = 0
            point1 = tuple(point1)
        if point2[1]<0:
            point2 = list(point1)
            point2[2] = 0
            point2 = tuple(point2)
        min_x = min(point1[0],point2[0])
        min_y = min(point1[1],point2[1])
        width = abs(point1[0] - point2[0])
        height = abs(point1[1] -point2[1])
        print(point1[0],point1[1],point2[0],point2[1])


def main(file_path,save_path):
    """


    :param file_path: 选择黑边最大的图片
    :param save_path: 选择保存地址
    :return:
    """

    global img,min_x,min_y,width,height
    img = cv2.imread(file_path)
    cv2.namedWindow('image',cv2.WINDOW_FREERATIO)
    cv2.setMouseCallback('image', on_mouse)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    filepath= os.path.split(file_path)[0]
    print(filepath)
    for filename in natsort.natsorted(os.listdir(filepath)):
        if os.path.splitext(filename)[1] == ".jpg":
            pic_path = filepath + '/' + filename
            img = cv2.imread(pic_path)
            cut_img = img[min_y:min_y + height, min_x:min_x + width]
            cv2.imwrite(save_path+'/'+filename, cut_img,[int(cv2.IMWRITE_JPEG_QUALITY),100])



if __name__ == '__main__':
    file_path = 'C:/Users/Mr.Chow/Desktop/test/picture/20190622_130525.jpg'
    save_path = 'c:/users/Mr.Chow/Desktop/test'
    main(file_path,save_path)