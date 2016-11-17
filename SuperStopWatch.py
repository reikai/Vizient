#! python3
# It's a stopwatch. Press enter to start and/or lap. CTRL + C to quit.

import time

# Display instructions.
print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
input()     # Press ENTER to begin
print('Started.')
startTime = time.time()
lastTime = startTime
lapNum = 1

# Start tracking the lap times:

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print(' Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time()  # Reset the reference point for lap times.
except KeyboardInterrupt:
    # Handle the Ctrl+C exception to keep its error message from displaying.
    print('OOPS')

