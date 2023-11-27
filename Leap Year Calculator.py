"""Formula to calculate leap year.

We begin by identifying the year we want to know if its a leap year.
We then divide the year by 4 to check if its evenly divisible.
Then confirm that the year is not evenly divisible by 100.
Check if the year is divisible by 400.
If the year is evenly divisible by 4, then the year is a leap year.

If the year is only evenly divisible by 100 and not evenly divisible by 400, then the year is not a leap year."""


def leap_year_checker(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year & 400 == 0:
                print("Leap Year.")
            else:
                print("Not a Leap Year.")
        else:
            print("Leap Year.")
    else:
        print("Not a Leap Year.")



year_input = int(input("Enter the year: "))
leap_year_checker(year_input)
