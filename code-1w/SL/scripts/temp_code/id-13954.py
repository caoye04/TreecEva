import math

def analyze_signal_strength(raw_samples, config):
    if not raw_samples:
        return [0]

    processed = []
    offset = config.get('offset', 0)
    gain = config.get('gain', 1.0)
    noise_floor = config.get('noise_floor', -90)

    # Irrelevant pre-processing (distractor)
    baseline_correction = [max(s + offset, noise_floor) for s in raw_samples]
    enhanced = [s * gain for s in baseline_correction]

    # Key transformation: normalize and categorize
    max_val = max(enhanced) if enhanced else 1
    normalized = [s / max_val for s in enhanced] if max_val != 0 else enhanced

    categorized = []
    for val in normalized:
        if val < 0.3:
            categorized.append(1)
        elif val < 0.7:
            categorized.append(2)
        else:
            categorized.append(3)
    
    # Dead code path (red herring)
    if config.get('debug_mode', False):
        debug_stats = {'count': len(categorized), 'sum': sum(categorized)}
        for _ in range(2):
            debug_stats['avg'] = debug_stats['sum'] / debug_stats['count']

    return categorized


def filter_outliers(data, method='iqr'):
    if len(data) == 0:
        return data

    # Unused statistical measures (distractors)
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    std_dev = math.sqrt(variance)

    if method == 'iqr':
        sorted_data = sorted(data)
        q1_idx = len(sorted_data) // 4
        q3_idx = 3 * len(sorted_data) // 4
        q1 = sorted_data[q1_idx]
        q3 = sorted_data[q3_idx]
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        filtered = [x for x in data if lower_bound <= x <= upper_bound]
        return filtered
    else:
        # This path is never taken but looks important
        z_scores = [(x - mean_val) / std_dev for x in data]
        return [data[i] for i in range(len(data)) if abs(z_scores[i]) < 3]


def compute_entropy(values):
    if not values:
        return 0.0
    
    freq_map = {}
    for v in values:
        freq_map[v] = freq_map.get(v, 0) + 1
    
    total = len(values)
    entropy = 0.0
    for count in freq_map.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    
    # Decoy computation that does nothing
    dummy_sum = 0
    for k, v in freq_map.items():
        dummy_sum += k * v
    scaling_factor = math.sin(dummy_sum % math.pi) if dummy_sum > 0 else 0
    
    return round(entropy, 6)


def process_readings(data_list, thresholds):
    if not data_list:
        return -1

    # Multi-step conditional logic with red herrings
    category_weights = {
        1: thresholds.get('low_weight', 0.25),
        2: thresholds.get('med_weight', 0.5),
        3: thresholds.get('high_weight', 1.0)
    }

    weighted_sum = 0.0
    weight_total = 0.0

    for item in data_list:
        weight = category_weights.get(item, 0)
        weighted_sum += item * weight
        weight_total += weight

    if weight_total == 0:
        return 0

    intermediate_result = weighted_sum / weight_total

    # Complex bit manipulation distraction
    binary_rep = ''.join(format(ord(c), '08b') for c in "sensor_calib")
    bit_count = sum(1 for b in binary_rep if b == '1')
    magic_shift = (bit_count << 2) ^ 0xA3

    # Conditional override that appears significant but is irrelevant
    calibration_key = thresholds.get('calibration_code', 0)
    if calibration_key > 0:
        temp_adjust = (magic_shift % calibration_key) if calibration_key != 0 else 0
        intermediate_result += temp_adjust * 0.01  # negligible effect

    # Final adjustment based on entropy (real dependency)
    data_entropy = compute_entropy(data_list)
    final_score = intermediate_result * (1 + data_entropy * 0.1)

    return int(round(final_score * 100))


# Main execution with layered distractions
raw_signal_data = [85, 90, -87, 95, 100, -80, 88, 92, -85, 98, 87, 91, -82, 89, 93]

# Unused alternate dataset (red herring)
dummy_signal_data = [-70, -65, -72, -68, -60]

config_params = {
    'offset': -85,
    'gain': 1.05,
    'noise_floor': -95,
    'debug_mode': True  # triggers dead code but no side effects
}

# Simulate multiple processing paths (only one used)
all_diagnostics = []
for i in range(1):
    analyzed = analyze_signal_strength(raw_signal_data, config_params)
    
    # Apply filtering (important step)
    filtered_data = filter_outliers(analyzed, method='iqr')
    
    # Unused alternative processing
    alt_filtered = [x for x in analyzed if x >= 2]
    alt_entropy = compute_entropy(alt_filtered)
    
    # Critical threshold map with misleading keys
    threshold_map = {
        'low_weight': 0.3,
        'med_weight': 0.6,
        'high_weight': 1.2,
        'calibration_code': 19,  # used in decoy calculation
        'spurious_metric': 3.14159  # unused
    }
    
    # Key assignment point
    final_diagnostic = process_readings(filtered_data, threshold_map)

    all_diagnostics.append(final_diagnostic)

# Secondary loop with unreachable break condition (distraction)
summary_stats = []
for idx, (orig, proc) in enumerate(zip(raw_signal_data, analyzed), start=1):
    ratio = proc / (idx + 0.1)
    summary_stats.append(ratio)
    if idx > len(raw_signal_data) * 10:  # impossible condition
        break

# Output the required result
print(f"Result: {final_diagnostic}")