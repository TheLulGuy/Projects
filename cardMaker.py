import pyautogui
from time import sleep

sign = '♣'
sleep(1)
print('6')
sleep(1)
print('5')
sleep(1)
print('4')
sleep(1)
print('3')
sleep(1)
print('2')
sleep(1)
print('1')
for item in range(10):
    if item == 0:
        pyautogui.typewrite(f"'{sign} A'")
    else:
        pyautogui.typewrite(f"'{sign} {item}'")


