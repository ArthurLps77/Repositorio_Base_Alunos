# intalar o pyautogui com o coamndo:
#pip install pyautogui

#crie uma automação que abra automaticação um navegador

# importamos a bibliot4eca para o script em uso
import pyautogui
#'press' é um comando que utilizamos para pressioanar a tecla desejada 
pyautogui.press('win') #para pressionar a tecla windons

#'sleep' é um comando que utilizamos para deixar o codigos
# em espera por alguns segundos
pyautogui.sleep(1)

#'write' é um comando que utilizamos  para passar o que queremos 
#escrever 
pyautogui.write('Gogle chome')
pyautogui.press('Enter')