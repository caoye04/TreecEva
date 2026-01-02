def calculate_stability_index(data):
    # Preprocessing: Normalize sensor readings
    normalized = [x / sum(data) for x in data]
    
    # Irrelevant transformation (distractor)
    squared_norms = list(map(lambda x: x**2, normalized))
    total_squared = sum(squared_norms)
    
    # Compute entropy-like dispersion metric (actual relevant logic)
    import math
    dispersion = -sum(p * math.log(p) for p in normalized if p > 0)
    
    # Simulate device-specific calibration offset (semi-relevant)
    calibration_factor = 1.78
    raw_index = dispersion * calibration_factor
    
    # Conditional adjustment based on data size (relevant)
    adjustment = 0.5 if len(data) > 5 else 0.2
    adjusted_index = raw_index + adjustment
    
    # Dead code path - never executed due to input constraints (dead code distractor)
    max_val = max(data)
    if max_val < 0:
        fallback = sum(data) / len(data)
        adjusted_index = fallback
    
    # Final thresholding using tuple unpacking and conditional expression
    low_bound, high_bound = (0.8, 2.1)
    energy_threshold = adjusted_index if low_bound <= adjusted_index <= high_bound else high_bound
    
    return energy_threshold

# Sensor readings from environmental monitoring unit
readings = [12, 15, 10, 8, 20, 14, 11]

# Auxiliary computation - irrelevant to final result (misleading variable)
peak_to_avg_ratio = max(readings) / (sum(readings) / len(readings))
drift_estimate = sum(abs(readings[i] - readings[i+1]) for i in range(len(readings)-1))

# Key execution point
energy_threshold = calculate_stability_index(readings)

# Output result
print(f"Result: {energy_threshold}")