import pandas as pd

df = pd.read_csv("data/car_sales.csv")

# Remove duplicates
df.drop_duplicates(inplace=True)

# Remove rows with missing values
df.dropna(inplace=True)

# Standardize column names
df.columns = df.columns.str.lower().str.replace(" ", "_")

print(df.head())
print(df.shape)

df.to_csv("data/car_sales_cleaned.csv", index=False)

print("Cleaned dataset saved.")
print(df.columns.tolist())