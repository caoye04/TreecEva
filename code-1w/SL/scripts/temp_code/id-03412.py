def calculate_thermal_output(profile, limit):
    adjusted_values = [x * 1.75 for x in profile if x > limit]
    offset = sum([x for x in profile if x <= limit]) * 0.1
    filtered_data = profile[::2]  # every other reading
    temp_sum = 0
    for val in adjusted_values:
        temp_sum += val ** 0.5
    
    # Irrelevant signal correction (distractor)
    correction_factor = 0.0
    if len(filtered_data) > 5:
        correction_factor = sum(filtered_data[:3]) / 3.0
    smoothed_data = [abs(x - correction_factor) for x in filtered_data]

    # Secondary computation that looks important but isn't used
    baseline_estimate = sum(smoothed_data) / len(smoothed_data) if smoothed_data else 0
    decay_rate = 0.9
    projected_loss = 0
    for i in range(3):
        projected_loss += baseline_estimate * (decay_rate ** i)

    # Actual result calculation
    raw_output = temp_sum + offset
    efficiency_ratio = 0.88
    final_output = raw_output * efficiency_ratio
    return int(final_output)

# Sensor data from thermal array (simulated)
data_readings = [12, 45, 67, 23, 78, 88, 34, 56, 91, 15]

# Redundant preprocessing (distractor)
sorted_readings = sorted(data_readings)
median_value = sorted_readings[len(sorted_readings)//2]
average_reading = sum(data_readings) / len(data_readings)

# Threshold logic based on dynamic condition
dynamic_threshold = average_reading * 0.75

# Key assignment statement
thermal_capacity = calculate_thermal_output(data_readings, dynamic_threshold)

# Output result as required
print(f"Result: {thermal_capacity}")