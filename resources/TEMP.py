import pyautogui as p
import time

def open_firefox():
    p.hotkey("win","r")
    time.sleep(1)
    p.typewrite("firefox")
    p.press("enter")
    time.sleep(1)

def open_website():
    p.typewrite("youtube.com")
    time.sleep(1)
    p.press("enter")
    time.sleep(1)

if __name__=="__main__":
    open_firefox()
    open_website()
