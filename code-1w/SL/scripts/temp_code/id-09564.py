import itertools

# Simulated sensor array diagnostics with red herrings
def analyze_sensor_array(raw_readings):
    baseline = sum(raw_readings) / len(raw_readings)
    deviations = [abs(x - baseline) for x in raw_readings]
    high_deviation_threshold = 0.5
    flagged = [i for i, d in enumerate(deviations) if d > high_deviation_threshold]
    
    # Irrelevant transformation (dead code path)
    temp_normalized = []
    for x in raw_readings:
        if x > 0:
            temp_normalized.append(1 / (1 + x))
        else:
            temp_normalized.append(0)
    
    # Unused statistical distraction
    mean_sq = sum(x**2 for x in raw_readings) / len(raw_readings)
    variance = mean_sq - baseline**2
    
    # Real processing: compute trend score (only this matters)
    trend_score = 0
    for i in range(1, len(raw_readings)):
        if raw_readings[i] > raw_readings[i-1]:
            trend_score += 1
        elif raw_readings[i] < raw_readings[i-1]:
            trend_score -= 0.5
    
    return trend_score

# Legacy system compatibility layer (distractor)
def legacy_calibrate(x):
    return (x * 0.97) + 0.3

# Unused signal smoothing (decoy function)
def smooth_signal(signal):
    from functools import reduce
    return reduce(lambda a, v: a[:-1] + [((a[-1] + v) / 2), (a[-1] + v) / 2], signal, [signal[0]])

# Core diagnostic logic
def evaluate_system_health(sensor_id, readings):
    # Irrelevant metadata processing
    checksum = sum(ord(c) for c in sensor_id) % 100
    
    # Fake anomaly detection
    anomalies = []
    for i, val in enumerate(readings):
        if abs(val - 0.5) < 0.01:
            anomalies.append(i)
    
    # Real work hidden among distractions
    filtered_readings = [x for x in readings if x > 0.1]
    if not filtered_readings:
        filtered_readings = [0.1]
    
    # Apply weighting via lambda and slicing (actual relevant use)
    weight_func = lambda i, x: 0.8 + 0.2 * (len(filtered_readings) - i) / len(filtered_readings)
    weighted_values = [
        weight_func(i, x) * x 
        for i, x in enumerate(filtered_readings)
    ]
    
    # Decoy data structure manipulation
    history_log = [{'step': j, 'val': readings[j]} for j in range(len(readings)) if j % 3 == 0]
    for entry in history_log:
        entry['flag'] = 'review' if entry['val'] > 0.7 else 'normal'
    
    return sum(weighted_values)

# Aggregation with itertools distraction
def aggregate_metrics(data_stream, importance_weights):
    # Complex-looking but irrelevant combinatorics
    permutations = list(itertools.permutations(importance_weights[:3]))
    cycle_stream = itertools.cycle([1.0])
    _ = [next(cycle_stream) for _ in range(5)]  # burn-in (distraction)
    
    # Real aggregation logic
    combined = 0.0
    for idx, (value, weight) in enumerate(zip(data_stream, importance_weights)):
        if idx % 2 == 0:
            combined += value * weight
        else:
            combined += value * (weight ** 0.5)
    
    # Spurious bit manipulation (no effect)
    int_part = int(combined)
    bit_fiddle = (int_part << 3) | (int_part >> 2)
    bit_fiddle ^= 0xFF
    bit_fiddle &= 0xFFFF
    
    # Final adjustment that actually matters
    if len(data_stream) > 4:
        combined *= 1.1
    
    return round(combined, 6)

# --- Main Execution ---
if __name__ == '__main__':
    # Simulated input data
    sensor_ids = ['SNSR-A7', 'SNSR-B2', 'SNSR-C9']
    all_readings = [
        [0.12, 0.15, 0.23, 0.35, 0.41, 0.48],
        [0.08, 0.11, 0.19, 0.25],
        [0.14, 0.22, 0.31, 0.42, 0.55]
    ]
    
    # Distractor: unused matrix operation
    correlation_matrix = [
        [sum(a*b for a,b in zip(all_readings[i], all_readings[j])) for j in range(3)]
        for i in range(3)
    ]
    
    # Real pipeline
    trends = [analyze_sensor_array(reads) for reads in all_readings]
    health_scores = [
        evaluate_system_health(sid, reads) 
        for sid, reads in zip(sensor_ids, all_readings)
    ]
    
    # Weight configuration (some irrelevant entries)
    config_weights = [0.8, 1.2, 0.9, 1.5, 1.1, 0.7]  # last two will be sliced
    active_weights = config_weights[:len(health_scores)]  # slicing use
    
    # Inject more noise
    temp_cache = {f'key_{i}': i**3 for i in range(10)}
    cleanup = [temp_cache.pop(f'key_{i}') for i in range(0, 10, 2)]
    
    # Critical execution point
    final_diagnostic = aggregate_metrics(health_scores, active_weights)
    
    # Output result
    print(f"Target result: {final_diagnostic}")