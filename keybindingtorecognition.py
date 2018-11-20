from pyautogui import *
import numpy as m
from object_movement import dirX, dirY

#left and right movement using direction information
#left means going to the left tab on internet
#right means going to the right tab on internet
def f(dirX):
    return {
        'Left':
        pyautogui.hotkey('ctrl', 'shift', 'tab')
        break
        'Right':
        pyautogui.hotkey('ctrl', 'tab')
        break
    }[dirX]
}

#close or far away the camera using depth information
#close means open a new tab on internet
#far means close the current tab on internet
def f(dirD):
    return {
        'Close':
        pyautogui.hotkey('ctrl', 't')
        break
        'Far':
        pyautogui.hotkey('ctrl', 'w')
        break
    }[dirD]
}

#doing a punch with gesture recognition
#you can change between applications
if gesture== "punch"
    pytaugui.hotkey('alt','tab')
    break
