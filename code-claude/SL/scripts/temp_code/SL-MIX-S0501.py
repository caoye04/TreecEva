# Calculate customer discount based on purchase history and loyalty points
base_price = 120
order_count = 7
previous_returns = 1

# Loyalty program parameters
loyalty_points = order_count * 15 - previous_returns * 5
points_threshold = 100

# Determine discount rate based on purchase history
discount_rate = 0.15 if order_count > 5 else 0.10

# Calculate final discount amount
discount_amount = base_price * (discount_rate if loyalty_points >= points_threshold else discount_rate / 2)

# Apply minimum discount policy
minimum_discount = 5
discount_amount = max(discount_amount, minimum_discount)

print(f"Result: {discount_amount}")