current_time = input("What time is it now")
time_current = int(current_time)
alarm_time = input("What is the alarm time")
time_alarm = int(alarm_time)
go_off = (time_alarm % 24) + time_current
print(go_off)