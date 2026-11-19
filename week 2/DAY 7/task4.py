from datetime import datetime

# Get current date and time
now = datetime.now()

# Format date and time
formatted_date = now.strftime("%A, %d-%B-%Y %I:%M %p")

# Print result
print("Current Date and Time:", formatted_date)