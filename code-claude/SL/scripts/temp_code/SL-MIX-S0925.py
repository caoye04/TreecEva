# Calculate final price for an online purchase with discount and shipping

customer_tier = 'gold'
discounts = {'bronze': 0.05, 'silver': 0.10, 'gold': 0.15, 'platinum': 0.20}

product_name = 'Wireless Headphones'
base_price = 89.99
color_preference = 'black'

shipping_method = 'standard'
shipping_fees = {'express': 12.50, 'standard': 4.99, 'economy': 2.50}

# Apply any available discount and add shipping fee
total_cost = round(base_price * (1 - discounts.get(customer_tier, 0)) + shipping_fees[shipping_method])

# Calculate estimated delivery days
delivery_days = {'express': 2, 'standard': 5, 'economy': 9}
expected_delivery = delivery_days[shipping_method]

print(f"Product: {product_name} ({color_preference})")
print(f"Result: {total_cost}")