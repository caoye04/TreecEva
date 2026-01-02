from collections import defaultdict, Counter

# Simulate sensor data with timestamps and readings
timestamps = [101, 102, 103, 104, 105, 106, 107, 108]
raw_readings = [23.5, 24.1, 23.9, 25.2, 24.8, 26.0, 25.6, 25.9]

# Irrelevant auxiliary data (distractor)
status_codes = ['OK', 'OK', 'WARN', 'OK', 'OK', 'ERROR', 'OK', 'OK']
error_flags = [False, False, True, False, False, True, False, False]

# Data processing pipeline
readings_by_hour = defaultdict(list)
for t, r in zip(timestamps, raw_readings):
    hour = t // 100
    readings_by_hour[hour].append(r)

# Extract relevant processed data
processed_data = []
smoothing_factor = 0.1
prev = 0
for i, reading in enumerate(raw_readings):
    # Apply exponential smoothing (semi-relevant computation)
    smoothed = smoothing_factor * reading + (1 - smoothing_factor) * prev if i > 0 else reading
    deviation = abs(reading - smoothed)
    processed_data.append({
        'index': i,
        'raw': reading,
        'smoothed': round(smoothed, 3),
        'deviation': round(deviation, 3)
    })
    prev = smoothed

# Secondary distractor: analyze status patterns (not used later)
status_counter = Counter(status_codes)
flag_transitions = 0
for i in range(1, len(error_flags)):
    if error_flags[i] != error_flags[i-1]:
        flag_transitions += 1

# Auxiliary function for scoring
def calculate_stability_score(data_chunk):
    if not data_chunk:
        return 0
    deviations = [entry['deviation'] for entry in data_chunk]
    return round(sum(deviations) / len(deviations), 3)

# Another unused helper (dead code path - distractor)
def predict_next_value(data_list):
    if len(data_list) < 2:
        return 0
    trend = data_list[-1]['raw'] - data_list[-2]['raw']
    return data_list[-1]['raw'] + trend

# Main scoring logic
def compute_final_score(data):
    total_weighted_score = 0.0
    base_offset = 10
    for idx, record in enumerate(data):
        raw_val = record['raw']
        dev_score = 1 / (1 + record['deviation'])  # inverse deviation weighting
        
        # Conditional bonus for even indices (arbitrary rule)
        bonus = 2.5 if idx % 2 == 0 else 0
        
        # Accumulate weighted contribution
        contribution = (raw_val + dev_score) * (1 + idx * 0.05) + bonus
        total_weighted_score += contribution
    
    # Additional adjustment based on pattern count (semi-relevant)
    high_deviation_count = sum(1 for d in data if d['deviation'] > 0.3)
    penalty = high_deviation_count * 1.75
    
    # Final composition
    final = total_weighted_score - penalty + base_offset
    
    # Distractor variables inside function
    avg_raw = sum(d['raw'] for d in data) / len(data)
    peak_dev = max(d['deviation'] for d in data)
    
    return int(round(final))

# Execute main computation
intermediate_sum = sum(int(t % 100) for t in timestamps)  # irrelevant sum
placeholder_result = predict_next_value(processed_data)  # dead function call

final_score = compute_final_score(processed_data)
print(f"Result: {final_score}")