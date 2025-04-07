# Import just the date class from the datetime module
from datetime import date

# Get today's date
today = date.today()

# Ask the user for their birth date
year = int(input("Enter the year you were born (e.g., 1990): "))
month = int(input("Enter the month you were born (1–12): "))
day = int(input("Enter the day you were born (1–31): "))

# Create a date object for the birth date
birth_date = date(year, month, day)

# Calculate the difference between today and the birth date
days_old = (today - birth_date).days

print(f"You are {days_old} days old!")