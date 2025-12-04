# Calculate discounts for a customer's purchase
prices = [120, 85, 200, 35]
base_rate = 0.05

# Membership level affects discount rate
membership = "gold"

# Calculate discount based on price and membership
calculate_discount = lambda price: price * (base_rate + (0.03 if membership == "gold" else 0.01))

# Calculate shipping cost (not used in final calculation)
shipping = 10 if sum(prices) < 500 else 0

# Apply discounts to all items
total_discount = sum(map(calculate_discount, prices))

# Calculate final price
final_price = sum(prices) - total_discount + shipping

print(f"Total discount: {total_discount}")