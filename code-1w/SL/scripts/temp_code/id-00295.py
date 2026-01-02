import math

# System health monitoring simulation with noise filtering and diagnostic logic
def collect_sensor_data():
    raw_readings = [127, 255, 64, 89, 190, 31, 142, 73, 201, 55]
    timestamps = [163000, 163001, 163002, 163003, 163004, 163005, 163006, 163007, 163008, 163009]
    statuses = ['OK', 'ERROR', 'OK', 'OK', 'WARNING', 'OK', 'ERROR', 'OK', 'OK', 'WARNING']
    return list(zip(raw_readings, timestamps, statuses))


def filter_outliers(data):
    values = [x[0] for x in data]
    mean = sum(values) / len(values)
    variance = sum((x - mean) ** 2 for x in values) / len(values)
    stddev = math.sqrt(variance)
    threshold = 1.5 * stddev
    filtered = [entry for entry in data if abs(entry[0] - mean) <= threshold]
    
    # Irrelevant transformation
    temp_map = {i: val[0] for i, val in enumerate(filtered)}
    reversed_map = {v: k for k, v in temp_map.items()}
    
    # Distractor: unused computation
    anomaly_score = 0
    for val in values:
        if val > 200:
            anomaly_score += 1
        elif val < 50:
            anomaly_score += 0.5
    
    return filtered


def extract_metrics(clean_data):
    readings = [x[0] for x in clean_data]
    time_gaps = [clean_data[i+1][1] - clean_data[i][1] for i in range(len(clean_data)-1)]
    status_flags = [x[2] for x in clean_data]
    
    # Bitwise feature extraction (relevant)
    bit_pattern_sum = 0
    for val in readings:
        ones = bin(val).count('1')
        parity = bin(val).count('1') % 2
        bit_pattern_sum += ones * parity
    
    # Dead code path - never executed due to logic
    peak_magnitude = 0
    if False and len(readings) > 100:
        peak_magnitude = max(readings)
        normalization_factor = math.log(peak_magnitude)
        readings = [r / normalization_factor for r in readings]

    # Unused statistical distraction
    avg_gap = sum(time_gaps) / len(time_gaps) if time_gaps else 0
    gap_variance = sum((g - avg_gap)**2 for g in time_gaps) / len(time_gaps) if time_gaps else 0
    
    return {
        'readings': readings,
        'bit_score': bit_pattern_sum,
        'statuses': status_flags,
        'gaps': time_gaps
    }


def analyze_readings(metrics):
    readings = metrics['readings']
    bit_score = metrics['bit_score']
    statuses = metrics['statuses']
    
    # Real processing chain
    base_value = sum(r ** 0.5 for r in readings if r > 50)  # Only significant readings
    adjustment = 0
    
    # Conditional adjustments based on status distribution
    status_set = set(statuses)
    critical_count = statuses.count('ERROR')
    warning_count = statuses.count('WARNING')
    
    # Set operation influencing logic
    if 'ERROR' in status_set and 'WARNING' in status_set:
        adjustment -= 15
    if len(status_set) == 1:
        adjustment += 10
    
    # Secondary distractor block
    synthetic_curve = []
    for i in range(1, len(readings)):
        diff = readings[i] - readings[i-1]
        rate = diff / readings[i-1] if readings[i-1] != 0 else 0
        synthetic_curve.append(rate * 100)
    
    # Noise injection (unused)
    noise_floor = 0.05
    perturbed = [r + r * noise_floor for r in readings]
    
    # Key computation
    trend_factor = len([s for s in statuses if s == 'OK'])
    core_diagnostic = int(base_value + adjustment + bit_score)
    
    # Final red herring
    if len(synthetic_curve) > 5:
        smoothing_factor = sum(synthetic_curve) / len(synthetic_curve)
        core_diagnostic = int(core_diagnostic * (1 - smoothing_factor * 0.01))
    
    final_diagnostic = core_diagnostic + 100  # Final offset
    
    # Unused complex structure
    debug_snapshot = {
        'raw_sum': sum(readings),
        'entropy': -sum((r/sum(readings)) * math.log(r/sum(readings)) for r in readings if r > 0),
        'covariance_proxy': sum(readings[i] * statuses.count('OK') for i in range(len(readings)))
    }
    
    return final_diagnostic

# Main execution flow
data = collect_sensor_data()
filtered_data = filter_outliers(data)
filtered_metrics = extract_metrics(filtered_data)
final_diagnostic = analyze_readings(filtered_metrics)
print(f"Target result: {final_diagnostic}")