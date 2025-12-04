# E-commerce product performance analysis

product_inventory = {
    'laptop': {'price': 1200, 'cost': 800, 'stock': 15},
    'phone': {'price': 800, 'cost': 450, 'stock': 25},
    'tablet': {'price': 300, 'cost': 150, 'stock': 40},
    'headphones': {'price': 150, 'cost': 50, 'stock': 100},
    'monitor': {'price': 400, 'cost': 250, 'stock': 20}
}

# Customer review scores (out of 5)
review_scores = {
    'laptop': 4.5,
    'phone': 4.2,
    'tablet': 3.9,
    'headphones': 4.7,
    'monitor': 4.1
}

# Calculate potential revenue and visibility scores
total_potential_revenue = 0
visibility_score = {}

for product, details in product_inventory.items():
    revenue = details['price'] * details['stock']
    total_potential_revenue += revenue
    
    # Calculate visibility score based on price and reviews
    normalized_price = details['price'] / 1000  # Scale down prices
    visibility_score[product] = review_scores[product] * normalized_price

# Track products with low stock for reordering
low_stock_products = []
for product, details in product_inventory.items():
    if details['stock'] < 20:
        low_stock_products.append(product)

# Calculate profit margin for each product
profit_margins = {}
for product, details in product_inventory.items():
    profit_margins[product] = (details['price'] - details['cost']) / details['price'] * 100

# Find average profit margin
average_margin = sum(profit_margins.values()) / len(profit_margins)

# Calculate total profit for each product
product_profits = {}
for product, details in product_inventory.items():
    unit_profit = details['price'] - details['cost']
    total_profit = unit_profit * details['stock']
    product_profits[product] = total_profit

# Find the product with highest profit
highest_profit = max(product_profits.values())
lowest_profit = min(product_profits.values())
profit_range = highest_profit - lowest_profit

# Calculate a weighted score that doesn't affect the result
weighted_scores = {}
for product in product_inventory:
    weighted_scores[product] = review_scores[product] * profit_margins[product] / 100

print(f"Result: {highest_profit}")