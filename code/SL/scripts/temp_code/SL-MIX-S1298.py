pastry_price = 2.50
quantity = 12
discount_rate = 0.15

# Lambda function to compute discounted price
compute_total = lambda qty, price, discount: qty * price * (1 - discount) if qty > 10 else qty * price

# Calculate final cost using the lambda
final_cost = compute_total(quantity, pastry_price, discount_rate)

print(f"Result: {final_cost}")