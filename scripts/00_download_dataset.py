import os

os.system(
    "kaggle datasets download -d gagandeep16/car-sales -p data"
)

print("Dataset downloaded successfully!")
print("If Car_sales.csv is not extracted automatically, extract car-sales.zip manually.")