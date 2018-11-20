import numpy
import cv2
import "camera"
import wx

device = cv2.cv.CV_CAP_OPENNI
capture = cv2.VideoCapture(device)

if not(capture.isOpened(device)):
    capture.open(device)
    break

capture.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 480)

depth, timestamp = "camera".sync_get_depth()
cv2.imshow("depth", depth)

app= wx.App()
layout= 
layout=Show(True)
app.MainLoop()