from collections import defaultdict, Counter

# Simulated sensor data with multiple channels
data_stream = [
    (1, [3, 1, 4, 1]), (2, [5, 9, 2, 6]), (3, [5, 3, 5, 8]), 
    (4, [9, 7, 9, 3]), (5, [2, 3, 8, 4]), (6, [6, 2, 6, 4]),
    (7, [1, 8, 2, 8]), (8, [4, 5, 9, 0]), (9, [4, 5, 2, 3])
]

# Irrelevant calibration coefficients (distractor)
calibration_factors = {1: 0.98, 2: 1.02, 3: 0.99, 4: 1.01, 5: 0.97}
offset_adjustments = defaultdict(lambda: 0.5)
for k in calibration_factors:
    offset_adjustments[k] += calibration_factors[k]

# Misleading noise filter that's not actually used (dead code path)
def legacy_filter(sequence):
    return [x for x in sequence if x % 2 == 1]

# Unused helper (red herring)
def compute_entropy(values):
    counts = Counter(values)
    total = len(values)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * (p ** 0.5)  # Not real entropy, but looks plausible
    return entropy

# Actual processing begins here
filtered_data = []
for index, readings in data_stream:
    if index % 2 == 1:  # Only odd-indexed packets are valid
        filtered_data.append((index, [x for x in readings if x > 2]))

# Signal normalization using dynamic baseline (relevant)
baseline_shift = sum([len(readings) for _, readings in filtered_data]) * 0.1
normalized_data = []
for idx, vals in filtered_data:
    shifted = [v - int(baseline_shift) + idx // 3 for v in vals]
    normalized_data.append(shifted)

# Flatten and group by magnitude bands (relevant)
flattened = [item for sublist in normalized_data for item in sublist]
magnitude_bins = defaultdict(int)
for val in flattened:
    if val < 0: band = 'negative'
    elif val < 5: band = 'low'
    elif val < 8: band = 'medium'
    else: band = 'high'
    magnitude_bins[band] += 1

# Decoy statistical summary (irrelevant computations)
summary_stats = {}
for key, count in magnitude_bins.items():
    summary_stats[f'{key}_weight'] = count * (0.8 if 'high' in key else 0.3)

# Real threshold logic (critical path)
threshold_map = {'negative': -1, 'low': 2, 'medium': 5, 'high': 7}
trigger_points = 0
for i, val in enumerate(flattened):
    expected_min = threshold_map['low']
    if i % 4 == 0:
        expected_min = threshold_map['medium']
    if val >= expected_min:
        trigger_points += 1

# Complex data transformation pipeline (relevant)
processed_data = []
for i, chunk in enumerate(normalized_data):
    transformed = []
    for j, num in enumerate(chunk):
        # Bit manipulation with modular arithmetic
        temp = (num ^ j) % 9
        if i > 0 and temp > threshold_map['low']:
            temp = (temp + i) // 2
        transformed.append(temp)
    processed_data.append(transformed)

# Secondary decoy analysis (misleading intermediate result)
anomaly_scores = []
for seq in processed_data:
    score = 0
    for x in seq:
        if x in (3, 5, 7):
            score += x * 0.7  # arbitrary weighting
    anomaly_scores.append(round(score, 2))

# Core diagnostic function with nested logic (key computation)
def analyze_signal(data_blocks, limits):
    total_score = 0
    peak_count = 0
    
    for block_idx, block in enumerate(data_blocks):
        block_max = max(block) if block else 0
        if block_max > limits['medium']:
            peak_count += 1
            
        for pos, val in enumerate(block):
            # Interleaved conditionals with short-circuit logic
            if block_idx % 2 == 0 and (val > limits['low'] or (pos > 0 and block[pos-1] < limits['negative'])):
                total_score += val * 2
            elif val > limits['medium'] and pos % 2 == 1:
                total_score += val
            
            # Hidden increment via bit counting (subtle but relevant)
            if val > 0:
                binary_ones = bin(val).count('1')
                if binary_ones >= 2:
                    total_score += 1

    # Cross-block dependency check
    if len(data_blocks) > 4 and peak_count >= 3:
        total_score += 10
    
    # Final adjustment based on distribution
    flat_vals = [v for b in data_blocks for v in b]
    high_vals = [v for v in flat_vals if v > limits['high']]
    if len(high_vals) >= 2:
        total_score += len(high_vals) * 3
    
    return int(total_score)

# Critical execution point
final_diagnostic = analyze_signal(processed_data, threshold_map)
print(f"Result: {final_diagnostic}")