# Calculate total discount for eligible items in a shopping cart

prices = [12.99, 24.50, 8.75, 32.00, 15.25]
elements = ['Shirt', 'Pants', 'Socks', 'Jacket', 'Hat']

# Items with True are eligible for discount
eligible_items = [False, True, False, True, True]

# Base discount rate is 15%
discount_rate = 0.15

# Calculate how many items are eligible
eligible_count = sum(1 for item in eligible_items if item)

# Apply a small adjustment based on number of eligible items
adjusted_rate = discount_rate + 0.02 if eligible_count > 2 else discount_rate

# We'll use the original discount rate for the calculation
# This calculates the discount amount for each eligible item
total_discount = sum(map(lambda x: x[1] * (discount_rate if x[0] else 0), zip(eligible_items, prices)))

# Display results
print(f"Total items: {len(prices)}")
print(f"Eligible items: {eligible_count}")
print(f"Result: {total_discount}")