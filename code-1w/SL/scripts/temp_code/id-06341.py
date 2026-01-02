def calculate_harvest_efficiency(plots, sensors):
    base_yield = 0
    adjustment_factor = 0.85
    outlier_threshold = 150
    cumulative_score = 0
    efficiency_log = []
    
    for i, (plot, sensor) in enumerate(zip(plots, sensors)):
        raw_value = plot['size'] * plot['fertility']
        
        # Irrelevant computation - simulates sensor noise filtering
        filtered_data = [x for x in sensor if x > 10]
        avg_sensor = sum(filtered_data) / len(filtered_data) if filtered_data else 0
        
        # Distractor: unused complex calculation
        hypothetical_max = (plot['size'] ** 2) // max(plot['fertility'], 1)
        
        if plot['irrigated']:
            raw_value *= 1.4
        
        if avg_sensor < 25:
            raw_value *= adjustment_factor
        
        # Real logic affecting result
        capped_value = min(raw_value, 200)
        adjusted_value = max(capped_value - 30, 10)
        
        efficiency_log.append(adjusted_value)
        
        # Only plots with high fertility contribute fully
        contribution = adjusted_value if plot['fertility'] >= 3 else adjusted_value * 0.6
        base_yield += contribution
    
    # Simulate multi-step aggregation
    valid_logs = {i: v for i, v in enumerate(efficiency_log) if v > 40}
    correction_term = len(valid_logs) * 2.5 if len(valid_logs) > 3 else 0
    
    # Unused set operation - distractor
    unique_adjusted = set(round(v * 0.1) for v in efficiency_log)
    
    # Final computation chain
    temp_result = base_yield + correction_term
    penalty = 0
    
    for log_val in efficiency_log:
        if log_val < 50:
            penalty += 5
    
    final_yield = int(temp_result - penalty)
    
    # Dead code path - misleading
    if len(sensors) > 10:
        final_yield = round(final_yield * 1.1)
    
    return final_yield

# Input data
plots = [
    {'size': 10, 'fertility': 4, 'irrigated': True},
    {'size': 8, 'fertility': 2, 'irrigated': False},
    {'size': 12, 'fertility': 5, 'irrigated': True},
    {'size': 9, 'fertility': 3, 'irrigated': True},
    {'size': 7, 'fertility': 1, 'irrigated': False}
]

sensors = [
    [20, 30, 15],
    [10, 5, 25],
    [40, 35, 50],
    [28, 32],
    [8, 12]
]

final_yield = calculate_harvest_efficiency(plots, sensors)
print(f"Target result: {final_yield}")