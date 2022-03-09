from datetime import datetime
from playsound import playsound

# alarm_input = input('Please input the alarm time: ')
# find way to use os to detect time

target_time_hour = 5
target_time_minute = 15

datetime.now().time().hour == target_time_hour
datetime.now().time().minute == target_time_minute

if current_time_hour and current_time_minute == target_time:
    print('It\'s time!')


# if the time matches alarm time, play a sound
# https://pypi.org/project/DateTime/#id1
# https://docs.python.org/3/library/os.path.html
# os.path.getctime(path)