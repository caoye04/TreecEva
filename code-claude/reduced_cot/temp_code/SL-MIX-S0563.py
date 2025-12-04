# Calculate discount for an online bookstore purchase
original_price = 45.99
discount_rate = 0.15

# Customer information
user_name = "JohnDoe123"
user_age = 28
is_member = user_name.endswith("123")
purchase_count = 3

# Calculate the discount based on membership status
discount_amount = original_price * (discount_rate if is_member else discount_rate/2)

# Calculate final price
shipping_cost = 4.99
final_price = original_price - discount_amount + shipping_cost

print(f"Original price: ${original_price}")
print(f"Discount amount: ${discount_amount:.2f}")
print(f"Final price: ${final_price:.2f}")