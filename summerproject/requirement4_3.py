import cv2
import natsort
import os
import numpy as np


#img_path = 'C:/Users/73497/Desktop/photo1/test3'
# img_1 = cv2.imread('C:/Users/73497/Desktop/photo1/test2/30.jpg')
# print img.shape


def on_EVENT_LBUTTONDOWN(event,x,y,flags,param):
    global t1,t2,img
    if event ==cv2.cv2.EVENT_RBUTTONDOWN:
        xy = '%d,%d '% (x, y)
        print (xy)
        # cv2.circle(img, (x, y), 1, (255, 0, 0), thickness=-1)
        # cv2.putText(img, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
        #             1.0, (0, 0, 0), thickness=1)
        cv2.imshow("image", img)
        t2.append([x,y])
        t1.append([x,y])
    if event == cv2.EVENT_LBUTTONDOWN:

        xy = '%d,%d '% (x, y)
        print (xy)
        cv2.circle(img, (x, y), 1, (255, 0, 0), thickness=-1)
        cv2.putText(img, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
                    1.0, (0, 0, 0), thickness=1)
        cv2.imshow("image", img)
        t1.append([x,y])


def warpaffine(img_path, save_path):
    global t1, t2, img
    t1=[]
    t2=[]
    for imgname in natsort.natsorted(os.listdir(img_path)):
        if os.path.splitext(imgname)[1] == ".jpg":
            img_name = os.path.join(img_path+ '/',imgname)
            img=cv2.imread(img_name)
            cv2.namedWindow("image",0)
            cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)
            cv2.imshow("image", img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            rows,cols = img.shape[:2]
            print(t1)
            print(t2)
            pts1 = np.float32([t1[0],[0,0],t1[1]])
            pts2 = np.float32([t2[0],[0,0],t2[1]])
            M = cv2.getAffineTransform(pts1,pts2)
            # #第三个参数：变换后的图像大小
            res = cv2.warpAffine(img,M,(cols,rows))
            #cv2.imwrite(img_name,res,[int(cv2.IMWRITE_JPEG_QUALITY),100])
            cv2.imwrite(save_path + '/' + imgname, res, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
            t1.clear()

# cv2.namedWindow("image_1",0)
# cv2.setMouseCallback("image_1", on_EVENT_LBUTTONDOWN)
# cv2.imshow("image_1", img_1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# print(t1)


# rows,cols = img_1.shape[:2]
# pts1 = np.float32([t1[0],[0,0],t1[1]])
# pts2 = np.float32([[1298,507],[0,0],[1295,1561]])
# M = cv2.getAffineTransform(pts1,pts2)
# #第三个参数：变换后的图像大小
# res = cv2.warpAffine(img_1,M,(cols,rows))
# cv2.namedWindow("res", 0)
# cv2.imshow("res", res)
# cv2.imwrite('C:/Users/73497/Desktop/photo1/test3/30.jpg',res,[int(cv2.IMWRITE_JPEG_QUALITY),100])
#
# cv2.namedWindow("img", 0)
# cv2.imshow("img", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

if __name__=='__main__':
    warpaffine(img_path)
    print()
    print(t2[0])
    print(t2[1])
