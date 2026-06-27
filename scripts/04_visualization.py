import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Tushar@26",
    database="car_sales_db"
)
# (1)Top 10 Manufactures (Bar Chart)
query = """
SELECT manufacturer,
       ROUND(SUM(sales_in_thousands), 2) AS total_sales
FROM car_sales
GROUP BY manufacturer
ORDER BY total_sales DESC
LIMIT 10;
"""
df = pd.read_sql(query, conn)



# Create chart
plt.figure(figsize=(10, 6))

plt.bar(df["manufacturer"], df["total_sales"])

plt.title("Top 10 Manufacturers by Sales")
plt.xlabel("Manufacturer")
plt.ylabel("Sales (Thousands)")
plt.xticks(rotation=45)

plt.tight_layout()


# plt.show()
plt.savefig("output/top10_manufacturers.png")
print("Chart saved successfully!")
plt.close()


# (2)Vehicle Type Distribution  (Bar Chart)
query = """
SELECT vehicle_type,
       COUNT(*) AS count
FROM car_sales
GROUP BY vehicle_type;
"""
df = pd.read_sql(query, conn)

plt.figure(figsize=(8,8))
plt.pie(
    df["count"],
    labels=df["vehicle_type"],
    autopct="%1.1f%%"
)
plt.title("Vehicle Type Distribution")
plt.show()


# (3)Scatter Plot (Sales vs Price)
query = """
SELECT sales_in_thousands,
       price_in_thousands
FROM car_sales;
"""
df = pd.read_sql(query, conn)


plt.figure(figsize=(8,5))
plt.scatter(
    df["price_in_thousands"],
    df["sales_in_thousands"]
)
plt.xlabel("Price (Thousands)")
plt.ylabel("Sales (Thousands)")
plt.title("Price vs Sales")
plt.show()


#(4) Top 10 fuel Efficent Cars (Horizontal bar chart)
query = """
SELECT model,
       fuel_efficiency
FROM car_sales
ORDER BY fuel_efficiency DESC
LIMIT 10;
"""
df = pd.read_sql(query, conn)


plt.figure(figsize=(10,5))
plt.barh(
    df["model"],
    df["fuel_efficiency"]
)
plt.title("Top 10 Fuel Efficient Cars")
plt.show()


# (5) Correlation Heatmap
import seaborn as sns

numeric_df = df.select_dtypes(include=["float64","int64"])

plt.figure(figsize=(12,8))
sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm"
)
plt.title("Correlation Matrix")
plt.show()
df = pd.read_sql(query, conn)


conn.close()
