from datetime import date

# Take date of birth from user
year = int(input("Enter your birth year: "))
month = int(input("Enter your birth month: "))
day = int(input("Enter your birth day: "))

# Create date of birth
dob = date(year, month, day)

# Get today's date
today = date.today()

# Calculate age
age = today.year - dob.year

# Adjust age if birthday hasn't occurred yet
if (today.month, today.day) < (dob.month, dob.day):
    age -= 1

# Print age
print("Your exact age is:", age, "years")