def calculate_optimal_capacity(warehouse_data, product_weights):
    # Initialize tracking variables
    total_space = 0
    efficiency_factor = 0.85
    overhead_constant = 120
    
    # Process warehouse sections
    section_multipliers = {'A': 2, 'B': 1.5, 'C': 0.75, 'D': 1.25}
    section_offsets = {'A': 50, 'B': 30, 'C': 20, 'D': 40}
    
    # Calculate base capacity from warehouse data
    base_capacity = 0
    for section, metrics in warehouse_data.items():
        if section in section_multipliers:
            # Apply section-specific calculations
            area = metrics.get('area', 0)
            height = metrics.get('height', 0)
            temperature = metrics.get('temperature', 20)
            
            # Temperature adjustment (distraction)
            temp_factor = 1.0
            if temperature < 5:
                temp_factor = 0.9
            elif temperature > 30:
                temp_factor = 0.8
            
            # Calculate section capacity
            section_capacity = area * height * section_multipliers[section]
            
            # Apply section offset
            if section in ['A', 'C']:
                section_capacity += section_offsets[section]
            
            base_capacity += section_capacity
    
    # Simulate complex logistics calculations (mostly distractions)
    logistics_overhead = {}
    for i in range(1, 6):
        factor = i * 0.15
        adjusted = overhead_constant * factor
        logistics_overhead[f'tier_{i}'] = adjusted
    
    # Product weight analysis (partially relevant)
    weight_categories = {'light': 0, 'medium': 0, 'heavy': 0}
    for product, weight in product_weights.items():
        if weight < 10:
            weight_categories['light'] += 1
        elif weight < 50:
            weight_categories['medium'] += 1
        else:
            weight_categories['heavy'] += 1
    
    # Calculate weight adjustment (this is where the key calculation happens)
    weight_adjustment = 0
    if weight_categories['heavy'] > 0:
        weight_adjustment = weight_categories['heavy'] * 5
        if weight_categories['medium'] > weight_categories['light']:
            weight_adjustment += 15
    else:
        weight_adjustment = weight_categories['medium'] // 2
    
    # Calculate theoretical max (distraction)
    theoretical_max = base_capacity * 1.5 - logistics_overhead['tier_3']
    
    # Calculate practical capacity (distraction)
    practical_capacity = base_capacity * efficiency_factor
    
    # Seasonal adjustments (distraction)
    seasons = ['winter', 'spring', 'summer', 'fall']
    season_factors = [0.9, 1.1, 1.2, 1.0]
    current_season = 2  # summer
    
    seasonal_adjustment = base_capacity * (season_factors[current_season] - 1.0)
    
    # Optimization algorithms (distraction with some relevance)
    optimization_tiers = []
    for i in range(1, 4):
        tier_value = (base_capacity // (5 - i)) + (i * 10)
        optimization_tiers.append(tier_value)
    
    # Calculate final optimal capacity
    optimal_capacity = base_capacity - weight_adjustment
    
    # Apply bitwise operations for special cases (distraction)
    bit_flags = 0b1010
    if bit_flags & 0b1000:
        bit_adjustment = bit_flags ^ 0b0110
        optimal_capacity = optimal_capacity + bit_adjustment
    
    return optimal_capacity

# Warehouse data
warehouse_data = {
    'A': {'area': 200, 'height': 4, 'temperature': 22},
    'B': {'area': 150, 'height': 3, 'temperature': 18},
    'C': {'area': 100, 'height': 5, 'temperature': 15},
    'D': {'area': 180, 'height': 4, 'temperature': 25}
}

# Product weights
product_weights = {
    'product1': 5,
    'product2': 12,
    'product3': 30,
    'product4': 60,
    'product5': 8,
    'product6': 45,
    'product7': 75
}

# Calculate the optimal warehouse capacity
optimal_capacity = calculate_optimal_capacity(warehouse_data, product_weights)
print(f"Result: {optimal_capacity}")