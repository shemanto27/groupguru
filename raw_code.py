import pyautogui
import time

groups = ['germany.econsultancybd','1065023467469160','BSFG1']

time.sleep(5)

pyautogui.keyDown('ctrl')
pyautogui.keyDown('t')
pyautogui.keyUp('t')
pyautogui.keyUp('ctrl')

for i in range(len(groups)):
    link = 'https://facebook.com/groups/'+groups[i]
    pyautogui.typewrite(link)
    pyautogui.typewrite('\n')

    print("Waiting for 45 seconds\n")
    time.sleep(3)

    pyautogui.typewrite('p')
    time.sleep(2)
    print("Writing post\n")
    pyautogui.typewrite("Can anyone suggest me resources to know about study in Germany?")
    time.sleep(4)

    pyautogui.moveTo(907, 878)
    pyautogui.click(button='left')

    time.sleep(3)

    pyautogui.write(['f6'])
    time.sleep(1)


