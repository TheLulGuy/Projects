import pyautogui, time

msg = input('Enter message: ')
n = input('Enter how many time you want to send the message: ')
time.sleep(5)
for item in range(int(n)):
    pyautogui.typewrite(msg, interval=0)
    pyautogui.press('enter')
