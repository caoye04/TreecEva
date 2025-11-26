product_costs = {'A': 150, 'B': 200, 'C': 75, 'D': 120}
profit_margins = {'A': 0.25, 'B': 0.30, 'C': 0.40, 'D': 0.20}

selling_prices = {}
for product, cost in product_costs.items():
    margin = profit_margins[product]
    selling_prices[product] = cost * (1 + margin)

final_prices = {k: round(v) for k, v in selling_prices.items()}

# Calculate total profit across all products
total_profit = sum(final_prices.values())

print(f"Result: {total_profit}")