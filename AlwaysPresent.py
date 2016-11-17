#! python3
# This program simply nudges the mouse continuously to show that the user is 'active.'
# Use a keyboard interrupt to stop the program.

import pyautogui
import sys
import os
import time

print('Beginning mouse movement. Press CTRL + C to interrupt.')
try:
    while True:
        print('Hello World!')
        # pyautogui.moveRel(10, 0, duration=0.25)
        # pyautogui.moveRel(-10, 0, duration=0.25)
        time.sleep(2)
except KeyboardInterrupt:
    print('INTERRUPPEN')