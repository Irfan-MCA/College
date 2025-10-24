import datetime

current_year = datetime.datetime.now().year

try:
    final_year = int(input("Enter the final year: "))

    if final_year <= current_year:
        print("Final year must be greater than the current year.")
    else:
        print(f"Leap years from {current_year} to {final_year} are:")
        for year in range(current_year, final_year + 1):
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                print(year)
except ValueError:
    print("Please enter a valid year (integer).")
