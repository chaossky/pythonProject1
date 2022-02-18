import time
import pyautogui
import pyperclip

# data = open('test_sample.txt', 'r', encoding='utf8')
# data = open('intro.txt', 'r', encoding='utf8')
data = open('gumjung.txt', 'r', encoding='utf8')
# data = open('article001.txt', 'r', encoding='utf8')
# data= open('카테고리.txt', 'r', encoding='utf8')
# data = open('전기기사.txt', 'r', encoding='utf8')
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
    # if str_list[i] == '\\' and str_list[i + 1] == "n":
    #     pyautogui.hotkey('enter')
    #     pyperclip.copy(str_list[i])
    #     # pyautogui.hotkey('space')
    #     pyautogui.hotkey('ctrl', 'v')
    # if str_list[i - 1] == '\\' and str_list[i] == 'n':
    #     pass
    else:
        pyperclip.copy(str_list[i])
        pyautogui.hotkey('space')
        pyautogui.hotkey('ctrl', 'v')

# for i in range(len(str_list)):
#     time.sleep(0.1)
#     if "." in str_list[i]:
#         pyperclip.copy(str_list[i])
#         pyautogui.hotkey('ctrl', 'v')
#         pyautogui.hotkey('enter')
#     else:
#         pyperclip.copy(str_list[i])
#         pyautogui.hotkey('space')
#         pyautogui.hotkey('ctrl', 'v')
