from datetime import datetime, date, timedelta

utc_time = datetime.utcnow()
print(utc_time)  # Output will be in the format: YYYY-MM-DD HH:MM:SS.ssssss

# Get the current date and time
current_datetime = datetime.now()
print(current_datetime)  # Output will be in the format: YYYY-MM-DD HH:MM:SS.ssssss
print(current_datetime.isoformat())
print(current_datetime.year)
print(current_datetime.month)
print(current_datetime.day)
print(current_datetime.hour)
print(current_datetime.minute)
print(current_datetime.second)
print(current_datetime.microsecond)

# some other datetime
some_datetime = datetime(year=2021, month=5, day=1, hour=12, minute=30, second=15, microsecond=123456)
print(some_datetime)

# get the current date
current_date = current_datetime.date()
print(current_date)  # Output will be in the format: YYYY-MM-DD
current_date = date.today()
print(current_date)  # Output will be in the format: YYYY-MM-DD

# get datetime day ago
day_ago = datetime.now() - timedelta(days=1)
print(day_ago)  # Output will be in the format: YYYY-MM-DD HH:MM:SS.ssssss

# formatting datetime ot string "The 1st of May"
may_day = datetime(year=2021, month=5, day=1)
print(may_day.strftime("%A, %d %B %Y"))

# datetime from string

# 1. fromisoformat
my_datetime = datetime.fromisoformat("2023-08-07T20:15:30.384294")
print(my_datetime)

# 2. strptime
my_datetime = datetime.strptime("2023-08-07 20:15:30", "%Y-%m-%d %H:%M:%S")
print(my_datetime)
