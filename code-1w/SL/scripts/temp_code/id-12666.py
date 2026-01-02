def calculate_efficiency(data, limit):
    filtered = [x for x in data if x > limit]
    if not filtered:
        return 0.0
    avg = sum(filtered) / len(filtered)
    variance = sum((x - avg) ** 2 for x in filtered) / len(filtered)
    efficiency = (avg / (variance + 1)) if variance != 0 else avg
    return efficiency

# Sensor profile data (simulated temperature readings over time)
sensor_readings = [23.5, 24.1, 19.8, 25.6, 26.7, 22.3, 27.1, 28.4, 20.0, 21.9]
baseline_offset = 1.2
adjusted_readings = [x + baseline_offset for x in sensor_readings]  # Minor adjustment

# Threshold for significant thermal activity
activation_threshold = 24.0

# Determine operational mode based on initial checks (distractor logic)
mode_flag = 'active' if sum(1 for x in adjusted_readings if x > 25) > 3 else 'standby'
placeholder_value = 999  # Dead variable - no impact
dummy_calc = len(adjusted_readings) * 0.01  # Irrelevant computation

profile_data = adjusted_readings[:8]  # Use first 8 readings only
threshold = activation_threshold - 0.5
scaling_factor = 100.0

# Key computational step
thermal_capacity = calculate_efficiency(profile_data, threshold) * scaling_factor

# Additional irrelevant tracking
status_log = []
for reading in sensor_readings:
    status_log.append('high' if reading > 25 else 'normal')

# Output result
print(f"Result: {thermal_capacity}")