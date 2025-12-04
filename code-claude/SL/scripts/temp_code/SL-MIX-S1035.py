def calculate_purchase_total(item_price, quantity, is_member=False):
    # Base price calculation
    base_price = item_price * quantity
    
    # Various discount rates
    seasonal_discount = 0.05  # 5% seasonal sale
    loyalty_discount = 0.12   # 12% loyalty discount
    clearance_discount = 0.15 # 15% clearance items (not used)
    
    # Customer information
    customer_years = 3 if is_member else 1
    has_coupon = False  # Customer doesn't have additional coupon
    
    # Calculate applicable discount
    discount_amount = base_price * (loyalty_discount if customer_years > 2 else seasonal_discount)
    
    # Final price calculation
    final_price = base_price - discount_amount
    
    print(f"Base Price: ${base_price:.2f}")
    print(f"Discount Amount: ${discount_amount:.2f}")
    print(f"Final Price: ${final_price:.2f}")
    
    return final_price

# Process a purchase
item_price = 25.0
quantity = 4
purchase_total = calculate_purchase_total(item_price, quantity, is_member=True)
print(f"Target result: {discount_amount}")