def calculate_revenue(sales, price_adj):
    base_revenue = 0
    discount_factor = 0.95  # 5% discount on all transactions
    loyalty_bonus = 50  # bonus for loyal customers
    
    # Process each product category with its sales
    for category, (quantity, region) in sales.items():
        # Apply regional price adjustments
        base_price = price_adj.get(region, 100)  # default price 100
        
        # Calculate seasonal multiplier (not used in final calculation)
        season_code = ord(region[0].lower()) % 4
        seasonal_multiplier = 1.0 + (season_code * 0.05)
        
        # Process based on product category
        if category.startswith('tech'):
            item_revenue = quantity * base_price * 1.2  # tech premium
        elif category.endswith('food'):
            item_revenue = quantity * base_price * 0.9  # food discount
            # Track food items (not used in final calculation)
            food_items = [f"{category}-{i}" for i in range(min(3, quantity))]
        else:
            item_revenue = quantity * base_price
        
        base_revenue += item_revenue
    
    # Apply general discount and add loyalty bonus for qualified sales
    qualified_for_bonus = base_revenue > 5000
    adjusted_revenue = base_revenue * discount_factor
    
    # Temporary variable to track potential revenue (not used)
    potential_revenue = base_revenue * 1.1
    
    # Add loyalty bonus if qualified
    if qualified_for_bonus:
        adjusted_revenue += loyalty_bonus
    
    return round(adjusted_revenue)

# Sales data: category -> (quantity, region)
sales_data = {
    'tech_gadgets': (120, 'North'),
    'office_supplies': (85, 'South'),
    'fresh_food': (45, 'East'),
    'tech_accessories': (60, 'West')
}

# Price adjustments by region
price_adjustments = {
    'North': 110,
    'South': 95,
    'East': 105,
    'West': 115
}

# Calculate total revenue
total_revenue = calculate_revenue(sales_data, price_adjustments)
print(f"Target result: {total_revenue}")
