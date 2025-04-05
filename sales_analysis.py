import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("sales_data.csv")

# Group data by product and calculate total sales and total profit
product_sales = df.groupby('Product')[['Sales', 'Profit']].sum()

# Display the grouped data
print(product_sales)

# Set the style of the plots
sns.set(style="whitegrid")

# Create a bar plot for Sales
plt.figure(figsize=(10, 6))
sns.barplot(x=product_sales.index, y=product_sales['Sales'], palette='Blues_d')
plt.title('Total Sales by Product')
plt.ylabel('Total Sales')
plt.xlabel('Product')
plt.show()

# Create a bar plot for Profit
plt.figure(figsize=(10, 6))
sns.barplot(x=product_sales.index, y=product_sales['Profit'], palette='Greens_d')
plt.title('Total Profit by Product')
plt.ylabel('Total Profit')
plt.xlabel('Product')
plt.show()
