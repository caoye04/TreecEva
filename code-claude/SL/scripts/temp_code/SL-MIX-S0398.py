def calculate_discount(price, years):
    # Calculate discount based on loyalty years
    base_discount = 0.05  # 5% base discount
    loyalty_bonus = years * 0.01  # 1% per year
    max_discount = 0.25  # Maximum discount cap
    
    # Calculate total discount percentage
    total_discount = base_discount + loyalty_bonus
    
    # Apply discount cap using conditional expression
    effective_discount = min(total_discount, max_discount)
    
    # Calculate discount amount
    return price * effective_discount

# Customer information
original_price = 120.00
loyalty_years = 8
shipping_cost = 15.00

# Some additional data we track
store_id = "NYC-104"
season_modifier = lambda x: x * 1.1 if x > 100 else x

# Apply the discount calculation
discount_amount = calculate_discount(original_price, loyalty_years)

# Calculate final price (not needed for this problem)
final_price = original_price - discount_amount + shipping_cost

print(f"Result: {discount_amount}")