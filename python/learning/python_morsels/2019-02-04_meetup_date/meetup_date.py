# https://www.pythonmorsels.com/exercises/a8ce6ad2f64c4804acd52f9a2de464e8/


from datetime import date, timedelta 
from calendar import Calendar, weekday, monthcalendar, THURSDAY
import calendar
from enum import IntEnum
from itertools import count


Weekday_1 = IntEnum('Weekday', 'MONDAY TUESDAY WEDNESDAY THURSDAY FRIDAY SATURDAY SUNDAY')

WEEKDAY_NAMES = [d.upper() for d in calendar.day_name]
Weekday_2 = IntEnum('Weekday', zip(WEEKDAY_NAMES, count()))


class Weekday(IntEnum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

# My solution

def meetup_date__(year, month, nth=4, weekday=Weekday.THURSDAY):
    if nth < 0:
        month += 1
    d = date(year, month, 1)

    if nth >= 0 and weekday >= d.weekday():
        nth -= 1
    elif nth < 0 and weekday < d.weekday():
        nth += 1

    add_days = weekday - d.weekday()

    return d + timedelta(days=add_days) + timedelta(weeks=nth)


# Solutions

# Helper function for some of the bonus solutions

def weekdays_in_month_1(year, month, weekday):
    """Return list of all 4/5 dates with given weekday and year/month."""
    d = date(year, month, 1)
    d += timedelta(days=(7 + weekday - d.weekday()) % 7)
    first_to_fifth = (
        d + timedelta(days=7)*i
        for i in range(6)
    )
    return [
        d
        for d in first_to_fifth
        if d.month == month
    ]

def weekdays_in_month_2(year, month, weekday):
    """Return list of all 4/5 dates with given weekday and year/month."""
    return [
        dates[0]
        for dates in Calendar(weekday).monthdatescalendar(year, month) 
        if dates[0].month == month
    ]
    

def weekdays_in_month(year, month, weekday):
    """Return list of all 4/5 dates with given weekday and year/month."""
    return [
        date(year, month, week[weekday])
        for week in monthcalendar(year, month) 
        if week[weekday] != 0 
    ]


def meetup_date_1(year, month):
    """Return date of the fourth Thursday of given month"""
    first_day_of_the_month = date(year, month, 1)
    shift = timedelta((Weekday.THURSDAY - first_day_of_the_month.weekday()) % 7) 
    first_thursday = first_day_of_the_month + shift
    return first_thursday + timedelta(weeks=3)


# With Calendar

def meetup_date_2(year, month):
    """Return date of the fourth Thursday of given month"""
    cal = monthcalendar(year, month)
    if cal[0][THURSDAY] == 0:
        nth_of_month = 4
    else:
        nth_of_month = 3
    day_of_fourth_thursday = cal[nth_of_month][THURSDAY]
    return date(year, month, day_of_fourth_thursday)


def meetup_date_3(year, month):
    """Return date of the fourth Thursday of given month"""
    nth = (
        4
        if weekday(year, month, 1) != THURSDAY
        else 3
    )
    thursday_calendar = Calendar(THURSDAY).monthdatescalendar(year, month)
    return thursday_calendar[nth][0]


# Bonus

def meetup_date_4(year, month, *, nth=4, weekday=THURSDAY):
    """Return date of the fourth Thursday of given month"""
    first_day_of_the_month = date(year, month, 1)
    shift = timedelta((weekday - first_day_of_the_month.weekday()) % 7)
    return first_day_of_the_month + shift + timedelta(weeks=nth-1)


def meetup_date_5(year, month, *, nth=4, weekday=THURSDAY):
    """Return date of the fourth Thursday of given month"""
    cal = monthcalendar(year, month)
    if cal[0][weekday] != 0:
        nth -= 1
    return date(year, month, cal[nth][weekday]) 


def meetup_date_6(year, month, *, nth=4, weekday=calendar.THURSDAY):
    """Return date of the nth weekday of the given month."""
    if calendar.weekday(year, month, 1) == weekday:
        nth -= 1
    return calendar.Calendar(weekday).monthdatescalendar(year, month)[nth][0]


# Bonus - allow negative weeks

def meetup_date_7(year, month, *, nth=4, weekday=THURSDAY):
    """Return date of the fourth Thursday of given month"""
    cal = monthcalendar(year, month)
    if nth > 0 and cal[0][weekday] != 0 or nth < 0 and cal[-1][weekday] == 0:
        nth -= 1
    return date(year, month, cal[nth][weekday]) 


def meetup_date_8(year, month, *, nth=4, weekday=calendar.THURSDAY):
    """Return date of the nth weekday of the given month."""
    if nth > 0 and calendar.weekday(year, month, 1) == weekday:
        nth -= 1
    return calendar.Calendar(weekday).monthdatescalendar(year, month)[nth][0]


def meetup_date(year, month, *, nth=4, weekday=calendar.THURSDAY):
    """Return date of the nth weekday of the given month."""
    return weekdays_in_month(year, month, weekday)[nth-1 if nth > 0 else nth]


