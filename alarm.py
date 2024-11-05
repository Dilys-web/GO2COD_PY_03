import time
from datetime import datetime, timedelta
import pygame

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time.strftime('%H:%M:%S')}")
    while True:
        current_time = datetime.now()
        if current_time >= alarm_time:
            print("Alarm ringing!")
            try:
                pygame.mixer.pre_init(44100, -16, 2, 2048)
                pygame.init()
                pygame.mixer.init()
                pygame.mixer.music.load('alarm1.wav')  # Load your sound file
                pygame.mixer.music.load('Loud_Alarm_Clock_Buzzer.wav')
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    time.sleep(1)
            except pygame.error as e:
                print(f"Error playing sound: {e}")
            break
        time.sleep(1)

if __name__ == "__main__":
    # Set the alarm time (24-hour format)
    alarm_hour = int(input("Enter hour (0-23): "))
    alarm_minute = int(input("Enter minute (0-59): "))
    alarm_second = int(input("Enter second (0-59): "))

    # Create a datetime object for the alarm time
    alarm_time = datetime.now().replace(hour=alarm_hour, minute=alarm_minute, second=alarm_second, microsecond=0)

    # If the time is in the past, set it for the next day
    if alarm_time < datetime.now():
        alarm_time += timedelta(days=1)

    set_alarm(alarm_time)
