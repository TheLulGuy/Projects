#! python3
# stopwatch.py - a simple stopwatch program

import time

print('Press ENTER to begin the stopwatch \nPress CTRL-C to quit')
input() # Waits for input

print('Started')
startime = time.time()
lastime = startime
lapnum = 0
try:
    while True:
        input()
        laptime = round(time.time() - lastime, 3) # Time between last time and current time
        totaltime = round(time.time() - startime, 3) # Time between start of timer and now
        print(f'Lap {lapnum}: {laptime} ({totaltime})')
        lapnum += 1
        lastime = time.time() # Reset lastime to start a new lap
except KeyboardInterrupt:
    # To be printed when CTRL-C is pressed
    print('\nStopped')

