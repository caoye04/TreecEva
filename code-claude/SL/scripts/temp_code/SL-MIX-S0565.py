# Calculate the total price of products that meet specific criteria

def apply_discount(original_price, discount_rate):
    return original_price * (1 - discount_rate)

# Product prices (in dollars)
prices = [45.99, 32.50, 18.75, 89.99, 12.25, 65.00, 37.49]

# Filter prices between $20 and $70, then apply 15% discount
discount_rate = 0.15
filtered_prices = [apply_discount(price, discount_rate) for price in prices if 20 <= price <= 70]

# Calculate sum of filtered and discounted prices
filtered_sum = sum(filtered_prices)

# Calculate average of original prices for comparison
original_avg = sum(prices) / len(prices)

print(f"Result: {filtered_sum}")