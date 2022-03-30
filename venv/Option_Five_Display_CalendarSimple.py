def num_of_days_set(set_month):
    if set_month == 4 or 6 or 9 or 11:
        numDays = 30
    elif set_month == 2 and year_is_leap == True:
        numDays = 29
    elif set_month == 2 and year_is_leap == True:
        numDays = 28
    else:
        numDays = 31
    return numDays

def build_calendar(set_day_of_week):
    num_of_days_set(set_month)
    dayStart = int(input("Start day of month? (Sun = 0, Mon = 1 etc.)\n"))
    set_day = int(input("day of the month?\n"))
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
