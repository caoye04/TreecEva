def calculate_thermal_properties(efficiency_map):
    base_factor = 1.75
    adjustment = 0.89
    thermal_index = 0
    cumulative_stress = 0
    
    # Irrelevant diagnostic tracking (distractor)
    debug_log = []
    cycle_count = 0
    
    for temp, readings in efficiency_map.items():
        if temp < 20:
            continue  # Skip low temps
        
        peak_reading = max(readings) if readings else 0
        normalized_peak = peak_reading * base_factor
        
        # Real computation branch
        if normalized_peak > 50:
            thermal_index += int(normalized_peak // 10)
            
        # Distractor: complex but unused calculation
        safety_margin = (peak_reading * adjustment) ** 0.5
        reliability_score = 100 - safety_margin
        debug_log.append(reliability_score)
        
        # Accumulation with slicing relevance
        mid_readings = readings[1:-1]  # Exclude first and last
        cumulative_stress += sum(mid_readings) * (temp / 25)
        
        cycle_count += 1  # Tracking unused variable

    # Conditional expression used idiomatically
    fallback_value = 42 if not debug_log else 0
    
    # Key result computation
    raw_capacity = thermal_index * 15 + (cumulative_stress / (cycle_count or 1))
    thermal_capacity = int(raw_capacity - fallback_value)
    
    return thermal_capacity

# Setup input data
readings_data = {
    15: [10, 20, 30],      # Skipped due to temp < 20
    25: [45, 58, 60, 50],
    30: [55, 65, 70],
    35: [40, 52, 58, 60, 55]
}

# Mapping transformation (semi-relevant preprocessing)
efficiency_map = {k: [v[i] + i for i in range(len(v))] for k, v in readings_data.items()}

# Execute main logic
target_result = calculate_thermal_properties(efficiency_map)
print(f"Target result: {target_result}")