import datetime

date = datetime.date(2026, 12, 12)
today = datetime.date.today()

time = datetime.time(6, 30, 40)
now = datetime.datetime.now()

now = now.strftime("%H:%M:%S , %d-%m-%Y")

target_datetime = datetime.datetime(2026, 2, 6, 15, 30, 0)
current_datetime = datetime.datetime.now()

if target_datetime == current_datetime:
    print("You are just on the target date.")
elif target_datetime < current_datetime:
    print("You passed the target date.")
elif target_datetime > current_datetime:
    print("Oh dear! The target date is far.")

