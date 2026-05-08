import pandas as pd
import matplotlib.pyplot as plt

# read the csv file
data = pd.read_csv("sales_data.csv")

print("\n========== SALES DATA ==========\n")
print(data)

# calculate total sales for each product
data["Total_Sales"] = data["Price"] * data["Quantity"]

print("\n========== UPDATED DATA ==========\n")
print(data)

# total revenue
total_revenue = data["Total_Sales"].sum()

print("\n========== TOTAL REVENUE ==========")
print(f"Total Revenue: ${total_revenue}")

# best selling product by quantity
best_product = data.loc[data["Quantity"].idxmax()]

print("\n========== BEST SELLING PRODUCT ==========")
print(f"Product Name : {best_product['Product']}")
print(f"Category     : {best_product['Category']}")
print(f"Quantity Sold: {best_product['Quantity']}")

# average product price
average_price = data["Price"].mean()

print("\n========== AVERAGE PRODUCT PRICE ==========")
print(f"Average Price: ${average_price:.2f}")

# category wise sales
category_sales = data.groupby("Category")["Total_Sales"].sum()

print("\n========== CATEGORY SALES ==========\n")
print(category_sales)

# save updated data to a new csv file
data.to_csv("updated_sales_data.csv", index=False)

print("\nUpdated data saved as updated_sales_data.csv")

# create a simple bar chart
category_sales.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()

plt.show()