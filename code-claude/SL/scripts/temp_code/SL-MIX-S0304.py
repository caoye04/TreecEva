# Calculate total cost with quantity discounts

item_prices = [12.50, 8.75, 12.50, 9.99, 12.50]
shipping_fee = 5.00
tax_rate = 0.085

# Apply quantity discount for items with the same price
discount_calculator = lambda prices: sum(prices) - sum([p * 0.1 for p in prices if prices.count(p) >= 3])

# Calculate costs
total_cost = discount_calculator(item_prices)
base_total = sum(item_prices)

# Apply tax and shipping
final_cost = (total_cost * (1 + tax_rate)) + shipping_fee

print(f"Result: {total_cost}")