# Calculate total order price with shipping based on weight
prices = [12.50, 8.75, 15.00, 9.99]
quantities = [2, 1, 3, 2]
shipping_rates = (3.99, 5.99, 8.99)

# Calculate weight of order (not needed for total price)
item_weights = [0.5, 0.3, 0.8, 0.4]
order_weight = sum(w * q for w, q in zip(item_weights, quantities))

# Calculate base price before discounts
base_price = 0
for i, (price, quantity) in enumerate(zip(prices, quantities)):
    base_price += price * quantity

# Apply promotional discount
discount_rate = 0.10 if base_price > 50 else 0
promo_code = "SUMMER10"
if promo_code.lower().startswith("summer"):
    discount_rate += 0.05

# Apply the discount
discounted_price = base_price * (1 - discount_rate)

# Calculate final price with tax
tax_rate = 0.085
total_price = sum(map(lambda x: x[0] * x[1], zip(prices, quantities)))
total_with_tax = total_price * (1 + tax_rate)

print(f"Result: {total_price}")