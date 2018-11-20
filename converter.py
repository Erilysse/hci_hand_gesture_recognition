#converter BSR colors in HSV colors
import sys
import numpy as np
import cv2

blue = sys.argv[1]
green = sys.argv[2]
red = sys.argv[3]  

color = np.uint8([[[blue, green, red]]])
hsv_color = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)

hue = hsv_color[0][0][0]

#lower bound is the minimum shade of of the color that will be detected
print("Lower bound is :"),
print("[" + str(hue-10) + ", 100, 100]\n")

#upper bound is the maximum shade of the color that will be detected
print("Upper bound is :"),
print("[" + str(hue + 10) + ", 255, 255]")