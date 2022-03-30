def setting_year():
    set_year = int(input("\nInput a year after 1999:\n"))
    is_leap_year(set_year)
    return set_year


def is_leap_year(set_year):
    if (set_year % 4) == 0:
        if (set_year % 100) == 0:
            if (set_year % 400) == 0:
                year_is_leap = True
            else:
                year_is_leap = False
        else:
            year_is_leap = True
    else:
        year_is_leap = False
    return year_is_leap


def setting_month():
    set_month = int(input("Enter the Month (1 to 12):\n"))
    return set_month


def setting_day():
    set_day = int(input("Enter day (1 to 31):\n"))
    return set_day


def setting_day_of_week():
    set_day_of_week = int(input("Day of Week(1-7):\n"))
    if set_day_of_week == 1:
        set_day_of_week_string = "Sunday"
    elif set_day_of_week == 2:
        set_day_of_week_string = "Monday"
    elif set_day_of_week == 3:
        set_day_of_week_string = "Tuesday"
    elif set_day_of_week == 4:
        set_day_of_week_string = "Wednesday"
    elif set_day_of_week == 5:
        set_day_of_week_string = "Thursday"
    elif set_day_of_week == 6:
        set_day_of_week_string = "Friday"
    elif set_day_of_week == 7:
        set_day_of_week_string = "Saturday"
    return set_day_of_week, set_day_of_week_string


class dateInfo:
    def __init__(self):
        self.set_year = setting_year()
        #self.year_is_leap =
        self.set_month = setting_month()
        self.set_day = setting_day()
        self.set_day_of_week = setting_day_of_week()
        self.set_day_of_week_string

    print(set_year)
    print(is_leap_year(set_year))
    print(set_month)
    print(set_day)
    print(set_day_of_week)

"""
    setting_year()
    setting_month()
    setting_day()
    setting_day_of_week()
"""








