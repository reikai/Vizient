#! python3
# This is a test for multithreaded programs.

import threading
import time

print('Start of program.')

def takeANap():
    time.sleep(5)
    print('WAKE UP')

threadObj = threading.Thread(target=takeANap)
threadObj.start()

print('End of program.')