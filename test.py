import time
import pyautogui
import pyperclip

data = open('mot000002.txt', 'r', encoding='utf8')
count = 0
lines = data.read()
data.close()

str001 = lines.split(" ")
str_list = (list(str001))

#print(str_list)

time.sleep(4)

for i in range(len(str_list)):
    time.sleep(0.1)
    if str_list[i].count('\\n') > 0:
        pyautogui.hotkey('enter')
        pyperclip.copy(str_list[i])
        pyautogui.hotkey('ctrl', 'v')
    else:
        pyperclip.copy(str_list[i])
        pyautogui.hotkey('space')
        pyautogui.hotkey('ctrl', 'v')
