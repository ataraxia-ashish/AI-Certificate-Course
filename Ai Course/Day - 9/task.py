import pandas as pd

# Load your data
df = pd.read_csv('coffee_shop_sales.csv')

# Group by product and sum the quantities
product_sales = df.groupby('product_type')['transaction_qty'].sum().reset_index()

# Find the Maximum and Minimum
max_sold = product_sales.loc[product_sales['transaction_qty'].idxmax()]
min_sold = product_sales.loc[product_sales['transaction_qty'].idxmin()]

print(f"Top Seller: {max_sold['product_type']} ({max_sold['transaction_qty']} units)")
print(f"Lowest Seller: {min_sold['product_type']} ({min_sold['transaction_qty']} units)")