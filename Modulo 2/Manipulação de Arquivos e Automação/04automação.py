#Crie umas automação que escreva um texto automaticamente 

import pyautogui
import time

#OBS: abra um bloco de notas vazio
# Aguarde alguns segundos para voce abrir
time.sleep(5)

#escreva o texto
pyautogui.write('Furar moleiras é divertido', interval=0.1 )