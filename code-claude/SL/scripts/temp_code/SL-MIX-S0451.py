# Calculate shipping cost based on delivery options and package weight
package_weight = 12.5  # Weight in kg
weight_limit = 10.0   # Standard weight limit
base_rate = 15.0      # Base shipping rate

# Delivery settings
express_delivery = True
premium_factor = 0.25  # 25% premium for express delivery

# Calculate surcharge based on weight
overweight = package_weight - weight_limit
weight_surcharge = overweight * 2.0 if overweight > 0 else 0

# Customer loyalty discount
customer_tier = 'gold'
loyalty_discount = 2.0 if customer_tier == 'gold' else 0

# Calculate final shipping cost
shipping_cost = base_rate * (1 + premium_factor if express_delivery else 0) + (weight_surcharge if package_weight > weight_limit else 0)

# Apply loyalty discount
final_cost = shipping_cost - loyalty_discount

print(f"Shipping cost: {shipping_cost}")