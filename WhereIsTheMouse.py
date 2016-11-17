#! python3
# Find the X,Y location of the mouse and prints it to the screen.

import pyautogui
import time
print('Press CTRL + C to quit.')


try:
    while True:
        # Get the mouse coordinates.
        x, y = pyautogui.position()
        print('Mouse is currently at ' + str(x) + ', ' + str(y))
        time.sleep(1)

except KeyboardInterrupt:
    print('\nDone.')

