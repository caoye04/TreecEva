import math

def analyze_signal(x):
    # Irrelevant helper function (dead code path)
    return sum(xi ** 2 for xi in x if xi > 0.5)

def dummy_transform(data):
    # Distractor: looks important but unused in critical path
    return [d * 1.05 for d in data]

def validate_entry(record):
    # Misleading validation logic (not actually used in main flow)
    return all(isinstance(v, (int, float)) and v >= 0 for v in record.values())

def compute_entropy(values):
    # Red herring computation
    total = sum(values)
    probs = [v / total for v in values if v > 0]
    return -sum(p * math.log(p) for p in probs)

def extract_features(signal):
    # Unused feature engineering (decoy)
    return {
        'peak': max(signal),
        'rms': math.sqrt(sum(s**2 for s in signal) / len(signal)),
        'zero_crossings': sum(1 for i in range(1, len(signal)) if signal[i-1] * signal[i] < 0)
    }

def rotate_matrix(m):
    # Bit manipulation decoy
    size = len(m)
    for i in range(size // 2):
        for j in range(i, size - i - 1):
            temp = m[i][j]
            m[i][j] = m[size - 1 - j][i]
            m[size - 1 - j][i] = m[size - 1 - i][size - 1 - j]
            m[size - 1 - i][size - 1 - j] = m[j][size - 1 - i]
            m[j][size - 1 - i] = temp
    return m

def process_readings(data, calib):
    # Core logic buried among noise
    adjusted = []
    for i, row in enumerate(data):
        adjusted_row = []
        for j, val in enumerate(row):
            corrected = val * calib[i][j]
            adjusted_row.append(corrected)
        adjusted.append(adjusted_row)
    
    # Flatten with enumerate and zip (required feature)
    flat_adjusted = []
    for i, row in enumerate(adjusted):
        for j, val in enumerate(row):
            flat_adjusted.append((i, j, val))
    
    indexed_vals = [v for _, _, v in flat_adjusted]
    
    # Conditional branching and early break
    threshold_met = False
    cumulative = 0
    for idx, val in enumerate(indexed_vals):
        if val > 100:
            cumulative += math.log(val)
            if cumulative > 20:
                threshold_met = True
                break
    
    # Key transformation using dictionary and zip (required features)
    stats_map = {}
    for k, v in enumerate(indexed_vals):
        stats_map[f'entry_{k}'] = v * (0.9 + (k % 7) * 0.01)
    
    # Real computation chain
    base_score = 0
    keys_in_order = sorted(stats_map.keys(), key=lambda x: int(x.split('_')[1]))
    ordered_vals = [stats_map[k] for k in keys_in_order]
    
    # Use of zip to pair with offset
    paired_diffs = []
    for a, b in zip(ordered_vals, ordered_vals[1:]):
        paired_diffs.append(abs(a - b))
    
    # Final logic step
    if threshold_met:
        base_score = sum(paired_diffs) * 1.75
    else:
        base_score = sum(ordered_vals) * 0.45
    
    # Final answer depends on this
    final_weight = len([v for v in indexed_vals if v > 10]) * 2.3
    return base_score + final_weight

# Main execution block
sensor_data = [
    [12.1, 8.4, 15.6, 23.2],
    [7.8, 18.9, 9.3, 11.7],
    [25.4, 6.2, 13.8, 19.1],
    [10.5, 14.3, 8.7, 22.8]
]

calibration_matrix = [
    [1.05, 0.98, 1.02, 1.11],
    [0.94, 1.07, 0.96, 1.03],
    [1.12, 0.91, 1.04, 1.08],
    [0.99, 1.06, 0.93, 1.14]
]

# Irrelevant data structures (distractors)
dummy_logs = {'status': 'ok', 'count': 42, 'active': True}
feature_set = extract_features([row[0] for row in sensor_data])
entropy_val = compute_entropy([item for row in sensor_data for item in row])

# Unused transformation
distorted_data = dummy_transform([val for row in sensor_data for val in row])

# Critical statement
final_diagnostic = process_readings(sensor_data, calibration_matrix)

# Print result as required
print(f"Target result: {final_diagnostic}")