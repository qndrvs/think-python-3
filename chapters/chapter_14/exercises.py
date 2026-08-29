## EXERCISES
class Time:
    """Represents a time of day."""
def make_time(hour, minute, second):
    time = Time()
    time.hour = hour
    time.minute = minute
    time.second = second
    return time
def int_to_time(seconds):
    minute, second = divmod(seconds, 60)
    hour, minute = divmod(minute, 60)
    return make_time(hour, minute, second)
def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

# 2. Exercise 2
def subtract_time(time1: object, time2: object) -> int:
    seconds1: int = time_to_int(time1)
    seconds2: int = time_to_int(time2)
    return abs(seconds1 - seconds2)

# 3. Exercise 3
def is_time_after(time1: object, time2: object) -> bool:
    seconds1: int = time_to_int(time1)
    seconds2: int = time_to_int(time2)
    return seconds1 > seconds2

# 4. Exercise 4
class Date:
    """Represents a year, month, and day"""

def make_date(year: int, month: int, day:int) -> object:
    date: object = Date()
    date.year = year
    date.month = month
    date.day = day
    return date

def print_date(date):
    print(f"{date.year}-{date.month:02d}-{date.day:02d}")

def date_to_tuple(date):
    return (date.year, date.month, date.day)
def is_date_after(date1, date2):
    return date_to_tuple(date1) > date_to_tuple(date2)