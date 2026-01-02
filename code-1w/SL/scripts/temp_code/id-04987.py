def calculate_stability_index(readings):
    base_offset = 10
    adjustment_factor = 0.5
    temp_buffer = []
    cumulative_drift = 0
    stability_sum = 0
    
    for reading in readings:
        # Irrelevant transformation (distractor)
        processed = (reading * 2 + base_offset) / 3.5
        temp_buffer.append(processed)
        
        # Actual logic: track drift from ideal baseline (50)
        drift = abs(reading - 50)
        cumulative_drift += drift
        
        # Conditional expression (required Python feature)
        correction = adjustment_factor if reading > 45 else -adjustment_factor
        stability_sum += drift - correction
    
    # Secondary loop with early break (suggested paradigm)
    filtered_readings = []
    for val in readings:
        if val < 30:
            break
        filtered_readings.append(val)
    
    # Dummy calculation using filtered data (semi-relevant, distractor)
    dummy_avg = sum(filtered_readings) / len(filtered_readings) if filtered_readings else 0
    
    # Core result computation (depends only on cumulative_drift and length)
    n = len(readings)
    energy_threshold = int((cumulative_drift / n) * 10) if n > 0 else 0
    
    # Extra unrelated state tracking (interference)
    outlier_count = sum(1 for x in readings if x < 20 or x > 80)
    consistency_flag = len(temp_buffer) == len(readings)
    
    return energy_threshold

# Simulated sensor readings (deterministic input)
readings = [52, 48, 55, 45, 50, 53, 47, 51]

# Key execution point
energy_threshold = calculate_stability_index(readings)

# Output result as required
print(f"Result: {energy_threshold}")