import pandas as pd

df = pd.read_csv(r"C:\Internship\week 2\DAY 6\product.csv")

print("First 2 Rows:")
print(df.head(2))

print("Total Dimensions:")
print(df.shape)