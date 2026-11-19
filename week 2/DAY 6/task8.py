import pandas as pd

# Read CSV file
df = pd.read_csv("marks.csv")

# Calculate average Maths marks
average = df['Maths'].mean()

print("Average Maths Marks:", average)

# Find Maths topper
topper = df.loc[df['Maths'].idxmax()]

print("\nMaths Topper:")
print(topper)