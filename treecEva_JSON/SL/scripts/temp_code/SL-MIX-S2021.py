from functools import reduce

beverage_prices = {'espresso': 2.50, 'latte': 4.00, 'cappuccino': 3.50}
sales_counts = {'espresso': 30, 'latte': 30, 'cappuccino': 20}

# Calculate revenue for each beverage using dictionary comprehension and merging
revenues = {k: beverage_prices[k] * sales_counts[k] for k in beverage_prices}
total_revenue = sum(revenues.values())

# Compute base profit as 30% of total revenue
base_profit = total_revenue * 0.30

# Apply bonus if latte revenue exceeds $100
bonus = 20 if revenues['latte'] > 100 else 0
final_profit = base_profit + bonus

print(f'Result: {final_profit}')