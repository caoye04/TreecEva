# Calculate discount for online purchase

item_price = 85
item_quantity = 3

# Determine discount based on purchase value
base_discount = 10
purchase_value = item_price * item_quantity

# Apply loyalty bonus if applicable
customer_loyalty = True
loyalty_bonus = 5 if customer_loyalty else 0

# Calculate final discount percentage
discount_percent = base_discount + loyalty_bonus

# Apply weekend special if today is weekend
is_weekend = False
weekend_bonus = 2
discount_percent = discount_percent + weekend_bonus if is_weekend else discount_percent

# Calculate the discount amount
total_discount = discount_percent * item_price / 100

# Calculate final price after discount
final_price = item_price - total_discount

print(f"Result: {total_discount}")