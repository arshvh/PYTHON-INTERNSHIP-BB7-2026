import random

# Roll two dice
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)

# Calculate sum
total = dice1 + dice2

# Display results
print("First Dice:", dice1)
print("Second Dice:", dice2)
print("Total:", total)

# Check winning condition
if total == 7 or total == 11:
    print("You Win!")
else:
    print("Try Again!")