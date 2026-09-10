import pyautogui
import time
import random

#pyautogui.PAUSE = 0.1  
while 0:
    time.sleep(1)
    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)
    time.sleep(1)
    print(pyautogui.position())
def SetSS(Name):
    return pyautogui.locateOnScreen(f'{Name}.png', confidence=0)
def RandomizeClick(RandLocs):
    time.sleep(0.25)
    #pyautogui.click(500, random.choice(RandLocs))
    pyautogui.click(500, RandLocs)

Link = "https://ldcsb.elearningontario.ca/d2l/lms/quizzing/user/quiz_summary.d2l?qi=12013872&ou=29333976"
pyautogui.click(1166,421)


while True:
    RandomizeClick(435)
    RandomizeClick(630)
    RandomizeClick(830)

    time.sleep(0.1)

    pyautogui.click(1314, 910)

    #RandomizeClick([422, 464])
    #RandomizeClick([622, 670])

    RandomizeClick(415)
    RandomizeClick(640)

    #submit
    time.sleep(0.5)
    pyautogui.click(475, 788, duration=0.1)
    time.sleep(1)
    pyautogui.click(475, 788)

    time.sleep(2)

    #Sub2
    pyautogui.click(432, 475)
    time.sleep(0.1)
    pyautogui.click(400, 792)

    time.sleep(0.1)
    pyautogui.click(400, 750)
    time.sleep(0.1)
    pyautogui.click(400, 708)
    time.sleep(0.1)
    pyautogui.click(400, 665)
    time.sleep(0.1)
    pyautogui.click(400, 633)
    time.sleep(0.1)

    pyautogui.click(655, 100)
    time.sleep(0.1)
    pyautogui.hotkey('command', 'a')
    time.sleep(0.1)
    pyautogui.write(Link)
    time.sleep(0.1)
    pyautogui.hotkey('enter')

    time.sleep(2)
    pyautogui.click(222, 916)
    time.sleep(2)
