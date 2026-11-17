import pandas as pd

# Read CSV file
df = pd.read_csv("products.csv")

# Display first 2 rows
print("First 2 Rows:")
print(df.head(2))

# Display total dimensions
print("\nShape of Dataset:")
print(df.shape)