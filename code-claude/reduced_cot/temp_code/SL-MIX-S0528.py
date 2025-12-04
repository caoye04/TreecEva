def apply_seasonal_factor(month):
    # Higher discount in winter months
    winter_months = [11, 12, 1, 2]
    summer_months = [6, 7, 8]
    
    if month in winter_months:
        return 1.2
    elif month in summer_months:
        return 0.9
    else:
        return 1.0

def calculate_base_points(price):
    # Calculate loyalty points (not used in final discount)
    if price < 50:
        return price * 0.5
    elif price < 100:
        return price * 0.75
    else:
        return price * 1.0

def calculate_discount(price, tier, years):
    # Base discount percentage based on loyalty tier
    tier_discounts = {
        'bronze': 5,
        'silver': 10,
        'gold': 15,
        'platinum': 20
    }
    
    # Get base discount percentage
    base_discount = tier_discounts.get(tier.lower(), 0)
    
    # Additional discount for membership years
    loyalty_bonus = min(years * 0.5, 10)  # Cap at 10%
    
    # Apply seasonal adjustment (not actually used)
    current_month = 3  # March
    seasonal_factor = apply_seasonal_factor(current_month)
    
    # Calculate potential additional offers (not applied)
    special_offer = 5 if price > 200 else 0
    
    # Calculate points (not used in discount calculation)
    points = calculate_base_points(price)
    
    # Apply the actual discount
    total_percentage = base_discount + loyalty_bonus
    discount_amount = price * (total_percentage / 100)
    
    # Cap discount at 30% of original price
    max_discount = price * 0.3
    final_discount = discount_amount if discount_amount <= max_discount else max_discount
    
    return round(final_discount, 2)

# Customer information
original_price = 250
loyalty_tier = 'Gold'
years_member = 8

# Calculate membership level score (not used in final calculation)
membership_score = len(loyalty_tier) * years_member

# Apply discount
total_discount = calculate_discount(original_price, loyalty_tier, years_member)

# Calculate final price (not the requested value)
final_price = original_price - total_discount

print(f"Result: {total_discount}")