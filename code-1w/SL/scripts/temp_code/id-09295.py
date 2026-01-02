from collections import defaultdict, Counter
import itertools

# Simulate sensor readings with noise and validity flags
def fetch_sensor_data():
    raw_readings = [15, 18, 15, 22, 18, 25, 30, 25, 22, 15]
    timestamps = list(range(10))
    validity = [True, True, True, False, True, True, False, True, True, True]
    return list(zip(timestamps, raw_readings, validity))

# Filter and normalize valid sensor data
def preprocess_data(raw_data):
    valid_readings = []
    outlier_count = 0
    temp_sum = 0
    stats_log = defaultdict(int)
    
    for ts, val, valid in raw_data:
        if not valid:
            stats_log['invalid'] += 1
            continue
        if val < 16 or val > 28:
            outlier_count += 1
            stats_log['outliers'] += 1
            continue
        temp_sum += val
        valid_readings.append(val)
        
    avg_valid = temp_sum / len(valid_readings) if valid_readings else 0
    normalized = [v - avg_valid for v in valid_readings]
    
    # Dummy tracking variables (distraction)
    magnitude = sum([abs(x) for x in normalized])
    peak_deviation = max(normalized) - min(normalized) if normalized else 0
    
    return {
        'values': valid_readings,
        'normalized': normalized,
        'stats': dict(stats_log),
        'avg_base': avg_valid
    }

# Apply weighted temporal smoothing
def smooth_sequence(data_obj):
    sequence = data_obj['normalized']
    smoothed = []
    weights = [0.25, 0.5, 0.25]
    
    if len(sequence) < 3:
        return sequence[:]
    
    # Misleading convolution setup (not fully used)
    padded = [sequence[0]] + sequence + [sequence[-1]]
    convolution_trace = []
    
    for i in range(1, len(sequence) + 1):
        window = padded[i-1:i+2]
        weighted = sum(w * x for w, x in zip(weights, window))
        smoothed.append(weighted)
        convolution_trace.append((window, weighted))  # Unused
    
    # Additional irrelevant transformation
    transformed_meta = {"length": len(smoothed), "version": "1.1"}
    
    data_obj['smoothed_dev'] = smoothed
    return data_obj

# Compute final diagnostic score based on pattern consistency
def compute_pattern_risk(smoothed_deviations):
    risk = 0
    zero_crossings = 0
    prev = 0
    
    for dev in smoothed_deviations:
        if (prev <= 0 and dev > 0) or (prev >= 0 and dev < 0):
            zero_crossings += 1
        prev = dev
    
    # Count repeating patterns using sliding windows
    pattern_counter = Counter()
    for i in range(len(smoothed_deviations) - 2):
        key = tuple(round(x, 2) for x in smoothed_deviations[i:i+3])
        pattern_counter[key] += 1
    
    repeated_patterns = sum(1 for cnt in pattern_counter.values() if cnt > 1)
    base_risk = zero_crossings * 3 + repeated_patterns * 2
    
    # Dummy secondary analysis (irrelevant to final result)
    entropy_proxy = 0
    for cnt in pattern_counter.values():
        if cnt > 1:
            entropy_proxy += 1
    
    return base_risk

# Final scoring with calibration offset
def compute_final_score(processed_data):
    deviations = processed_data.get('smoothed_dev', [])
    base_risk = compute_pattern_risk(deviations)
    baseline_ref = processed_data['avg_base']
    
    # Calibration factors (some unused)
    factor_a = 1.8
    factor_b = 0.95
    adjustment = (factor_a - factor_b) * 2  # Distractor
    
    # Critical computation
    signal_energy = sum(x**2 for x in deviations) if deviations else 0
    stability_index = 100 - base_risk - int(signal_energy)
    
    # Secondary metrics (unused in final score)
    coherence = len(deviations) / (base_risk + 1) if base_risk else 0
    fluctuation_rate = base_risk / len(deviations) if deviations else 0
    
    final_score = int(stability_index + 10)  # Final deterministic result
    
    # Dead code branch (never executed but adds cognitive load)
    if False:
        fallback = sum(processed_data['values']) // len(processed_data['values'])
        final_score = fallback * 2
    
    return final_score

# Execution pipeline
if __name__ == '__main__':
    raw_data = fetch_sensor_data()
    processed_data = preprocess_data(raw_data)
    enhanced_data = smooth_sequence(processed_data)
    final_score = compute_final_score(enhanced_data)
    print(f"Result: {final_score}")