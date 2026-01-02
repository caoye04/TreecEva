from collections import defaultdict, Counter
import math

# Simulated sensor data acquisition
def acquire_sensor_data():
    raw_signals = [
        (1, [3, 1, 4, 1, 5, 9, 2, 6]),
        (2, [2, 7, 1, 8, 2, 8, 1, 8]),
        (3, [1, 6, 1, 8, 0, 3, 3, 9]),
        (4, [9, 9, 8, 8, 7, 7, 6, 6])
    ]
    metadata_log = {'version': '2.1', 'calibrated': True, 'units': 'mV'}
    return raw_signals, metadata_log

# Irrelevant helper – looks useful but unused in critical path
def compute_entropy(vector):
    counts = Counter(vector)
    total = len(vector)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

# Legacy function – appears important but not used
def legacy_normalization(data_list):
    max_val = max(max(seq) for _, seq in data_list)
    return [(sid, [val / max_val for val in seq]) for sid, seq in data_list]

# Core processing: filter and transform
def preprocess_sequence(seq, min_threshold=2):
    # Apply non-linear transformation
    transformed = [int(math.sqrt(x)) if x >= 1 else 0 for x in seq]
    # Mask low-amplitude noise
    filtered = [x if x >= min_threshold else 0 for x in transformed]
    return filtered

# Another red herring: computes statistics but not essential
def analyze_amplitude_patterns(signal_matrix):
    pattern_freq = defaultdict(int)
    for _, seq in signal_matrix:
        key_pattern = tuple(1 if x > 0 else 0 for x in seq)
        pattern_freq[key_pattern] += 1
    return dict(pattern_freq)

# Main filtering logic with distractors
raw_data, config = acquire_sensor_data()

decoy_analysis = [compute_entropy(seq) for _, seq in raw_data]
decoy_normalized = legacy_normalization(raw_data)

# Actual relevant preprocessing
processed_entries = []
for sensor_id, sequence in raw_data:
    cleaned = preprocess_sequence(sequence, min_threshold=2)
    processed_entries.append((sensor_id, cleaned))

# Misleading aggregation (unused later)
temp_aggregate = [sum(seq) for _, seq in processed_entries]
baseline_shift = sum(temp_aggregate) // len(temp_aggregate)

# Real threshold mapping based on id
threshold_map = defaultdict(lambda: 1)
for sid, _ in processed_entries:
    if sid % 2 == 0:
        threshold_map[sid] = 2
    else:
        threshold_map[sid] = 1

# Filtering entries by activity level (non-zero elements)
active_mask = []
for sid, seq in processed_entries:
    active_count = sum(1 for x in seq if x > 0)
    active_mask.append((sid, active_count))

# Only keep sensors with sufficient active components
min_activity = 3
filtered_data = [
    (sid, seq) for (sid, seq), (_, act) in zip(processed_entries, active_mask)
    if act >= min_activity
]

# Decoy clustering attempt (never used)
clustering_probe = []
for sid, seq in filtered_data:
    magnitude = sum(x**2 for x in seq) ** 0.5
    clustering_probe.append((sid, round(magnitude, 3)))

# Critical function containing answer logic
def process_signals(entries, thresholds):
    accumulator = 0
    history = []
    for sensor_id, readings in entries:
        threshold = thresholds[sensor_id]
        # Count how many readings meet dynamic threshold
        triggered = 0
        running_max = 0
        for val in readings:
            if val >= threshold:
                triggered += 1
                if val > running_max:
                    running_max = val
        # Compute contribution using triggered count and max
        if triggered > 0:
            contribution = triggered * running_max
            # Special rule: even sensors get squared contribution
            if sensor_id % 2 == 0:
                contribution = contribution ** 2
            accumulator += contribution
        history.append(triggered)
    
    # Final adjustment based on history variance (if any)
    if len(history) > 1:
        mean_hist = sum(history) / len(history)
        variance = sum((x - mean_hist) ** 2 for x in history) / len(history)
        adjustment = int(variance * 10)
        accumulator -= adjustment
    else:
        accumulator -= 5  # default penalty
    
    return accumulator

# Execute main computation
final_output = process_signals(filtered_data, threshold_map)

# Logging decoys
debug_stats = {
    'total_processed': len(processed_entries),
    'after_filtering': len(filtered_data),
    'decoy_entropy_avg': sum(decoy_analysis)/len(decoy_analysis)
}

# Output the result as required
print(f"Result: {final_output}")