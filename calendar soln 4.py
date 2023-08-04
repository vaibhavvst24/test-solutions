def get_season(month, day): # for finding the season through day and month 
    seasons = {
        (3, 20): "Spring",
        (6, 21): "Summer",
        (9, 22): "Autumn",
        (12, 21): "Winter"
    }
    
    for (m, d), season in seasons.items():
        if (month, day) >= (m, d):
            return season
    return "Winter"

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) # calculation for leap year 

def get_days_in_year(year):
    if is_leap_year(year):
        return 366
    else:
        next_leap_year = year + (4 - year % 4)
        return next_leap_year - year

if __name__ == "__main__": # main program
    try:
        year = int(input("Enter the year: "))
        month = int(input("Enter the month (1-12): "))
        day = int(input("Enter the day (1-31): "))

        season = get_season(month, day)
        print("Season:", season)

        if is_leap_year(year):
            print(f"{year} is a leap year.")
            days_in_year = get_days_in_year(year)
            print(f"Number of days in {year}: {days_in_year}")
        else:
            next_leap_year = year + (4 - year % 4)
            print(f"{year} is not a leap year.")
            print(f"Next leap year: {next_leap_year}")

    except ValueError as e:
        print("Error:", e)
