# Comando para encontra a posição X e Y do mouse para a auto automação 
import pyautogui
import time

print('Voce tem 5 segundos para posicionar o mouse sobre o botão de escrever')
time.sleep(5)
print("Posicão do mouse", pyautogui.position())
