#include "mainwindow.h"
#include <QApplication>
#include"opencv_modules.hpp"
#include"opencv2/opencv.hpp"

int main(int argc, char *argv[])
{
    using namespace cv;
    Mat image = imread("C:/Users/Pasto/Pictures/Saved Pictures/windows-98-background.jpg");
    QApplication a(argc, argv);
    MainWindow w;
    imshow("output",image);
    w.show();
    return a.exec();
}
