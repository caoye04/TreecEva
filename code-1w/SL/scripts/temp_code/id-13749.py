def calculate_final_score(values, importance):
    total = 0
    weight_sum = 0
    for i in range(len(values)):
        if importance[i] > 0.1:
            total += values[i] * importance[i]
            weight_sum += importance[i]
    return round(total / weight_sum) if weight_sum else 0

# Simulated sensor data (temperature readings in Celsius)
sensor_readings = [23.5, 24.1, 19.8, 22.0, 25.3, 20.4, 21.7, 26.0, 18.9, 24.5]

# Irrelevant transformation: normalize to Fahrenheit (not used in final computation)
fahrenheit_vals = [(c * 9/5) + 32 for c in sensor_readings]
discard_outliers = [f for f in fahrenheit_vals if 60 < f < 80]  # Distractor list

# Weight profile based on sensor reliability (decreasing confidence over time)
sensor_weights = [0.25, 0.24, 0.23, 0.22, 0.20, 0.18, 0.15, 0.10, 0.05, 0.02]

# Extract middle segment of data for analysis (slicing)
data_slice = sensor_readings[2:8]  # Focused on indices 2-7
temp_snapshot = sensor_readings[1:9:2]  # Unused slice with step (distractor)

# Adjust weights to match slice length
weight_slice = sensor_weights[2:8]

# Auxiliary calculation: average without weighting (not used in result)
raw_avg = sum(data_slice) / len(data_slice)

# Key statement
final_score = calculate_final_score(data_slice, weight_slice)

# Additional irrelevant tracking
status_flags = tuple(1 if x > 20 else 0 for x in data_slice)
activation_count = sum(status_flags)  # Semi-relevant but unused

print(f"Result: {final_score}")