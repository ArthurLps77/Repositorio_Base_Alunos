# Automação de login ficticio
#Ideia: Prencher automaticamente o formulario (HTML)

import pyautogui, time # outra maneirade escrever 
time.sleep(3)
pyautogui.write("alunopython", interval=0.1)
pyautogui.press('tab')
pyautogui.write("senha123", interval=0.1)
pyautogui.press('enter')
