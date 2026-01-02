def calculate_adjusted_average(readings, limit):
    filtered = [r for r in readings if r > limit]
    temp_sum = sum(filtered)
    count = len(filtered)
    
    # Distractor: Irrelevant computation on outliers
    outlier_count = len([r for r in readings if r < limit * 0.5])
    adjustment_factor = 1.0
    if outlier_count > 2:
        adjustment_factor = 0.9
    
    # More distraction: Simulate calibration (not actually used)
    calibration_offset = 0
    for i in range(min(3, len(readings))):
        if readings[i] % 2 == 0:
            calibration_offset += 0.1
    
    # Actual logic path
    if count == 0:
        return 0
    raw_avg = temp_sum / count
    
    # Apply hidden correction based on data spread
    variance_proxy = sum((r - raw_avg) ** 2 for r in filtered) / count
    if variance_proxy < 25:
        raw_avg += 2.5  # Stability bonus
    
    return int(raw_avg)  # Final score is integer

# Sensor readings in Celsius from a lab experiment
temperatures = [18, 25, 30, 12, 35, 40, 8, 22]
threshold = 20

# Misleading preprocessing
normalized_temps = [t * 1.05 for t in temperatures]
sorted_normalized = sorted(normalized_temps)
median_temp = sorted_normalized[len(sorted_normalized) // 2]

# Noise injection (unused)
noise_level = 0
for t in temperatures:
    if t > 25:
        noise_level += t * 0.01

# Key execution point
final_score = calculate_adjusted_average(temperatures, threshold)

# Output result
print(f"Result: {final_score}")