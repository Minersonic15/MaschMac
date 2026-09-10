import pyautogui
import time
import random

pyautogui.PAUSE = 0.1  
while 0:
    time.sleep(1)
    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)
    time.sleep(1)
    print(pyautogui.position())

def RandomizeClick(RandLocs):
    time.sleep(0.25)
    #pyautogui.click(500, random.choice(RandLocs))
    pyautogui.click(500, RandLocs)

def SetSS(Name):
    return pyautogui.locateOnScreen(f'{Name}.png', confidence=0)
Start = SetSS("Start")
Submit1 = SetSS("Submit1")
Submit2 = SetSS("Submit2")
Assessment = SetSS("Assessment")
Quiz = SetSS("Quiz")
List = SetSS("List")
Begin = SetSS("Begin")

time.sleep(3)

pyautogui.click(1166,421)

#RandomizeClick([407, 450])
#RandomizeClick([630, 680])
#RandomizeClick([845, 880])
star = False
Sub1 = False
Sub2 = False
Ass = False
quiz = False
Beg = False
lis = False

while Beg == False:
    if not star:
        if Start is None:
            continue
        else:
            Star = True
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

            time.sleep(3)
    #submit2
    if not Sub1:
        if Submit1 is None:
            continue
        else:
            Sub1 = True
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
            time.sleep(2)

    #sub
    if not Sub2:
        if Submit2 is None:
            continue
        else:
            Sub2 = True
            pyautogui.click(722, 780)
            time.sleep(4)


    #Assessment
    if not Ass:
            if Assessment is None:
                continue
            else:
                Ass = True
                pyautogui.click(1248, 357)
                time.sleep(1)

    #Quizzes
    if not quiz:
        if Quiz is None:
            continue
        else:
            quiz = True
            pyautogui.click(877, 358)
            time.sleep(2)

    #select
    if not lis:
        if List is None:
            continue
        else:
            lis = True
            pyautogui.click(262, 744)
            time.sleep(2)

    #start
    if not Beg:
        if Begin is None:
            continue
        else:
            Beg = True
            pyautogui.click(222, 916)
            time.sleep(3)
    star = False
    Sub1 = False
    Sub2 = False
    Ass = False
    quiz = False
    Beg = False
    lis = False