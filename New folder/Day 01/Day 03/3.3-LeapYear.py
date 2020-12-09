year = int(input("Enter a year to check if it's a leap year: "))

# function to check whether the given input is a leap year or not
def leap_year(year):
    # if year is divisible by 4, 100 and 400 it is a leap year
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(year, "is a leap year.")
            else:
                print(year, "isn't a leap year.")
        else:
            print(year, "is a leap year.")
    else:
        print(year, "isn't a leap year.")

leap_year(year)