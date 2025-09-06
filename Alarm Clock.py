import pygame
import time
import datetime

pygame.mixer.init()

current_time=datetime.datetime.now().strftime("%H:%M:%S")

sound_track="Purple Desire - The Grey Room _ Clark Sims.mp3"


alarm_time=input("Enter the time to set alarm(HH:MM:SS): ")

if alarm_time<current_time:
    print("The time has already been passed\n")

else:

    print(f"The alarm for {alarm_time} has been set successfully\n")
    
    while True:

        now_time=datetime.datetime.now().strftime("%H:%M:%S")

        print(now_time)

        time.sleep(1)

        if now_time>=alarm_time:
            print("Wake up")
            
            pygame.mixer.music.load(sound_track)
            pygame.mixer.music.play(-1)

            while True:
                stop = input("Press S to stop: ").strip().upper()
                if stop == "S":
                    pygame.mixer.music.stop()
                    print("Alarm stopped")
                    break

            break

                                   

