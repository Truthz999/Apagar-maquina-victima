# Apagar-maquina-victima
**Abre el terminal de Windows y apaga la maquina victima**


# Code

```python

# Importamos los modulos que usaremos

import pyautogui
import time

pyautogui.press("win")
time.sleep(1.5)

pyautogui.write("cmd")
pyautogui.press("enter")

time.sleep(2)

pyautogui.write("shutdown -s -t 2") 
pyautogui.press("enter")
