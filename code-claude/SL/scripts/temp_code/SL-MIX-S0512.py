def calculate_price(sales_data, weights):
    # Apply market adjustments to raw data
    market_factor = 1.25
    adjusted_data = {k: v * market_factor for k, v in sales_data.items()}
    
    # Calculate preliminary price points
    preliminary = sum([adjusted_data.get(k, 0) * w for k, w in weights.items()])
    
    # Apply competitor analysis (not directly used in final calculation)
    competitor_prices = [120, 135, 142, 118]
    competitor_avg = sum(competitor_prices) / len(competitor_prices)
    
    # Calculate seasonal adjustment
    current_month = 4  # April
    seasonal_factor = 0.9 if current_month in [3, 4, 5] else 1.1
    
    # Apply discount threshold logic
    base_price = preliminary * seasonal_factor
    discount_eligible = base_price > 100 and current_month % 2 == 0
    
    # Calculate final price with potential discount
    if discount_eligible and base_price > competitor_avg:
        return base_price * 0.85
    elif discount_eligible:
        return base_price * 0.95
    else:
        return base_price

# Historical sales data by product category
sales_data = {
    'electronics': 50,
    'clothing': 35,
    'books': 20,
    'home': 45
}

# Price influence weights
price_weights = {
    'electronics': 0.4,
    'clothing': 0.3,
    'books': 0.1,
    'home': 0.2
}

# Additional market research data (not directly used)
market_trends = lambda x: x * 1.5 if x > 40 else x * 0.8
trend_adjusted = {k: market_trends(v) for k, v in sales_data.items()}

# Calculate optimal pricing
optimal_price = calculate_price(sales_data, price_weights)
print(f"Result: {optimal_price}")