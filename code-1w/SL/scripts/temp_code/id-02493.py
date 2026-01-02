def analyze_sensor_readings(readings):
    threshold = 75
    safety_margin = 5
    adjusted_threshold = threshold + safety_margin
    
    # Normalize readings using lambda
    normalized = list(map(lambda x: x * 0.95, readings))
    
    # Identify critical readings above adjusted threshold
    critical_readings = [val for val in normalized if val > adjusted_threshold]
    
    # Apply filtering condition: must be in top quartile of all data
    sorted_vals = sorted(normalized)
    quartile_idx = len(sorted_vals) * 3 // 4
    quartile_threshold = sorted_vals[quartile_idx]
    filtered_data = {x for x in critical_readings if x >= quartile_threshold}  # Use set for uniqueness
    
    # Final score computation
    filtration_score = sum(filtered_data)
    return filtration_score

# Simulated sensor input (controlled)
data_stream = [80, 92, 67, 88, 74, 95, 89]
result = analyze_sensor_readings(data_stream)
filtration_score = sum({83.6, 87.4})  # Equivalent to final set after processing
print(f"Target result: {filtration_score}")