
import cv2
import urllib
import numpy as np

stream1Url = 'rtsp://192.168.1.10:554/user=admin_password=d2gNs1nj_channel=1_stream=0.sdp?real_stream'
stream2Url = 'rtsp://192.168.1.10:554/user=admin_password=d2gNs1nj_channel=1_stream=0.sdp?real_stream'

vcap = cv2.VideoCapture(stream1Url)

while(1):
    #print vcap.isOpened()
    ret, frame = vcap.read()
    #print vcap.get(4)
    #print vcap.get(3)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

