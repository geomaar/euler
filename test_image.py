import pyautogui    
import time         
from PIL import Image 
import os


im = Image.open(r'C:\users\maria\desktop\download.jpg')
# location = pyautogui.locateOnScreen(im)
# centro = pyautogui.center((location.left,location.top,location.width,location.height))
# pyautogui.click(centro.x, centro.y)
print(type(im))