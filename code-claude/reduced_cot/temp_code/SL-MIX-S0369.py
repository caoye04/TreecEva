import itertools

# E-commerce loyalty program points calculator
def process_purchase_history(transactions):
    # Process recent purchases to calculate loyalty points
    base_multiplier = 2
    seasonal_bonus = 15
    purchase_threshold = 50
    
    # Initialize counters
    total_points = 0
    bonus_points = 0
    penalty_points = 0
    inactive_months = 3  # Customer was inactive for 3 months
    
    # Process each transaction using enumerate
    for idx, (amount, category, is_promo) in enumerate(transactions):
        # Calculate basic points (1 point per dollar spent)
        basic_points = amount // 1  # Integer division
        
        # Apply category multipliers
        if category == "electronics":
            category_multiplier = 1.5
        elif category == "grocery":
            category_multiplier = 1.0
        else:  # "clothing"
            category_multiplier = 1.2
        
        # Calculate transaction points
        transaction_points = int(basic_points * category_multiplier)
        
        # Apply promotional bonus if applicable
        if is_promo and amount > purchase_threshold:
            transaction_points += seasonal_bonus
        
        # Track bonus points separately (not used in final calculation)
        if idx % 2 == 0:  # Every other transaction gets extra tracking (not used)
            bonus_tracker = transaction_points & 0x0F  # Bitwise AND with 15
            bonus_points += bonus_tracker
        
        # Add to total
        total_points += transaction_points
    
    # Calculate penalty for inactivity (5 points per inactive month)
    penalty_points = inactive_months * 5
    
    # Calculate potential future points (distractor)
    potential_future = [total_points * 1.1, total_points * 1.2, total_points * 1.3]
    avg_potential = sum(potential_future) / len(potential_future)
    
    # Calculate final customer points
    customer_points = total_points - penalty_points
    
    # Apply membership tier adjustment (distractor)
    tier_levels = list(zip(['silver', 'gold', 'platinum'], [1.0, 1.05, 1.1]))
    for tier_name, tier_multiplier in tier_levels:
        tier_adjusted = customer_points * tier_multiplier
        if tier_name == 'gold':  # Customer's actual tier
            tier_bonus = int(customer_points * 0.05)  # Not used in final result
    
    return total_points, penalty_points, customer_points

# Customer's purchase history: (amount, category, is_promotional)
transactions = [
    (120, "electronics", True),
    (45, "grocery", False),
    (80, "clothing", True),
    (30, "grocery", False),
    (200, "electronics", False)
]

total_points, penalty_points, customer_points = process_purchase_history(transactions)
print(f"Total points earned: {total_points}")
print(f"Penalty points: {penalty_points}")
print(f"Result: {customer_points}")