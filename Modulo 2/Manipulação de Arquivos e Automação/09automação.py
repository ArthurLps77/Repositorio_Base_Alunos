import pyautogui
import time

pyautogui.press("win")
time.sleep(1)
pyautogui.write("Desenho com pyautogui")
pyautogui.press("enter")
time.sleep(2)

deadsec = [
   ' ⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀',
'⠀⣏⠉⠩⠥⢄⡔⠉⢸⣦⠤⠄⢀⣀⠀⠀⠀⠀⠀⠀⠀',
'⠀⢹⢰⠀⢰⡟⠀⠰⠘⣟⣳⡉⠓⠒⠪⠴⣂⠄⡀⠀⠀',
'⠀⠈⡄⡆⣦⣿⣾⡻⣿⣾⡿⣃⠀⠀⠀⠀⠀⠈⠉⠲⠄',
'⠀⠃⢀⡗⣿⡯⡛⢫⣽⣿⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀',
'⠀⠸⠈⣷⣿⣿⣭⣤⣿⣃⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀',
'⠀⢠⠔⢘⣆⢻⣳⡻⣿⣿⡧⠉⠉⡸⠒⣢⡀⠀⠀⠀',
'⠀⣠⠿⠠⣼⣿⠜⣿⡚⢽⣿⣡⡪⣸⣣⠀⠈⢻⠀⠀',
'⠀⡔⣇⣤⣶⡟⠙⣧⢫⢚⣲⣿⣿⣗⢊⣤⡶⡄⢈⠇⠀',
'⢸⠰⢈⣿⣦⡔⣾⣿⣿⠏⢠⣽⠟⡡⠂⢹⣷⠇⢸⠇⠀',
'⢠⢃⣥⣼⠋⡟⡉⠘⣿⡏⡿⠿⣿⣍⠠⣀⢹⢻⠂⡏⠰⠀',
'⢸⠊⢉⠌⢸⠱⡴⣷⣾⣿⢰⣾⣀⣀⠨⢋⣿⠀⢴⡇⡄⠀⠀',
'⠈⠣⣻⠶⠷⠀⢠⠈⣇⢸⡚⣋⣩⠐⠁⣿⣩⣊⠌⢁⡇⠀⠀⠀',
'⠉⠉⣷⣶⣇⣿⣿⢧⢹⠫⡄⣠⣿⣟⠓⠋⡌⠇⠀⠀⠀⠀',
'⢹⣹⣿⢿⣿⣿⡜⣽⡟⢸⠟⢠⣴⢢⣿⠀⠀⠀⠀⠀',
]
for linha in deadsec:
    pyautogui.write(linha,interval=0.1)
    pyautogui.press('enter')
    print('DEADSEC!!')
