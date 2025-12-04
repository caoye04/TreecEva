def calculate_packing_efficiency(items, container_size):
    # Calculate how efficiently items can be packed
    volume_used = sum(item['volume'] for item in items if item['priority'] > 0)
    return volume_used / container_size if container_size > 0 else 0

def optimize_shipping_route(destinations, fuel_capacity):
    # Optimize shipping route based on destinations and fuel
    route_efficiency = 0
    for dest in destinations:
        distance = dest.get('distance', 100)
        importance = dest.get('importance', 1)
        route_efficiency += (importance * 50) / (distance + 10)
    
    # Adjust for fuel capacity
    return route_efficiency * (fuel_capacity / 100)

def calculate_optimal_container_capacity(inventory, shipping_constraints):
    # Key variables for optimization
    base_capacity = 1000  # Standard container size
    adjustment_factor = 0
    
    # Process inventory data
    total_items = sum(1 for item in inventory if isinstance(item, dict))
    priority_items = sum(1 for item in inventory if isinstance(item, dict) and item.get('priority', 0) > 2)
    
    # These calculations appear important but are actually irrelevant
    potential_efficiency = calculate_packing_efficiency(inventory, base_capacity)
    route_optimization = optimize_shipping_route(shipping_constraints.get('destinations', []), 
                                               shipping_constraints.get('fuel', 75))
    
    # Misleading calculations that don't affect the result
    if potential_efficiency > 0.8:
        adjustment_factor += 250
    elif potential_efficiency > 0.5:
        adjustment_factor += 150
    
    # This is the actual logic that matters
    weather_conditions = shipping_constraints.get('weather_code', 0)
    transport_mode = shipping_constraints.get('transport_mode', 'truck')
    
    # Weather impact calculation (key factor)
    weather_impact = 0
    if weather_conditions & 0b1111 == 0b1010:  # Check specific weather pattern
        weather_impact = -200  # Bad weather reduces capacity
    elif weather_conditions & 0b1100 == 0b1100:
        weather_impact = -100  # Moderate weather impact
    
    # Transport mode factors (another key factor)
    transport_factor = {
        'truck': 0,
        'train': 200,
        'ship': 500,
        'plane': -150
    }.get(transport_mode, 0)
    
    # Calculate actual capacity based on what truly matters
    capacity = base_capacity + weather_impact + transport_factor
    
    # Misleading conditional that looks important but has no effect
    if route_optimization > 2.5:
        potential_capacity = capacity + 300
    else:
        potential_capacity = capacity + 0
    
    # This tuple unpacking looks important but doesn't affect the result
    dimensions = shipping_constraints.get('dimensions', (0, 0, 0))
    length, width, height = dimensions
    volume_constraint = length * width * height
    
    # More misleading calculations
    if volume_constraint > 10000:
        theoretical_adjustment = 50
    else:
        theoretical_adjustment = 25
    
    # The priority calculation is what actually matters
    priority_adjustment = priority_items * 50
    
    # Final calculation - only base_capacity, weather_impact, transport_factor and priority_adjustment matter
    optimal_capacity = capacity + priority_adjustment
    
    return optimal_capacity

# Test data
inventory = [
    {'id': 'A1', 'volume': 50, 'priority': 3},
    {'id': 'B2', 'volume': 30, 'priority': 1},
    {'id': 'C3', 'volume': 80, 'priority': 4},
    {'id': 'D4', 'volume': 20, 'priority': 2},
    {'id': 'E5', 'volume': 60, 'priority': 3}
]

shipping_constraints = {
    'weather_code': 0b1010,  # Binary representation of weather conditions
    'transport_mode': 'train',
    'fuel': 80,
    'destinations': [
        {'name': 'Warehouse A', 'distance': 120, 'importance': 3},
        {'name': 'Warehouse B', 'distance': 80, 'importance': 2}
    ],
    'dimensions': (20, 15, 10)
}

# Calculate the optimal container capacity
optimal_capacity = calculate_optimal_container_capacity(inventory, shipping_constraints)
print(f"Result: {optimal_capacity}")