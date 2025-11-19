from collections import defaultdict

# Initial prices
prices = {'croissant': 2.00, 'muffin': 1.50, 'scone': 2.50}

# Sales on day one
sales_day_one = {'croissant': 8, 'muffin': 12, 'scone': 15}

# Calculate revenue
total_revenue = sum(prices[item] * sales_day_one[item] for item in prices)

print(f"Result: {total_revenue}")