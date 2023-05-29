def gen_secs():
    for sec in range(0, 60):
        yield sec


def gen_minutes():
    for minute in range(0, 60):
        yield minute


def gen_hours():
    for hours in range(0, 24):
        yield hours


def gen_time():
    for hrs in gen_hours():
        for mins in gen_minutes():
            for secs in gen_secs():
                yield "%02d:%02d:%02d" % (hrs, mins, secs)


def gen_years(start=2019):
    while True:
        yield start
        start += 1


def gen_months():
    for hours in range(1, 13):
        yield hours


def gen_days(month, leap_year=True):
    days = 0
    if month in (4, 6, 9, 11):
        days = 30

    elif month in (1, 3, 5, 7, 8, 10, 12):
        days = 31

    elif month == 2 and leap_year:
        days = 29

    elif month == 2 and not leap_year:
        days = 28

    for day in range(1, days+1):
        yield day


def is_leap_year(year):
    return (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)

def gen_date():
    for year in gen_years():
        for month in gen_months():
            for days in gen_days(month, is_leap_year(year)):
                for time_of_day in gen_time():
                    yield "%02d/%02d/%04d %s" % (days, month, year, time_of_day)


def main():
    date_generator = gen_date()
    iteration_count = 0
    while True:
        try:
            value = next(date_generator)
            iteration_count += 1
            if iteration_count % 1000000 == 0:
                print(value)

        except StopIteration:
            break



if __name__ == '__main__':
    main()