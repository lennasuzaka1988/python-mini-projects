import psutil

battery_level = psutil.sensors_battery()
plug = battery_level.power_plugged
percentage = str(battery_level.percent)
plug = 'Plugged In' if plug else 'This is not plugged in.'
print(percentage + '% | ' + plug)
