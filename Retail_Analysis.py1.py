import pandas as pd
import matplotlib.pyplot as plt
print("RETAIL BUSINESS ANALYSIS")

df = pd.read_csv("Sample - Superstore.csv", encoding="latin1")

print("\nDataset Preview:")
print(df.head())

print("\nTotal Sales:", df["Sales"].sum())
print("Total Profit:", df["Profit"].sum())

print("\nTop 5 Products:")
print(df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head())

print("\nSales by Category:")
print(df.groupby("Category")["Sales"].sum())

print("\nProfit by Region:")
print(df.groupby("Region")["Profit"].sum())

print("\nAnalysis Completed Successfully!")
# Sales by Category - Pie Chart
category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(7,7))
plt.pie(category_sales, labels=category_sales.index, autopct="%1.1f%%")
plt.title("Sales by Category")
plt.show()
# Sales by Region - Bar Chart
region_sales = df.groupby("Region")["Sales"].sum()

plt.figure(figsize=(7,5))
region_sales.plot(kind="bar")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.show()

# Profit by Region - Bar Chart
region_profit = df.groupby("Region")["Profit"].sum()

plt.figure(figsize=(7,5))
region_profit.plot(kind="bar", color="green")
plt.title("Profit by Region")
plt.xlabel("Region")
plt.ylabel("Total Profit")
plt.show()