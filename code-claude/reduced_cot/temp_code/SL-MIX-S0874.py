import itertools

# Inventory management system for a small electronics store
# Track stock levels and identify most profitable items

# Initial inventory data
stock_dict = {'laptop': 24, 'tablet': 18, 'phone': 36, 'headphones': 52, 'charger': 65}
prices = {'laptop': 899, 'tablet': 499, 'phone': 699, 'headphones': 129, 'charger': 49}
cost_to_stock = {'laptop': 720, 'tablet': 380, 'phone': 520, 'headphones': 80, 'charger': 20}

# Calculate profit margins for analysis
profit_margins = {}
for item in stock_dict:
    # Profit margin as a percentage
    margin = (prices[item] - cost_to_stock[item]) / prices[item] * 100
    profit_margins[item] = round(margin, 1)

# Track sales data for the week
daily_sales = [
    {'laptop': 3, 'tablet': 2, 'phone': 5, 'headphones': 8, 'charger': 12},  # Monday
    {'laptop': 2, 'tablet': 4, 'phone': 6, 'headphones': 5, 'charger': 10},  # Tuesday
    {'laptop': 1, 'tablet': 1, 'phone': 4, 'headphones': 7, 'charger': 8},   # Wednesday
    {'laptop': 4, 'tablet': 2, 'phone': 3, 'headphones': 10, 'charger': 15},  # Thursday
    {'laptop': 5, 'tablet': 3, 'phone': 7, 'headphones': 12, 'charger': 20},  # Friday
]

# Update inventory based on sales
for day_sales in daily_sales:
    for item, sold in day_sales.items():
        stock_dict[item] -= sold

# Check for items that need restocking
restock_threshold = 25
restock_items = [item for item in stock_dict if stock_dict[item] < restock_threshold]

# Calculate potential combinations of bundle deals (not used in final calculation)
bundle_options = list(itertools.combinations(['laptop', 'tablet', 'phone', 'headphones', 'charger'], 2))
bundle_discounts = {bundle: 0.15 for bundle in bundle_options}  # 15% discount on bundles

# Calculate total profit for each item based on weekly sales
total_sales = {item: sum(day[item] for day in daily_sales) for item in stock_dict}
total_revenue = {item: total_sales[item] * prices[item] for item in total_sales}
total_cost = {item: total_sales[item] * cost_to_stock[item] for item in total_sales}
total_profit = {item: total_revenue[item] - total_cost[item] for item in total_sales}

# Find items with profit over $1000
profitable_items = [item for item in total_profit if total_profit[item] > 1000]

# Sorting by profit (not used in final calculation)
sorted_by_profit = sorted(total_profit.items(), key=lambda x: x[1], reverse=True)

# Calculate the average profit margin across all products
avg_margin = sum(profit_margins.values()) / len(profit_margins)

# Get stock level of the most profitable item
final_stock = stock_dict[max(profitable_items)]

# Display results
print(f"Items needing restock: {restock_items}")
print(f"Most profitable items: {profitable_items}")
print(f"Average profit margin: {avg_margin:.2f}%")
print(f"Stock of most profitable item: {final_stock}")