# Calculate discount for eligible items in shopping cart

base_prices = [45.99, 29.50, 15.75, 89.99, 10.25]
minimum_price = 20.00
discount_rate = 0.15

# Apply discount only to items above minimum price threshold
eligible_prices = [price for price in base_prices if price > minimum_price]

# Calculate the total discount amount
discount_amount = sum([price * discount_rate for price in eligible_prices])

# Apply additional discount if total purchases exceed threshold
total_purchase = sum(base_prices)
if total_purchase > 150.00:
    loyalty_bonus = 10.00
else:
    loyalty_bonus = 0.00

# Final amount to be paid by customer
final_amount = total_purchase - discount_amount - loyalty_bonus

print(f"Result: {discount_amount}")