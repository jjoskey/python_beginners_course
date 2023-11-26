import datetime

utc_time = datetime.datetime.now(datetime.UTC)
print(utc_time)  # Output will be in the format: YYYY-MM-DD HH:MM:SS.ssssss

current_datetime = datetime.datetime.now()
print(current_datetime)  # Output will be in the format: YYYY-MM-DD HH:MM:SS.ssssss
print(current_datetime.isoformat())  # Output will be in the format: YYYY-MM-DDTHH:MM:SS.ssssss
print(current_datetime.year)  # Output will be in the format: YYYY
print(current_datetime.month)  # Output will be in the format: MM
print(current_datetime.day)  # Output will be in the format: DD
print(current_datetime.hour)  # Output will be in the format: HH
print(current_datetime.minute)  # Output will be in the format: MM
print(current_datetime.second)  # Output will be in the format: SS
print(current_datetime.microsecond)  # Output will be in the format: ssssss

some_datetime = datetime.datetime(year=2021, month=5, day=1, hour=12, minute=30, second=15, microsecond=123456)
print(some_datetime)  # Output will be in the format: YYYY-MM-DD HH:MM:SS.ssssss

current_date = datetime.date.today()
print(current_date)  # Output will be in the format: YYYY-MM-DD

current_datetime = datetime.datetime.now()
current_date = current_datetime.date()
print(current_date)  # Output will be in the format: YYYY-MM-DD


day_ago = current_datetime - datetime.timedelta(days=1)
print(day_ago)  # Output will be in the format: YYYY-MM-DD HH:MM:SS.ssssss


current_datetime = datetime.datetime.now()
current_datetime.strftime("%A, %d %B %Y")  # Output will be in the format: Monday, 01 March 2021

isoformat = "2023-08-07T20:15:30.384294"
my_datetime = datetime.datetime.fromisoformat(isoformat)
print(type(my_datetime))  # Output will be: <class 'datetime.datetime'>
print(my_datetime)  # Output will be in the format: 2023-08-07 20:15:30.384294
