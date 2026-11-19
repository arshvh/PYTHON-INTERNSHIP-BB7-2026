import random

# Generate 5 random numbers
numbers = []

for i in range(5):
    num = random.randint(10, 50)
    numbers.append(num)

# Sort numbers in ascending order
numbers.sort()

# Print result
print("Random Numbers:", numbers)