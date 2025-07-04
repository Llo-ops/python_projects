import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")

    is_alarm_running = True


    while is_alarm_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        time.sleep(1)
        print(f"The time right now is: {current_time}")
        sound_file = "Digital Watch Alarm Long.mp3"

        if current_time == alarm_time:
            print("Wake UP!")

            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)

            is_alarm_running = False

def main():
        alarm_time = input("Set your alarm (HH:MM:SS): ")
        set_alarm(alarm_time)
main()