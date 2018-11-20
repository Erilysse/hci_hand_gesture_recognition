import numpy as np
import cv2
# import C:/Program Files/SoftKinetic/DepthSenseSDK/ as dsc
import DepthSenseSDK as dsc

device = CAP_OPENNI
capture = VideoCapture(device)

if not(capture.isOpened(device)):
    capture.open(device)
    break

#allow camera or video file to warm up
time.sleep(2.0)

while True:
    #read the image we want to analyze and change it in HSV
    frame= dsc.read()
    frame= frame[1]
    if frame is None:
        break
    #resize frame, blurt it, convert it to the HSV
    #color space
    frame = 
    blurred = cv2.GaussianBlur(frame, (11,11),0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    #find lower and upper range of HSV, the number are the color of the marker converted in HSV (run python convert.py (number of each in BGR))
    #construct a mask for the color of the marker, then perform
    #a serie of dilations and erosions to remove any small
    #blobs left in the mask
    lowerr = np.array([169, 100, 100], dtype=np.uint8)
    upperr = np.array([189, 255, 255], dtype=np.uint8)
    mask = cv2.inRange(hsv, lowerr,upper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    #find contours in the mask and initialize the current
    #(x,y) center of the marker
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] ou [1]
    center = None
cv2.imshow('mask',mask)
cv2.imshow('image', img)


""""
for
Mat depthMap
Mat bgrImage

capture.retrieve(depthMap, CAP_OPENNI_DEPTH_MAP)
capture.retrieve(bgrImage, CAP_OPENNI_BGR_IMAGE)
"""

while(1):
  k = cv2.waitKey(0)
  if(k == 27):
    break

cv2.destroyAllWindows()