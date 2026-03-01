import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("coffee_shop_sales.csv")

# 1. add total_amount column 

data['total_amount'] = data['unit_price'] * data['transaction_qty']
data.describe()