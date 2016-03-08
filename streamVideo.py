
import cv2
import urllib
import numpy as np
import pywin
import win32gui

#stream1Url = 'rtsp://192.168.1.10:554/user=admin_password=d2gNs1nj_channel=1_stream=0.sdp?real_stream'
#stream2Url = 'C:\Users\waydeb\Documents\NjordONE\Wildlife.wmv'

vcap = cv2.VideoCapture('rtsp://192.168.1.10:554/user=admin_password=d2gNs1nj_channel=1_stream=0.sdp?real_stream')
#vcap = cv2.VideoCapture('Wildlife.wmv')


CroppedImgX = 500
CroppedImgY = 300

while(1):
    print vcap.isOpened()
    ret, frame = vcap.read()
    print vcap.get(4)
    print vcap.get(3)

    #read width and height of video feed
    streamWidth = vcap.get(3)
    streamHeight = vcap.get(4)

    #test upper limit
    #streamWidth = 1600
    #streamHeight = 1000

    #get curser position X-[0] 0-1600 left-right Y-[1] 0-1000 top-bottom
    cursorPos = win32gui.GetCursorPos()
    #print cursorPos[0]
    #print cursorPos[1]
    X1 = cursorPos[0]-CroppedImgX/2
    X2 = cursorPos[0]+CroppedImgX/2
    Y1 = cursorPos[1]-CroppedImgY/2
    Y2 = cursorPos[1]+CroppedImgY/2

    #limit extreme and subzero values.
    if X1 < 0:
        X1 = 0
        X2 = CroppedImgX
    elif X2 > streamWidth:
        X1 = streamWidth-CroppedImgX
        X2 = streamWidth
    if Y1 < 0:
        Y1 = 0
        Y2 = CroppedImgY
    elif Y2 > streamHeight:
        Y1 = streamHeight-CroppedImgY
        Y2 = streamHeight

    print X2
    
    #Crop the image crop = vis[y1:y2,x1:x2]  y2>y1 & x2>x1

    crop = frame[Y1:Y2,X1:X2]

    stitched = np.hstack((crop,crop))
    cv2.imshow('frame1', stitched)
    #cv2.imshow('frame2', crop)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

vcap.release()
cv2.destroyAllWindows()
