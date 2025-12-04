from collections import Counter, defaultdict

def calculate_base_price(product_code):
    # Base price calculation with bitwise operations
    digits = [int(d) for d in product_code if d.isdigit()]
    if not digits:
        return 50  # Default price
    
    # First bitwise operation - misleading
    base = (digits[0] << 3) | (digits[-1] & 0x0F)
    
    # Actual price calculation
    price = sum(digits) * 10
    return price

def apply_seasonal_discount(price, season):
    # Misleading seasonal calculation
    season_codes = {'winter': 0b1100, 'spring': 0b0011, 'summer': 0b1010, 'fall': 0b0101}
    irrelevant_factor = season_codes.get(season.lower(), 0) * 0.5
    
    # Actual discount logic
    if season.lower() == 'winter':
        return price * 0.8  # 20% winter discount
    elif season.lower() == 'summer':
        return price * 0.9  # 10% summer discount
    return price  # No discount for spring/fall

def process_inventory_data(data):
    # Misleading complex data transformation
    transformed = defaultdict(list)
    for k, v in data.items():
        if isinstance(v, list):
            transformed[k[::-1]] = [x * 2 for x in v]
        else:
            transformed[k] = v + 10
    
    # This transformation is never used
    return transformed

def calculate_adjusted_value(inventory_data, pricing_factors):
    # Complex but irrelevant analysis
    potential_markets = {'domestic': 1.0, 'international': 1.2, 'emerging': 0.9}
    market_distribution = Counter({'domestic': 5, 'international': 3, 'emerging': 2})
    weighted_market_factor = sum(potential_markets[m] * market_distribution[m] for m in market_distribution) / sum(market_distribution.values())
    
    # Misleading transformation
    temp_data = process_inventory_data(inventory_data)
    
    # Calculate item values - what actually matters
    total_value = 0
    for product_id, quantity in inventory_data.items():
        base_price = calculate_base_price(product_id)
        season = pricing_factors.get('season', 'spring')
        discounted_price = apply_seasonal_discount(base_price, season)
        
        # Misleading calculation branch that's never taken
        if product_id.startswith('Z') and product_id.endswith('X'):
            special_value = (base_price * 1.5) ^ (ord(product_id[1]) & 0x0F)
            total_value += special_value * quantity
            continue
        
        # Actual calculation
        item_value = discounted_price * quantity
        total_value += item_value
    
    # Apply tax - the real final step
    tax_rate = pricing_factors.get('tax_rate', 0.1)  # Default 10%
    final_value = total_value * (1 + tax_rate)
    
    # More distraction calculations
    logistics_cost = sum(inventory_data.values()) * 2.5
    marketing_budget = final_value * 0.15
    projected_revenue = final_value * 1.4
    
    return round(final_value, 2)

# Inventory data: product_id -> quantity
inventory_data = {
    'A123': 10,
    'B456': 5,
    'C789': 15,
    'D012': 8
}

# Pricing factors
pricing_factors = {
    'season': 'winter',
    'tax_rate': 0.08,
    'market': 'domestic',  # Unused distractor
    'promotion_code': 'SAVE20'  # Unused distractor
}

# Misleading calculations
market_analysis = defaultdict(float)
for product in inventory_data:
    market_analysis[product[0]] += inventory_data[product] * ord(product[0])

supply_chain_efficiency = 0.85
logistics_overhead = sum(inventory_data.values()) * 1.2

# The key calculation
final_inventory_value = calculate_adjusted_value(inventory_data, pricing_factors)
print(f"Target result: {final_inventory_value}")