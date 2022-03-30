def display_menu():
    print("\nBMC Calendar Application\n\nPlease choose from the following options:\n"
          "\n1.   Set Date\n"
          "2.   Display calendar for this month\n"
          "3.   Display date information\n"
          "4.   Quit\n")


def setting_year():
    set_year = int(input("\nInput a year after 1999:\n"))
    if set_year < 1999:
        print("Input was 1999 or older, please enter a valid date")
        setting_year()
    elif set_year < 2050:
        print("Input is for the distant future, please enter a valid date")
        setting_year()
    return set_year


def is_leap_year(set_year):
    if set_year % 4 == 0 and set_year % 100 != 0:
        return True
    elif set_year % 100 == 0:
        return False
    elif set_year % 400 == 0:
        return True
    else:
        return False


def setting_month():
    set_month = int(input("Enter the Month (1 to 12):\n"))
    return set_month


def setting_month_string(set_month):
    if set_month == 1:
        set_month_string = "January"
    elif set_month == 2:
        set_month_string = "February"
    elif set_month == 3:
        set_month_string = "March"
    elif set_month == 4:
        set_month_string = "April"
    elif set_month == 5:
        set_month_string = "May"
    elif set_month == 6:
        set_month_string = "June"
    elif set_month == 7:
        set_month_string = "July"
    elif set_month == 8:
        set_month_string = "August"
    elif set_month == 9:
        set_month_string = "September"
    elif set_month == 10:
        set_month_string = "October"
    elif set_month == 11:
        set_month_string = "November"
    elif set_month == 12:
        set_month_string = "December"
    return set_month_string


def setting_day():
    set_day = int(input("Enter day (1 to 31):\n"))
    return set_day


def setting_day_of_week():
    set_day_of_week = int(input("Day of Week(1-7):\n"))
    return set_day_of_week

def setting_day_of_week_string(set_day_of_week):
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
    return set_day_of_week_string


def num_of_days_set(set_month):
    if set_month == 4 or 6 or 9 or 11:
        numDays = 30
    elif set_month == 2 and year_is_leap == True:
        numDays = 29
    elif set_month == 2 and year_is_leap == False:
        numDays = 28
    else:
        numDays = 31
    return numDays


def build_calendar(set_day_of_week):
    num_of_days_set(set_month)
    dayStart = int(input("Start day of month? (Sun = 0, Mon = 1 etc.)\n"))
    #set_day = int(input("day of the month?\n"))
    isPrintDate = False  # won't print

    dateCurrent = 1  # date counter

    print(" Sun Mon Tue Wed Thu Fri Sat")
    for week in range(6): # week = 0,1...5
        for day in range(7):
            if day == set_day_of_week:
                isPrintDate = True
            if dateCurrent > numDays:
                isPrintDate = False
            if isPrintDate:
                if dateCurrent == set_day:
                    print(f'   * ', end='')
                    dateCurrent += 1
                else:
                    print(f'{dateCurrent:4d}', end='')
                    dateCurrent += 1
            else:
                print("    ", end='')
        print("")


def display_menu_option_3(set_year, year_is_leap, set_month_string, set_day, set_day_of_week_string):
    print("****************")
    print(str(set_day_of_week_string) + ", " + str(set_day) + " " + str(set_month_string) + " " + str(set_year))
    if year_is_leap:
        print(str(set_year) + " is a leap year")
    else:
        print(str(set_year) + " is not a leap year")
    print("****************")


def option_four():
    quit("\n***\nThank you for visiting the BMC Calendar application\n***")

set_year = 0
year_is_leap = bool
set_month = 0
set_month_string = ""
set_day = 0
set_day_of_week = 0
set_day_of_week_string = ""

display_menu()
user_main_menu_input = int(input("Option:\n"))
while user_main_menu_input != 0:
    if user_main_menu_input == 1:
        print("\nOption:1")
        set_year = setting_year()
        set_month = setting_month()
        set_month_string = setting_month_string(set_month)
        set_day = setting_day()
        set_day_of_week = setting_day_of_week()
        set_day_of_week_string = setting_day_of_week_string(set_day_of_week)

        #print(set_year)
        #print(is_leap_year(set_year))
        #print(set_month)
        #print(set_month_string)
        #print(set_day)
        #print(set_day_of_week)
        #print(set_day_of_week_string)

    elif user_main_menu_input == 2:
        print("\nOption:2")
        #num_of_days_set(set_month)
        #build_calendar(set_day_of_week)
        pass

    elif user_main_menu_input == 3:
        print("\nOption:3")
        display_menu_option_3(set_year, year_is_leap, set_month_string, set_day, set_day_of_week_string)

    elif user_main_menu_input == 4:
        option_four()
    else:
        print("\nInvalid input, please enter a number between 1 and 4\n")
    display_menu()
    user_main_menu_input = int(input("Option:\n"))

