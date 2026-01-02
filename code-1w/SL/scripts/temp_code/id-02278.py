import math

# Simulated sensor array data (irrelevant initialization)
sensor_matrix = [[(i * j + 1) % 7 for j in range(5)] for i in range(6)]
baseline_offset = sum(sum(row) for row in sensor_matrix) / len(sensor_matrix)

def normalize_readings(data):
    # Distractor function: not used in final computation path
    return [[x / (max(row) + 1e-8) for x in row] for row in data]

def encode_sequence(seq):
    # Dead code path: looks relevant but unused
    return [format(x, '03b') for x in seq]

# Core signal processing chain
raw_signals = [18, 27, 12, 36, 45, 54, 21]
scaling_factor = 0.75
adjusted_signals = [int(x * scaling_factor) for x in raw_signals]  # Apply attenuation

# Bit manipulation decoy
bit_shifted = []
for val in adjusted_signals:
    temp = (val << 2) ^ 5  # Irrelevant transformation
    bit_shifted.append(temp)

# Conditional filtering with red herring variables
valid_indices = []
overshoot_count = 0  # Unused metric
for idx, val in enumerate(adjusted_signals):
    if val > 20 and idx % 2 == 1:
        overshoot_count += 1  # Tracking irrelevant stat
    if 10 < val < 50:
        valid_indices.append(idx)

filtered_pairs = [(i, adjusted_signals[i]) for i in valid_indices]

# Decoy data structure
redundant_map = {i: {'raw': raw_signals[i], 'adj': adjusted_signals[i], 'flag': i in valid_indices} for i in range(len(raw_signals))}

# Real processing begins: tuple unpacking and conditional expression
paired_deltas = []
for i in range(len(filtered_pairs) - 1):
    curr_idx, curr_val = filtered_pairs[i]
    next_idx, next_val = filtered_pairs[i + 1]
    delta = next_val - curr_val
    # Conditional expression with misleading default
    category = 'stable' if abs(delta) < 10 else ('rising' if delta > 0 else 'falling')
    paired_deltas.append((delta, category))

# Set operations: core concept
unique_magnitudes = set(abs(d[0]) for d in paired_deltas)
even_deltas = {d for d in unique_magnitudes if d % 2 == 0}
threshold_candidates = even_deltas | {12, 18}  # Union with decoy values

# Create threshold map with distractor keys
threshold_map = {}
for k in ['t1', 't2', 'critical', 'aux', 'calib']:
    if k == 't1':
        threshold_map[k] = 6
    elif k == 'critical':
        threshold_map['critical'] = max(threshold_candidates) if threshold_candidates else 0
    else:
        threshold_map[k] = sum(adjusted_signals) % 19  # Irrelevant assignments

# Processed data construction using tuple unpacking
processed_data = []
running_total = 0
for delta, cat in paired_deltas:
    running_total += abs(delta)
    # Use of conditional expression
    status_flag = 1 if cat == 'rising' else (2 if cat == 'falling' else 0)
    processed_data.append((abs(delta), status_flag, math.log(abs(delta) + 1)))

# Critical function with multiple concepts
def analyze_signal(signal_tuples, limits):
    # Modular arithmetic distraction
    checksum = 0
    for t in signal_tuples:
        checksum = (checksum + t[1] * 7) % 23
    
    # Real logic: depends only on critical threshold
    critical_level = limits.get('critical', 10)
    aggregate = 0
    decay_factor = 0.9
    
    for i, (mag, flag, log_val) in enumerate(signal_tuples):
        # Weighted accumulation with exponential decay
        weight = decay_factor ** i
        if mag > critical_level:
            aggregate += mag * weight * 1.5
        else:
            aggregate += mag * weight
    
    # Final adjustment using set difference (core concept)
    magnitudes = {t[0] for t in signal_tuples}
    outliers = magnitudes - {m for m in magnitudes if m <= critical_level}
    penalty = len(outliers) * 2.5
    
    result = aggregate - penalty
    
    # Dead code branch (never executed due to logic)
    if len(signal_tuples) > 100:
        backup = sum(magnitudes) / len(magnitudes)
        result = backup  # Never reached
        
    return result

# Execution point of interest
final_diagnostic = analyze_signal(processed_data, threshold_map)

print(f"Result: {final_diagnostic}")