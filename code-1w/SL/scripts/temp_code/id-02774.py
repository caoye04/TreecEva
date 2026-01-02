import math

# Simulated system telemetry data
telemetry_stream = [14, 28, 19, 35, 22, 47, 13, 29]

# Irrelevant constants (distractors)
MAX_BUFFER_SIZE = 1024
RETRY_LIMIT = 3
DEBUG_MODE = True

# Noise injection for signal processing (unused red herring)
noise_floor = sum([math.sin(i * 0.5) for i in range(len(telemetry_stream))])

# Real-time filtering (partially relevant)
filtered_data = [x for x in telemetry_stream if x > 20]

# Historical baselines (distractor data)
baseline_averages = {
    'Q1': 23.1,
    'Q2': 26.4,
    'Q3': 25.8,
    'Q4': 24.9
}

# Complex nested structure with mixed data types (distractor)
system_state = {
    'status': 'ACTIVE',
    'payload': [
        {'id': 101, 'value': 42},
        {'id': 102, 'value': filtered_data[1] * 2},
        {'id': 103, 'value': None}
    ],
    'log': set(telemetry_stream),
    'cache': {i: telemetry_stream[i] ** 2 for i in range(len(telemetry_stream))}
}

# Auxiliary function - looks important but not used in final computation
def calculate_variance(data):
    mean = sum(data) / len(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

# Another decoy function with misleading name
def normalize_weights(w_list):
    total = sum(w_list)
    return [w / total for w in w_list]

# Bit manipulation red herring
def scramble_value(val):
    return ((val << 3) ^ 0xFF) & 0xFFFF

scrambled_values = [scramble_value(x) for x in filtered_data]

# Core performance metrics (this is where relevant logic begins)
metrics = {
    'throughput': len(filtered_data) * 10,
    'stability': sum(filtered_data) // len(filtered_data),
    'consistency': filtered_data[-1] - filtered_data[0],
    'response_time': 100 - (telemetry_stream[1] + telemetry_stream[4])
}

# Weight configuration for evaluation (critical)
weights = [0.4, 0.3, 0.2, 0.1]

# Redundant transformation (distractor)
weighted_metrics = {
    key: val * weights[i] for i, (key, val) in enumerate(metrics.items())
}

# Unused normalization path
temp_normalized = [v / 100 for v in metrics.values()]

# Key function that computes the answer
def evaluate_performance(metrs, wts):
    # Extract values in fixed order
    ordered_vals = [
        metrs['throughput'],
        metrs['stability'],
        metrs['consistency'],
        metrs['response_time']
    ]
    
    # Apply weights
    weighted_sum = sum(ordered_vals[i] * wts[i] for i in range(len(wts)))
    
    # Secondary adjustment based on system health (bit check)
    if len(filtered_data) & 1:  # odd length adds bonus
        weighted_sum += 5
    
    # Additional distraction: unused smoothing
    smoothed = weighted_sum * 0.95
    
    # Final adjustment based on data range
    data_range = max(filtered_data) - min(filtered_data)
    if data_range > 25:
        weighted_sum -= 2
    else:
        weighted_sum += 1
    
    return int(weighted_sum)

# Dead code path - never called
def log_diagnostics(state):
    print(f"Diagnostics: {state['status']}")

# Trigger execution
current_state = system_state['status']

# Critical statement
final_score = evaluate_performance(metrics, weights)

# Additional irrelevant slicing operation (meets language requirement)
segment_snapshot = telemetry_stream[2:6:1]
summary_slice = segment_snapshot[::-1]

# Set operations (meets language requirement)
unique_telemetry = set(telemetry_stream)
excluded_set = {19, 22}
active_set = unique_telemetry - excluded_set

# Slicing on list (meets language requirement)
rolling_window = filtered_data[1:3]

# Output result as required
print(f"Target result: {final_score}")