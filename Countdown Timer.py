#Countdown Timer

import time

timer = int(input("How long would you like to set the timer for(in seconds)? "))

# for x in reversed(range(0, timer)):
for x in range(timer, 0, -1):
    seconds = x % 60
    minutes = (int(x/60)) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Your time is up!")

