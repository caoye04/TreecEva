def calculate_final_score(raw_data, limits):
    # Preprocess: filter valid entries based on multiple criteria
    filtered = [x for x in raw_data if x > limits['min'] and x < limits['max']]
    
    # Irrelevant transformation: reverse and square (not used in final logic)
    reversed_squared = [y**2 for y in reversed(filtered)]
    temp_sum = sum(reversed_squared)  # Dead computation

    # Core logic: categorize and score
    high_vals = {x for x in filtered if x >= limits['threshold']}
    medium_vals = {x for x in filtered if limits['min'] < x < limits['threshold']}
    
    # Scoring with weighted contributions
    score_a = len(high_vals) * 3
    score_b = len(medium_vals) * 2
    
    # Secondary path: analyze distribution using slicing
    sorted_vals = sorted(filtered)
    mid_section = sorted_vals[len(sorted_vals)//4 : 3*len(sorted_vals)//4]
    spread_bonus = len(mid_section) if sum(mid_section) > 0 else 0  # Conditional bonus

    # Dummy state tracking (distractor)
    stats = {
        'count': len(filtered),
        'peak': max(filtered) if filtered else 0,
        'ignored_ratio': (len(raw_data) - len(filtered)) / len(raw_data) if raw_data else 0
    }
    
    # Final aggregation
    base_score = score_a + score_b
    adjustment = spread_bonus // 2
    final_score = base_score + adjustment
    
    return final_score

# Input setup
sensor_readings = [12, 7, 15, 3, 9, 18, 4, 11, 6, 14, 20, 5]
config = {
    'min': 4,
    'max': 19,
    'threshold': 10
}

# Execution
result = calculate_final_score(sensor_readings, config)
print(f"Target result: {result}")