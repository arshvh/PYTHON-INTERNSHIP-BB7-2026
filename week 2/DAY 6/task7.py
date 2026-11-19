import pandas as pd

# Load CSV file
df = pd.read_csv("product.csv")

# Filter products where Price > 5000
filtered_data = df[df['Price'] > 5000]

# Print filtered data
print(filtered_data)