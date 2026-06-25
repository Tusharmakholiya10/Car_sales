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

query = """
SELECT manufacturer,
       ROUND(SUM(sales_in_thousands), 2) AS total_sales
FROM car_sales
GROUP BY manufacturer
ORDER BY total_sales DESC
LIMIT 10;
"""

df = pd.read_sql(query, conn)

conn.close()

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