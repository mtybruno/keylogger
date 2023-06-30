from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(2)

def click(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

pic = pyautogui.screenshot(region=(0,0,0,0))
width, height = pic.size

while True:
    images = ['imagem.png'] #screenshots.png of what you're looking for.
    found_image = None

    for image in images:
        if pyautogui.locateOnScreen(image, region=(0,0,0,0), confidence=0.8) is not None:
            found_image = image
            break

    if found_image is not None:
        pyautogui.click(x=0, y=0) #Point and click coordenates.
        print("I can see it")
        time.sleep(1.0)
        #break <= remove # to stop the program when the conditions are true.        
    else:
        print("I can't see it")
        time.sleep(1.0)
