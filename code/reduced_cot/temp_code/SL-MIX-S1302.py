def calculate_ride_efficiency():
    rides_data = [
        {'name': 'Dragon Coaster', 'popularity': 85, 'maintenance': 12},
        {'name': 'Sky Dancer', 'popularity': 76, 'maintenance': 8},
        {'name': 'Aqua Twister', 'popularity': 92, 'maintenance': 15},
        {'name': 'Gravity Drop', 'popularity': 68, 'maintenance': 10}
    ]
    
    efficiency_lookup = {
        0: 5, 1: 3, 2: 8, 3: 2, 4: 7,
        5: 4, 6: 9, 7: 1, 8: 6, 9: 0
    }
    
    adjustment_factors = { 'Dragon Coaster': 2, 'Sky Dancer': 1, 'Aqua Twister': 3, 'Gravity Drop': 1 }
    
    efficiency_index = 0
    
    for ride in rides_data:
        base_score = ride['popularity'] - ride['maintenance']
        mod_result = base_score % 10
        
        if mod_result in [0, 2, 4, 6, 8]:
            lookup_value = efficiency_lookup[mod_result]
            adjusted_value = lookup_value * adjustment_factors[ride['name']]
            efficiency_index += adjusted_value
        else:
            efficiency_index -= mod_result
        
        # Early termination condition
        if efficiency_index > 30:
            break
    
    # Final adjustment using dictionary comprehension
    modifiers = {k: v for k, v in efficiency_lookup.items() if k % 2 == 0}
    modifier_sum = sum(modifiers.values())
    efficiency_index = (efficiency_index + modifier_sum) % 23
    
    return efficiency_index

result = calculate_ride_efficiency()
print(f"Result: {result}")