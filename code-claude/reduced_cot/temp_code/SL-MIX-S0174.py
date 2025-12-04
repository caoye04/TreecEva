def calculate_discount(base_value, loyalty_tier):
    # Calculate discount based on loyalty tier
    discounts = {'bronze': 0.05, 'silver': 0.10, 'gold': 0.15, 'platinum': 0.20}
    seasonal_bonus = 0.02  # Special seasonal promotion
    
    # Apply tier-based discount plus seasonal bonus
    return base_value * (discounts.get(loyalty_tier, 0) + seasonal_bonus)

# Market inventory and demand data
inventory = {
    'apples': {'quantity': 250, 'cost': 0.35, 'quality': 0.8},
    'oranges': {'quantity': 175, 'cost': 0.42, 'quality': 0.9},
    'bananas': {'quantity': 300, 'cost': 0.29, 'quality': 0.7},
    'grapes': {'quantity': 120, 'cost': 0.65, 'quality': 0.95}
}

demand = {
    'apples': 8,
    'oranges': 7, 
    'bananas': 9,
    'grapes': 6
}

def calculate_price(inventory_data, demand_data):
    # Process inventory and demand to find optimal pricing
    total_cost = sum(item['cost'] * item['quantity'] for item in inventory_data.values())
    avg_quality = sum(item['quality'] for item in inventory_data.values()) / len(inventory_data)
    
    # Calculate potential revenue based on demand
    potential_revenue = sum(demand_data.get(fruit, 0) * 2.5 for fruit in demand_data)
    
    # Market analysis metrics (not directly used in final calculation)
    market_saturation = sum(item['quantity'] for item in inventory_data.values()) / 1000
    competition_factor = 0.85 if market_saturation > 0.8 else 0.95
    weather_impact = {'sunny': 1.05, 'rainy': 0.95, 'cloudy': 1.0}
    current_weather = 'sunny'
    
    # Select highest demand fruit for special promotion
    promotion_fruit = max(demand_data, key=demand_data.get)
    promotion_bonus = 0.5 if inventory_data[promotion_fruit]['quantity'] > 200 else 0.25
    
    # Calculate base price using weighted formula
    base_price = (total_cost * 1.2 + avg_quality * 10) / 2
    
    # Apply demand adjustment - this is the key calculation
    demand_adjustment = sum(demand_data.values()) / 20
    
    # Loyalty program simulation
    loyalty_tier = 'silver' if base_price > 150 else 'bronze'
    loyalty_discount = calculate_discount(base_price, loyalty_tier)
    
    # Calculate final optimal price
    optimal_price = base_price + demand_adjustment - loyalty_discount + promotion_bonus
    
    return round(optimal_price, 2)

# Calculate the optimal pricing
optimal_price = calculate_price(inventory, demand)
print(f"Target result: {optimal_price}")