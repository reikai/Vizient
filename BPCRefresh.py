# Refreshes any Excel file through BPC.

import pyautogui
import time

l = r'\\filecluster01\dfs\VhaSecure1\ServiceDeliveryFinancials\Performance Services\_2016\Monthly Financials\Consulting'
f = r'Consulting Financials 9+3 V2.xlsx'
save = r'C:\Python Practice 3'

def resume(x):
    # For waiting on other systems or slow systems. Python is -fast-!
    for i in range(x):
        print('Resuming in ' + str(x - i) + ' seconds...')
        time.sleep(1)

def openExcelFile(location, filename):
    # Open Windows Explorer
    print('Opening Windows Explorer.')
    pyautogui.typewrite('winleft')
    resume(1)
    pyautogui.typewrite('Windows Explorer')
    resume(1)
    pyautogui.typewrite('\n')

    # Type in the full file location, force a new instance of Excel by opening an Excel file.
    # This only works if you don't have any instances of Excel open at run time.
    # This probably will need to be reworked.
    print('File location is: ' + location)
    print('File name is: ' + filename)
    fullfilelocation = location + '\\' + filename
    pyautogui.hotkey('alt', 'd')
    pyautogui.typewrite(fullfilelocation)
    pyautogui.typewrite('\n')
    print('Opening file...')


def BPCLogon():
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

