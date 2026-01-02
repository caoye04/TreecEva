def process_sensor_readings(readings):
    filtered = [r for r in readings if r > 18.5]
    adjusted = [r * 1.02 for r in filtered]
    return adjusted


def monitor_system_state(temps):
    avg = sum(temps) / len(temps)
    variance = sum((t - avg) ** 2 for t in temps) / len(temps)
    status_flag = 'STABLE' if variance < 5 else 'FLUCTUATING'
    return avg, variance, status_flag


def calculate_efficiency(data, limit):
    clipped = [min(d, limit) for d in data]
    weighted = [d * (0.9 + i * 0.01) for i, d in enumerate(clipped)]
    rolling_avg = []
    for i in range(2, len(weighted)):
        rolling_avg.append(sum(weighted[i-2:i+1]) / 3)
    valid_roll = [r for r in rolling_avg if r > 20]
    if len(valid_roll) == 0:
        return 0
    efficiency_score = sum(valid_roll) / len(valid_roll)
    penalty = 0
    for v in valid_roll:
        if v > 25:
            penalty += 0.5
    final_score = efficiency_score - penalty
    return max(final_score, 5)

# Simulated sensor data from thermal array
temperature_log = [19.2, 21.5, 17.8, 23.1, 24.6, 16.9, 25.3, 22.7, 20.4]

# Irrelevant transformation - distractor
normalized_log = [round((t - 16) / 10, 2) for t in temperature_log]
duplicate_check = {i: temp for i, temp in enumerate(temperature_log)}

# Data slicing and processing chain
processed_temps = process_sensor_readings(temperature_log)
baseline, variation, state = monitor_system_state(processed_temps)

# Secondary irrelevant computation - dead path
temp_differences = []
for i in range(1, len(temperature_log)):
    temp_differences.append(temperature_log[i] - temperature_log[i-1])
mean_diff = sum(temp_differences) / len(temp_differences)

# Key execution point
threshold = 24.0
logged_data = processed_temps[1:7]  # Slice of interest
thermal_capacity = calculate_efficiency(logged_data, threshold)

# Additional red herring variables
compression_ratio = 1.07
scaling_factor = sum(normalized_log) * 0.05
auxiliary_sum = sum(duplicate_check.values()) // len(duplicate_check)

# Final output
print(f"Result: {thermal_capacity}")