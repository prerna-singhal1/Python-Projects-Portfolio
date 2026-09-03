#Python Alarm Clock

import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

import time
import datetime
import pygame



def set_alarm(alarm_time):
    print(f"Your alarm time is {alarm_time}")
    sound_file = "alarm music.mp3"
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print("WAKE UP!🌞")

            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)

            is_running = False

        time.sleep(1)

def main():
    alarm_time = input("When would you like to set your alarm (HH:MM:SS): ")
    set_alarm(alarm_time)

    

if __name__ == "__main__":
    main()

