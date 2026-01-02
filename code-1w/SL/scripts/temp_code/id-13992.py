import itertools

def preprocess_readings(readings):
    filtered = [r for r in readings if r > 0]
    normalized = [r / sum(filtered) for r in filtered]
    return normalized

def calculate_efficiency(data, limit):
    valid_points = []
    temp_sum = 0
    
    for i, val in enumerate(data):
        if val < limit:
            temp_sum += val ** 2
            valid_points.append(i)
        else:
            temp_sum -= val * 0.1  # minor correction
    
    efficiency = temp_sum / (len(valid_points) + 1)
    
    # Distractor: irrelevant string processing
    status_msg = "Processing complete"
    padded_msg = status_msg.ljust(20, '.')
    char_count = len(padded_msg.strip())
    
    return efficiency

# Sensor simulation parameters
data_stream = [0.5, 1.2, 0.8, 2.3, 0.4, 3.1, 1.9]
base_offset = 0.25
offset_adjusted = [v + base_offset for v in data_stream]

# Preprocessing stage
logged_data = preprocess_readings(offset_adjusted)

# Irrelevant dictionary operations (distractors)
stats_summary = {
    'count': len(logged_data),
    'max_val': max(logged_data),
    'min_val': min(logged_data)
}

stats_summary['range'] = stats_summary['max_val'] - stats_summary['min_val']
stats_summary['label'] = 'sensor_group_A'

# Threshold logic and final computation
threshold = 0.6
baseline_score = sum(1 for x in logged_data if x > threshold)

scaling_factor = 100

# Key statement
thermal_capacity = calculate_efficiency(logged_data, threshold) * scaling_factor

# Additional dead code path (not executed but adds cognitive load)
if False:
    debug_trace = list(itertools.accumulate(logged_data))
    print(f'Debug trace: {debug_trace}')

print(f'Target result: {thermal_capacity}')