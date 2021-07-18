import pyautogui ,  time 

time.sleep(5)

file = open("send.txt","r")


# we can also use emotes 


for word in file:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    time.sleep(1)

