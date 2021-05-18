import pyautogui, time

msg = input('Enter message: ')
n = input('Enter how many times you want to repeat the message: ')
print('\nNow quickly switch over to your messaging app!')
time.sleep(5)
for item in range(int(n)):
    pyautogui.typewrite(msg)
    pyautogui.press('enter')