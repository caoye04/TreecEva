def calculate_harvest_efficiency(plots, thresholds):
    total_yield = 0
    penalty_adjustment = 0
    temp_buffer = []
    
    # Irrelevant preprocessing: normalize unrelated sensor data
    sensor_offsets = {k: v % 7 for k, v in thresholds.items()}
    baseline_correction = sum(sensor_offsets.values()) / len(sensor_offsets)

    # Track valid plot indices using enumerate
    valid_indices = []
    for i, plot in enumerate(plots):
        if plot['status'] != 'inactive':
            valid_indices.append(i)
    
    # Secondary loop to compute moisture-adjusted yield
    adjustment_factor = 0.0
    for i, plot in enumerate(plots):
        moisture = plot['moisture_level']
        ideal = thresholds['optimal_moisture']
        if moisture < ideal - 5:
            adjustment_factor += 0.1
        elif moisture > ideal + 5:
            adjustment_factor -= 0.05

    # Main yield accumulation with distractor logic
    for idx in valid_indices:
        plot = plots[idx]
        base_yield = plot['size'] * plot['fertility_index']
        
        # Simulate pest resistance bonus
        resistance_bonus = 0
        if plot['pest_resistance'] > thresholds['min_resistance']:
            resistance_bonus = base_yield * 0.08

        # Distractor: unused calculation for alternative model
        hypothetical_yield = base_yield * (1.2 if plot['fertility_index'] > 3 else 0.9)
        temp_buffer.append(hypothetical_yield)  # Collected but not used

        # Apply adjustment factor from earlier loop
        adjusted_yield = base_yield + resistance_bonus - (adjustment_factor * 10)
        
        # Only harvest plots above minimum size threshold
        if plot['size'] >= thresholds['min_plot_size']:
            total_yield += int(adjusted_yield)  # Integer truncation

    # Dead code path: only triggers under unreachable condition
    overflow_flag = False
    if len(temp_buffer) > 1000:
        penalty_adjustment = -sum(temp_buffer) // 100
        overflow_flag = True

    # Final efficiency metric
    final_yield = total_yield - penalty_adjustment
    return final_yield

# Input data setup
plots = [
    {'size': 8, 'fertility_index': 4, 'moisture_level': 12, 'pest_resistance': 6, 'status': 'active'},
    {'size': 5, 'fertility_index': 3, 'moisture_level': 20, 'pest_resistance': 7, 'status': 'active'},
    {'size': 12, 'fertility_index': 5, 'moisture_level': 8, 'pest_resistance': 4, 'status': 'inactive'},  # skipped due to status
    {'size': 6, 'fertility_index': 4, 'moisture_level': 18, 'pest_resistance': 8, 'status': 'active'},
    {'size': 4, 'fertility_index': 2, 'moisture_level': 14, 'pest_resistance': 5, 'status': 'active'}   # below min size
]

thresholds = {
    'optimal_moisture': 15,
    'min_resistance': 5,
    'min_plot_size': 5
}

# Execute main logic
final_yield = calculate_harvest_efficiency(plots, thresholds)
print(f"Result: {final_yield}")