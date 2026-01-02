def process_signals(data, threshold):
    magnitude = lambda x: x * x if x > 0 else 0
    processed = []
    temp_sum = 0
    
    for val in data:
        if val < 0:
            temp_sum += abs(val)
            continue
        squared = magnitude(val)
        if threshold(squared):
            processed.append(squared)
    
    # Irrelevant tracking variables
    avg_magnitude = sum(processed) / len(processed) if processed else 0
    outlier_count = 0
    for p in processed:
        if p > 3 * avg_magnitude:
            outlier_count += 1

    compression_factor = 1.5
    compressed = [p / compression_factor for p in processed]
    
    # Secondary processing with red herring logic
    adjusted_values = []
    scale = 2.0
    for c in compressed:
        adjusted = c * scale
        if adjusted > 50:
            adjusted -= 10
        adjusted_values.append(adjusted)
    
    final_output = int(sum(adjusted_values))
    return final_output

# Simulate sensor input
raw_sensor_data = [3, -5, 4, 7, -2, 8, 1, 6, -9, 5]

# Filtering irrelevant noise (distractor preprocessing)
mean_val = sum(raw_sensor_data) / len(raw_sensor_data)
filtered_data = [x for x in raw_sensor_data if x >= mean_val or x == -5]

# Threshold function using lambda (required feature)
threshold_func = lambda x: x % 2 == 0 and x > 10

# Additional unrelated computation (distractor)
redundant_calc = set()
for i in range(len(filtered_data)):
    for j in range(i + 1, len(filtered_data)):
        redundant_calc.add(abs(filtered_data[i] - filtered_data[j]))

# Unused helper set operation (set operations used as required)
duplicate_check = set([x for x in raw_sensor_data if raw_sensor_data.count(x) > 1])

# Key execution point
final_output = process_signals(filtered_data, threshold_func)

# Output result
print(f"Result: {final_output}")