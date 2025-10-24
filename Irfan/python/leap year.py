from datetime import datetime

# Get the current year
current_year = datetime.now().year

# Ask user for the final year
final_year = int(input("Enter the final year: "))

print(f"Leap years from {current_year} to {final_year}:")

# Function to check for leap year
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Loop through the years
for year in range(current_year, final_year + 1):
    if is_leap_year(year):
        print(year)
