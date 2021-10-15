from pyautogui import *
import pyautogui
#from PIL import ImageGrab
#from functools import partial
import time
import win32api, win32con
import keyboard
import os
import os.path

#ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)
os.system("cls" if os.name == "nt" else "clear")

def click(x,y):
    time.sleep(0.01)
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

print('Type "start" to start the Auto Accept.\n')

def AutoAccept(ready):
    try:
        if ready == "start":
            os.system("cls" if os.name == "nt" else "clear")
            print("Auto Accept is Currently Active.\n")
            print('Press "Ctrl + C" to stop the script.\n')

            while keyboard.is_pressed("q") == False:
                t = time.localtime()
                current_time = time.strftime("%H:%M:%S:", t)

                picture = pyautogui.locateOnScreen("accept.png", confidence=0.5)
                if picture != None:
                    saved_mouse_pos = pyautogui.position()
                    click(picture.left+70,picture.top+20)
                    print(current_time,  "Match Accepted!\n")
                    win32api.SetCursorPos(saved_mouse_pos)
                    time.sleep(0.5)
                else:
                    time.sleep(0.5)
        else:
            os.system("cls" if os.name == "nt" else "clear")
            print("Unknown Command:", ready, "\n")
            NewInput = input()
            AutoAccept(NewInput)

    except KeyboardInterrupt:
        os.system("cls" if os.name == "nt" else "clear")
        print("Auto Accept has been Closed.\n")
        pass

if os.path.isfile('accept.png'):
    AutoAccept(input())
else:
    print('"accept.png" is missing. Please make sure to have both files in the same folder.')