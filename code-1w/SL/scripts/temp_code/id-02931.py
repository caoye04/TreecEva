def transform_sequence(seq, factor):
    """Irrelevant transformation function (dead code path)"""
    return [x * factor + 2 for x in seq if x % 3 != 0]

# Sensor calibration constants (some are decoys)
calibration_ref = 0.87
offset_pad = 5
scaling_base = 1.03
unused_constant = 999  # No impact on result

# Simulated diagnostic thresholds by zone
threshold_map = {
    'core': 74.5,
    'peripheral': 62.1,
    'auxiliary': 58.3,
    'buffer': 45.7
}

# Raw sensor readings from four zones (indexed by name)
sensor_data = {
    'core': [70, 73, 75, 77, 72],
    'peripheral': [60, 63, 61, 64, 59],
    'auxiliary': [55, 59, 57, 60, 58],
    'buffer': [42, 46, 44, 48, 43]
}

# Misleading statistical aggregation (not used in final logic)
shadow_stats = {}
for zone, readings in sensor_data.items():
    avg = sum(readings) / len(readings)
    variance = sum((x - avg) ** 2 for x in readings) / len(readings)
    shadow_stats[zone] = round(variance, 2)

# Real processing begins: filter and scale relevant data
processed_data = {}
for label, values in sensor_data.items():
    filtered = [v for v in values if v > threshold_map[label] - 10]  # Pre-filter
    scaled = [v * calibration_ref for v in filtered]
    processed_data[label] = scaled[:3]  # Take only first three after scaling

# Extraneous set operation with no downstream use
duplicate_check = set()
for arr in processed_data.values():
    for val in arr:
        if val in duplicate_check:
            pass  # Dead logic branch
        duplicate_check.add(round(val))

# Auxiliary recursive smoothing function
def smooth_recursive(seq, depth=0):
    if depth >= 2 or len(seq) < 2:
        return seq
    smoothed = [(seq[i] + seq[i+1]) / 2 for i in range(len(seq)-1)]
    return smooth_recursive(smoothed, depth + 1)

# Apply smoothing only to core data (partial usage)
if 'core' in processed_data:
    processed_data['core'] = smooth_recursive(processed_data['core'])

# Decoy function that calculates entropy but is never called
def calculate_entropy(values):
    from math import log2
    total = sum(values)
    probs = [v / total for v in values]
    return -sum(p * log2(p) for p in probs if p > 0)

# Main analysis function combining boolean logic, comparisons, and dictionary lookups
def analyze_readings(data, limits):
    score = 0
    penalty_adjust = 0
    
    # Complex conditional scoring across zones
    for zone, samples in data.items():
        limit = limits[zone]
        high_count = sum(1 for s in samples if s > limit)
        low_count = sum(1 for s in samples if s < limit - 5)
        
        if high_count >= 2:
            if zone == 'core':
                score += 17
            elif zone == 'peripheral':
                score += 12
            else:
                score += 8
        
        if low_count >= 1:
            penalty_adjust -= 3
        
        # Bitwise manipulation red herring
        temp_flag = high_count & 1
        if temp_flag:
            penalty_adjust += 1  # Minor misleading adjustment
    
    # Final nonlinear transformation
    base_result = (score ** 1.5) - abs(penalty_adjust * 7)
    
    # Slicing-based correction using auxiliary data (only first two chars matter)
    zone_key = ''.join(sorted(limits.keys()))[:2]
    if zone_key == 'au':
        base_result -= 10
    
    # Critical result
    final_value = int(round(base_result))
    
    # Dead code: unused derived metrics
    consistency_metric = len([z for z in data.keys() if z in ['core', 'auxiliary']])
    debug_snapshot = {k: len(v) for k, v in data.items()}
    
    return final_value

# Execute critical statement
final_diagnostic = analyze_readings(processed_data, threshold_map)
print(f"Target result: {final_diagnostic}")