import cv2 as cv
import urllib
import numpy as np


vcap = cv.VideoCapture("rtsp://192.168.1.10:554/user=admin_password=d2gNs1nj_channel=1_stream=0.sdp?real_stream")
while(1):
    ret, frame = vcap.read()
    print vcap.get(4)
    print vcap.get(3)
    cv.imshow('frame', frame)
    if cv.waitKey(1) & 0xFF ==ord('q'):
        break

"""

CvCapture *camera = cvCreateFileCapture("rtsp://184.72.239.149/vod/mp4:BigBuckBunny_115k.mov");
if (camera == NULL) {
 printf("video is null, aborting...");
 return -1;
}
else{
 printf("video ok");
}

cv::VideoCapture vcap;
//open the video stream and make sure it's opened
if(!vcap.open("rtsp://184.72.239.149/vod/mp4:BigBuckBunny_115k.mov")) {
    std::cout << "Error opening video stream or file" << std::endl;
    return -1;
}

cv::VideoCapture capture("rtsp://192.168.1.10:554/user=admin_password=d2gNs1nj_channel=1_stream=0.sdp?real_stream");

if (!capture->isOpened()) {
    //Error
}


cv::namedWindow("TEST", CV_WINDOW_AUTOSIZE);

cv::Mat frame;

while(m_enable) {
    if (!capture->read(frame)) {
        //Error
    }
    cv::imshow("TEST", frame);

    cv::waitKey(30);
}
"""
