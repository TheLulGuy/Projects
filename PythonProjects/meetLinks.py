import webbrowser
import sys, time, random
from datetime import datetime


chem = ['https://classroom.google.com/u/1/c/MzQwMjY0MDg2NTg5', 'Chemistry']
phy = ['https://classroom.google.com/u/1/c/MzQwMjY0MDg2NTU5', 'Physics']
bio = ['https://classroom.google.com/u/1/c/MzQwMjg1MTQzNzMz', 'Biology']
eng = ['https://classroom.google.com/u/1/c/MzQwMjc5MDM3NTcy', 'English']
math = ['https://classroom.google.com/u/1/c/MzQwMjc5MDUwNTM5', 'Mathematics']
fre = ['https://classroom.google.com/u/1/c/MzQwMjc5MDM3NjQw', 'French']
his = ['https://classroom.google.com/u/1/c/MzQwMjc5MDM3Njc0', 'History']
geo = ['https://classroom.google.com/u/1/c/MzQwMjc5MDUwNTIy', 'Geography']
comp = ['https://classroom.google.com/u/1/c/MzQwMjY4MjkyNjc2', 'Computer']


mon = [eng, math, chem, fre, his, geo]
tue = [math, fre, chem, bio, phy, chem]
wed = [eng, math, his, phy, math, math]
thurs = [bio, eng, phy, geo, eng, eng]
fri = [comp, math, his, eng, bio, fre]
sat = [geo, comp, his]


timetable = [
    mon,
    tue,
    wed,
    thurs,
    fri,
    sat
]

flag = False
override = False

try:
    subject = sys.argv[1]
    if subject == 'table' or subject == 'timetable':
        today = datetime.today()
        weekday = today.weekday()
        for index, item in enumerate(timetable[weekday], start=1):
            print(f'{index} - {item[1]}')
        exit(0)
    elif subject == 'tableall':
        for day in timetable:
            for subject in day:
                print(subject[1], end=" ")
            print()

        exit(0)
    elif subject == 'override':
        override = True
    else:
        raise IndexError

except IndexError:
    pass

def choose(n):
    now = datetime.now()
    weekday = now.weekday()
    print('\nEntering {} class....'.format(timetable[weekday][n][1]))
    time.sleep(1)
    return timetable[weekday][n][0]

def click():
    time.sleep(7)
    pyautogui.moveTo(300, 300)
    time.sleep(1)
    pyautogui.click()


def closeWindow():
    time.sleep(1.5)
    pyautogui.hotkey('command', 'alt', 'left')
    pyautogui.hotkey('command', 'w')

def search(item):
    webbrowser.open_new(item)

def closeVideoMic():
    time.sleep(7)
    pyautogui.moveTo(370, 640)
    pyautogui.click()
    pyautogui.moveTo(440, 640)
    pyautogui.click()

def autoSelection():
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    if override:
        return choose(random.randint(0, 5))

    elif hour == 8 and minute >= 45:
        return choose(0)

    elif hour == 9 and minute >= 0:
        return choose(0)

    elif hour == 10 and minute >= 0:
        return choose(1)

    elif hour == 11 and minute >= 0:
        return choose(2)

    elif hour == 12 and minute >= 0:
        return choose(3)

    elif hour == 13 and minute >= 30:
        return choose(4)

    elif hour == 14 and minute >= 30:
        return choose(5)

    elif hour >= 15 and minute >= 10:
        print('classes have ended')
        exit(0)

import pyautogui
search(autoSelection())
click()
closeWindow()
closeVideoMic()
