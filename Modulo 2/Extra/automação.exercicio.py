import pyautogui, time

pyautogui.hotkey('win', 'r')
time.sleep(0.5)
pyautogui.write('calc\n')
time.sleep(1)
for tecla in ['8', '+', '2', 'enter']:
    pyautogui.press(tecla)
time.sleep(1)
pyautogui.hotkey('alt', 'f4')
