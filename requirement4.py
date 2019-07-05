import cv2
import os
import natsort
# from moviepy.editor import VideoFileClip, concatenate_videoclips
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.compositing import concatenate

def CompositeVideo(im_dir,save_dir,VideoName,fps,num):
    global w,h
    """
    :param im_dir: 图片文件夹地址
    :param save_dir: 视频保存的地址
    :param VideoName:   视频名称
    :param fps:     帧率
    :param num:     播放次数
    :return:
    """

    for imgname in natsort.natsorted(os.listdir(im_dir)):
        if os.path.splitext(imgname)[1] == ".jpg":
            imgname = os.path.join(im_dir+ '/',imgname)
            frame = cv2.imread(imgname)
            h=frame.shape[0]
            w=frame.shape[1]
            print(w,h)
            break
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    # print(sortlist.sort_filename(sortlist.delf(os.listdir(im_dir))))
    videoWriter_1 = cv2.VideoWriter(save_dir+'/'+VideoName+'.avi', fourcc,fps,(w, h))  # 括号可能是中文的，改一下，384,288需要改成你的图片尺寸，不然会报错
    videoWriter_2 = cv2.VideoWriter(save_dir+'/'+VideoName+'reverse'+'.avi', fourcc, fps, (w, h))

    #正序合成视频
    for imgname in natsort.natsorted(os.listdir(im_dir)):
        if os.path.splitext(imgname)[1] == ".jpg":
            imgname = os.path.join(im_dir+ '/',imgname)
            print(imgname)
            frame = cv2.imread(imgname)
            videoWriter_1.write(frame)
    videoWriter_1.release()
    #逆序合成视频
    Reverse_list=natsort.natsorted(os.listdir(im_dir))[::-1]
    for imgname in Reverse_list:
        # print(sortlist.sort_filename())
        if os.path.splitext(imgname)[1] == ".jpg":
            imgname = os.path.join(im_dir+'/', imgname)
            print(imgname)
            frame = cv2.imread(imgname)
            videoWriter_2.write(frame)
    videoWriter_2.release()
    repeatmv(num,VideoName,save_dir)

def repeatmv(num,mv_name,save_dir):
    """

    :param num:         循环次数
    :param mv_name:
    :param im_dir:
    :return:
    """
    mv_dir = os.path.join(save_dir + '/', str(mv_name) +'.avi')
    mv_dir_2 = os.path.join(save_dir + '/', str(mv_name) + 'reverse' + '.avi')
    movielist = []
    clip1 = VideoFileClip(mv_dir,target_resolution=(h, w))
    clip2 = VideoFileClip(mv_dir_2,target_resolution=(h, w))
    t = [clip1, clip2]

    for i in range(num):
        movielist += t
    finalclip = concatenate.concatenate_videoclips(movielist)
    finalclip.write_videofile(save_dir + '/' + str(mv_name)+'.mp4')
    os.remove(mv_dir)
    os.remove(mv_dir_2)

if __name__=='__main__':
    im_dir = ('C:/Users/73497/Desktop/photo1/test3')
    fps = 20  # 保存视频的FPS，可以适当调整
    VideoName = '123'
    save_dir = 'C:/Users/73497/Desktop/photo1/test3/123'
    CompositeVideo(im_dir,save_dir,VideoName,fps,3)
