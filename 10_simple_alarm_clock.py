#alarm clock

import time, datetime

def set_alarm():
    current_time=datetime.datetime.now().strftime("%H:%M:%S")
    print(f"Current time is: {current_time}")

    alarm_time = input("Enter alarm time in HH:MM:SS format: ")

    while True:
        current_time=datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Current time is: {current_time}",end="\r")
        if current_time==alarm_time:
            print("\nAlarm! Time's up!")
            break
        time.sleep(1)
set_alarm()