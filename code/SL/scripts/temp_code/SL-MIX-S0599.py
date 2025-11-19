from collections import defaultdict

def update_prices_based_on_sales(prices, counts):
    new_prices = prices.copy()
    for item in prices:
        if counts[item] > 10:
            new_prices[item] += 0.25
    return new_prices

# Initial data
items = ['croissant', 'muffin', 'scone']
initial_prices = {'croissant': 3.00, 'muffin': 2.50, 'scone': 2.75}
sales_counts = defaultdict(int, {'croissant': 8, 'muffin': 12, 'scone': 15})

total_revenue = 0.0
prices = initial_prices.copy()

for day in range(5):
    daily_revenue = sum(prices[item] * sales_counts[item] for item in items)
    total_revenue += daily_revenue
    prices = update_prices_based_on_sales(prices, sales_counts)

print(f"Result: {total_revenue}")