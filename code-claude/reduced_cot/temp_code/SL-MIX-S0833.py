from itertools import zip_longest

# Calculate total discount for eligible products
# Products with price and discount percentage
products = [(120, 'Headphones'), (85, 'Keyboard'), (200, 'Monitor'), (45, 'Mouse')]
discount_rates = [0.15, 0.05, 0.2, 0.12]

# Some products may have additional shipping fees
shipping_fees = [10, 5, 15, 8]

# Combine product prices with discount rates
product_discounts = list(zip([p[0] for p in products], discount_rates))

# Calculate shipping adjusted prices (not used in discount calculation)
shipping_adjusted = [(p[0] + fee) for p, fee in zip(products, shipping_fees)]

# Only apply discount if it's greater than 10%
total_discount = sum(map(lambda p: p[0] * p[1] if p[1] > 0.1 else 0, product_discounts))

# Calculate final price after discounts (not part of the question)
final_price = sum(p[0] for p in products) - total_discount

print(f"Result: {total_discount}")