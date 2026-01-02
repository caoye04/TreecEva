def calculate_adjusted_mean(data_slice):
    raw_sum = sum(data_slice)
    count = len(data_slice)
    mean_value = raw_sum / count if count > 0 else 0

    # Apply adjustment based on distribution skew
    below_mean = [x for x in data_slice if x < mean_value]
    above_mean = [x for x in data_slice if x > mean_value]
    skew_factor = len(above_mean) - len(below_mean)

    adjusted_mean = mean_value + (skew_factor * 0.05)
    return round(adjusted_mean, 4)

# Simulate sensor data with noise filtering
data_stream = [3.2, 4.1, 2.8, 5.6, 4.4, 3.9, 6.1, 5.0, 4.7, 5.3, 3.5, 4.9]
noise_threshold = 2.5
filtered_data = [x for x in data_stream if x > noise_threshold]

# Extract relevant window using slicing
window_start = 2
window_end = -1
processed_data = filtered_data[window_start:window_end]  # Critical slice

# Auxiliary computations (some irrelevant)
temp_stats = {
    'max_val': max(processed_data),
    'min_val': min(processed_data),
    'range_val': max(processed_data) - min(processed_data)
}

# Dummy transformation chain (distractor)
doubled_temp = [2 * x for x in processed_data]
decayed_values = [x * 0.95**i for i, x in enumerate(doubled_temp)]
shadow_metric = sum(decayed_values) / len(decayed_values) if decayed_values else 0

# Unused sorting operation (dead code path - distractor)
sorted_desc = sorted(processed_data, reverse=True)
midpoint_guess = sorted_desc[len(sorted_desc)//2] if sorted_desc else 0

# Core computation leading to answer
final_score = calculate_adjusted_mean(processed_data)

# Print result for extraction
print(f"Result: {final_score}")