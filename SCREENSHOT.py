import pyautogui
import pyinput
import os
import pwinput
import time
camera = pyautogui.screenshot()
camera.save(f'fisier_1.png')
constant = "PAROLA"
parola = pwinput.pwinput(prompt='Introdu parola: ', mask='*')
if parola == constant:
    print("Parola corecta")
    time.sleep(5)
    camera = pyautogui.screenshot()
    camera.save('fisier_2.png')
    time.sleep(5)
    camera = pyautogui.screenshot()
    camera.save('fisier_3.png')
    time.sleep(5)
    camera = pyautogui.screenshot()
    camera.save('fisier_4.png')
else:
    print("Parola gresita")

    