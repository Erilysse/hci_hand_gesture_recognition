from pyautogui import *
pyautogui.PAUSE = 2.5
import numpy as m
from object_movement import dirX, dirY

#left and right movement using direction information
#left means going to the left tab on internet
#right means going to the right tab on internet

if dirX == "Left":
    pyautogui.hotkey('ctrl', 'shift', 'tab')
else:
    pyautogui.hotkey('ctrl', 'tab')
    
#close or far away the camera using depth information
#close means open a new tab on internet
#far means close the current tab on internet
"""if dirD == "Close":
    pyautogui.hotkey('ctrl', 't')
else:
        pyautogui.hotkey('ctrl', 'w')

#doing a punch with gesture recognition
#you can change between applications
if gesture == "punch":
    pytaugui.hotkey('alt','tab')
"""