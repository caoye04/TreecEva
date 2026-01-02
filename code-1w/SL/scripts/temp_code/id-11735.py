from collections import defaultdict, Counter

# Simulate sensor data with noise and redundant readings
data_stream = [104, 102, 105, 103, 104, 106, 108, 107, 105, 109, 108, 106, 104, 105, 107]

# Misleading preprocessing: normalize around arbitrary baseline
drift_correction = sum(data_stream[:5]) // 5
normalized_readings = [x - drift_correction for x in data_stream]

# Extract patterns using modulo cycles (relevant for anomaly detection)
cycle_modulo = 3
modular_pattern = [val % cycle_modulo for val in normalized_readings]

# Buffer to hold processed segments
data_buffer = []
segment_window = 5

for i in range(0, len(normalized_readings) - segment_window + 1):
    segment = normalized_readings[i:i + segment_window]
    avg_segment = sum(segment) / len(segment)
    variance = sum((x - avg_segment) ** 2 for x in segment) / len(segment)
    peak = max(segment)
    trough = min(segment)
    
    # Irrelevant transformations (distractors)
    inverted_sum = sum([1 / (abs(x) + 1) for x in segment])  # unused
    entropy_approx = 0.0
    freq_counter = Counter(segment)
    for count in freq_counter.values():
        entropy_approx -= (count / len(segment)) * (count / len(segment))  # misleading metric
    
    # Relevant metrics
    stability_index = int(peak - trough)
    reliability_flag = 1 if variance < 4.0 else 0
    
    # Store structured block
    data_buffer.append({
        'window_start': i,
        'average': avg_segment,
        'stability': stability_index,
        'valid': reliability_flag,
        'pattern_key': tuple(modular_pattern[i:i + segment_window])
    })

# Secondary processing: aggregate across valid windows
status_log = []
defaulted_counts = defaultdict(int)

rolling_validation = 0
for entry in data_buffer:
    defaulted_counts[entry['pattern_key']] += 1  # track key reuse
    rolling_validation ^= entry['stability']  # bitwise accumulation (red herring)
    if entry['valid']:
        status_log.append(entry['average'])

# Another distraction: analyze log frequency patterns
log_counter = Counter(status_log)
dominant_frequency = max(log_counter.values())

# Core logic hidden among distractions
def calculate_stability_contribution(stable_blocks):
    total = 0
    for block in stable_blocks:
        if block['valid']:
            # Weight by inverse of stability index (lower = better)
            weight = 1.0 / (block['stability'] + 1)
            total += weight * block['average']
    return total

# More red herrings
baseline_shift = sum(normalized_readings) % 7  # unused
auxiliary_metric = len(defaulted_counts) * baseline_shift  # irrelevant

# Critical function that determines final score
def calculate_final_score(buffer):
    # Count how many transitions between high and low averages
    filtered_averages = [e['average'] for e in buffer if e['valid']]
    if not filtered_averages:
        return 0
    
    # Compute oscillation score using XOR on rounded diffs
    diffs = [int(round(filtered_averages[i+1] - filtered_averages[i])) for i in range(len(filtered_averages)-1)]
    oscillation_key = 0
    for d in diffs:
        oscillation_key ^= abs(d)  # use XOR to compress trend changes
    
    # Actual answer derived from weighted contribution
    base_contribution = calculate_stability_contribution(buffer)
    adjustment = oscillation_key % 4
    
    # Final deterministic computation
    final_value = int(base_contribution) + adjustment
    
    # Introduce a dummy transformation (not affecting result)
    temp_scale = final_value * 0.99
    temp_scale = round(temp_scale)  # dead computation
    
    return final_value

# Execute critical statement
final_score = calculate_final_score(data_buffer)
print(f"Target result: {final_score}")