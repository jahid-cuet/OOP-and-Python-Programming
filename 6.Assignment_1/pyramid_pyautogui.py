import pyautogui
from time import sleep
sleep(10)
n = int(input())
for i in range(1,n+1):
    pyautogui.write('#' *i,interval=0.25)
    pyautogui.press('enter')

#
##
###
####
#####
#







