#! python3
# Opens a specified directory, opens the first Excel file in that directory, and refreshes the workbook.

import pyautogui
import time

location = 'C:\Python Practice 3'
filename = ''

def resume(x):
    for i in range(x):
        print('Resuming in ' + str(x - i) + ' seconds...')
        time.sleep(1)

# Safety so you have time to execute the program and forget about life for a while
print('Please don\'t touch the mouse or keyboard.')
for i in range(5):
    print('Starting in ' + str(5 - i) + ' seconds...')

# Open Start Menu.
print('Opening Start Menu...')
pyautogui.click(27, 1029)

# Open Excel.
print('Opening Excel...')
pyautogui.click(139, 515)
print('Waiting for Excel to finish loading...')
resume(7)
print('Excel is open.')

# Log on to BPC so we can refresh Excel workbooks.
print('Changing to EPM Tab...')
pyautogui.click(612, 35)
print('Clicking log on...')
pyautogui.click(33, 70)
print('Waiting on logon dialog box...')
resume(10)
print('Logging on...')
pyautogui.click(732, 631)
# In case the system is busy that day, feel free to shorten
resume(10)

# Open the Open File dialog, navigate to the file location
print('Opening file...')
pyautogui.hotkey('ctrl', 'o')
pyautogui.click(433, 48)
resume(5)
print('Navigating to file location...')
pyautogui.typewrite(location)
pyautogui.typewrite('\n')
# Double Click to open file.
print('Opening first file in folder...')
print('Note: Need to find a better way to open ANY file in the folder, not just the first one.')
time.sleep(5)
pyautogui.doubleClick(429, 140)
time.sleep(5)

# Refresh entire workbook.
print('Refreshing the Excel workbook...')
pyautogui.click(319, 101)
resume(3)
pyautogui.click(389, 196)
resume(30)
print('Workbook has been refreshed.')

# Save the file in the same location.
print('Saving the file...')
pyautogui.click(81, 12)
pyautogui.click(1655, 7)
resume(5)

# Close Excel
print('Closing Excel.')
print('File can be found here: ' + location)
pyautogui.click(1653, 7)











