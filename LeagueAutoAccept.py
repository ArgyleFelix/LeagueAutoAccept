from pyautogui import *
import pyautogui
import time
import win32api, win32con
from termcolor import colored
import keyboard
import os
import os.path

start_time = time.time()
os.system("cls" if os.name == "nt" else "clear")

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def time_converter(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print("Program was running for {0}h:{1}m:{2}s".format(int(hours),int(mins),int(sec)))

print(colored("Auto Accept is Currently Offline.", "red"))
print("Currently this script only supports the main monitor.")
print("Make sure that you game is on the main monitor.\n")
print("The failsafe key is Numpad 5.")
print("If you lose control of your mouse you can hold it to close the script.\n")
print('Press "Ctrl + C" to stop the script.')
print('Type "start" to start the Auto Accept.\n')

def AutoAccept(ready):
    try:
        if ready == "start":
            os.system("cls" if os.name == "nt" else "clear")
            print(colored("Auto Accept is Currently Active.", "green"))
            print("The failsafe key is Numpad 5.\n")
            print('Press "Ctrl + C" to stop the script.\n')

            while keyboard.is_pressed("num 5") == False:
                t = time.localtime()
                current_time = time.strftime("%H:%M:%S:", t)
                picture = pyautogui.locateOnScreen("accept.png", confidence=0.5)
                if picture != None:
                    saved_mouse_pos = pyautogui.position()
                    click(picture.left+70,picture.top+20)
                    print(current_time,  "Match Accepted")
                    win32api.SetCursorPos(saved_mouse_pos)
                    time.sleep(0.5)
                else:
                    time.sleep(0.5)
        else:
            os.system("cls" if os.name == "nt" else "clear")
            print("Unknown Command:", ready, "\n")
            print('Type "start" to start the Auto Accept.')
            print('Press "Ctrl + C" to stop the script.\n')
            NewInput = input()
            AutoAccept(NewInput)

    except KeyboardInterrupt:
        os.system("cls" if os.name == "nt" else "clear")
        print(colored("Auto Accept has been Closed.\n", "red"))
        end_time = time.time()
        time_lapsed = end_time - start_time
        time_converter(time_lapsed)
        pass

if os.path.isfile("accept.png"):
    AutoAccept(input())
else:
    print('"accept.png" is missing. Please make sure to have both files in the same folder.')