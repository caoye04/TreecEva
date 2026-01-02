import math

# Simulated sensor array data (irrelevant initial setup)
sensor_grid = [[(i + j) % 7 for j in range(5)] for i in range(6)]
scaling_factor = 1.75
dummy_counter = 0

# Irrelevant transformation chain
transformed_grid = []
for row in sensor_grid:
    transformed_row = []
    for val in row:
        transformed_row.append(int((val * scaling_factor) ** 1.1) % 9)
    transformed_grid.append(transformed_row)

temp_aggregate = sum(sum(row) for row in transformed_grid)

# Real signal preprocessing begins here
raw_signal = [0.3, 0.8, 1.4, 2.1, 1.9, 0.7, 0.2, -0.5, -1.1, -1.8, -2.0, -1.3, -0.4]
filtered_signal = [x for x in raw_signal if abs(x) > 0.6]
smoothed_signal = []
for i in range(len(filtered_signal)):
    window = filtered_signal[max(0, i-1):min(i+2, len(filtered_signal))]
    smoothed_signal.append(sum(window) / len(window))

# Decoy function - never called
def legacy_process(data):
    return [d * 0.9 for d in data[::-1]]

# Actual processing function
def process_segment(segment, mode='adaptive'):
    if mode == 'adaptive':
        base = sum(abs(x) for x in segment) / len(segment)
        return base ** 0.5 * 10
    return max(segment) - min(segment)

# Apply processing
segmented_data = [smoothed_signal[i:i+3] for i in range(0, len(smoothed_signal), 3)]
processed_data = []
for seg in segmented_data:
    if len(seg) >= 2:
        processed_data.append(process_segment(seg))

# Red herring: complex but unused structure
redundant_analysis = {
    'metrics': [
        {'peak': max(smoothed_signal), 'trough': min(smoothed_signal)},
        {'variance': sum((x - sum(smoothed_signal)/len(smoothed_signal))**2 for x in smoothed_signal) / len(smoothed_signal)}
    ],
    'flags': {f'alert_{i}': False for i in range(5)}
}

# Threshold configuration map (used later)
threshold_map = {
    'level_1': 12.0,
    'level_2': 8.5,
    'level_3': 5.0
}

# Decoy list comprehensions
_ = [math.sin(x) for x in range(1, 10) if x % 3 == 0]
_ = [x for x in processed_data if x > 100]  # No such values

# Critical diagnostic function
def analyze_signal(data, thresholds):
    count_high = len([x for x in data if x > thresholds['level_1']])
    count_mid = len([x for x in data if thresholds['level_2'] < x <= thresholds['level_1']])
    count_low = len([x for x in data if thresholds['level_3'] < x <= thresholds['level_2']])
    
    # Distractor variables
    total_entries = len(data)
    avg_value = sum(data) / total_entries if total_entries else 0
    
    # Complex conditional weighting
    weight_high = 3.0 if count_high > 0 else 0.5
    weight_mid = 2.0 if count_mid > 1 else 0.8
    weight_low = 1.0 if count_low >= 1 else 0.3
    
    # Final computation path
    raw_score = count_high * weight_high + count_mid * weight_mid + count_low * weight_low
    
    # Normalization using bit manipulation (distraction)
    shift_correction = (count_high ^ count_mid) & 7
    normalized = raw_score * (1.1 - shift_correction * 0.01)
    
    # Additional irrelevant check
    if count_high > count_low and avg_value > 5:
        normalized *= 1.05
    
    return int(normalized * 10) / 10.0  # Round to one decimal

# Execute critical statement
final_diagnostic = analyze_signal(processed_data, threshold_map)

# Print result as required
print(f"Target result: {final_diagnostic}")