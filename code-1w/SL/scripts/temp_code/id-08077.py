def analyze_vital(vital, baseline):
    if len(vital) == 0:
        return 0
    avg = sum(vital) / len(vital)
    deviation = abs(avg - baseline)
    adjusted_score = (deviation * 1.5) // 1
    return int(adjusted_score)


def compute_thermal_load(readings):
    total_load = 0
    for r in readings:
        if r > 40:
            total_load += r ** 0.5
    return total_load  # distractor: not used in final result


def filter_outliers(data, limit=3):
    sorted_data = sorted(data)
    return sorted_data[limit:-limit] if len(sorted_data) > 2 * limit else sorted_data


def generate_summary(indices):
    cumulative = 0
    for i in indices:
        cumulative = (cumulative * 2) + (i % 7)
    return cumulative  # red herring variable


def process_metrics(data, config):
    # Extract relevant streams
    heart_rate = data['heart_rate']
    oxygen_levels = data['oxygen']
    neural_activity = data['neural']

    # Irrelevant preprocessing (distractor)
    normalized_o2 = [x / 100.0 for x in oxygen_levels]
    smoothed_neural = [n for n in neural_activity if n > 50]
    spike_count = len([n for n in neural_activity if n > 120])

    # Actual key computation path
    baseline_hr = config['hr_baseline']
    tolerance = config['tolerance_margin']

    hr_stat = analyze_vital(heart_rate, baseline_hr)
    
    # Bit manipulation for system health hash (decoy)
    health_hash = 0
    for val in oxygen_levels[:5]:
        health_hash ^= int(val) & 255
        health_hash = (health_hash << 1) | (health_hash >> 7)
    
    # Real diagnostic logic
    threshold_map = {k: v * 1.1 for k, v in config.items()}
    drift = abs(hr_stat - tolerance)

    # Set operation to simulate sensor consensus (actual use)
    high_readings = set(heart_rate)
    critical_zone = set(range(100, 150))
    overlap_count = len(high_readings & critical_zone)

    # Slice-based trend analysis
    recent_trend = heart_rate[-6:]
    rising_pattern = all(recent_trend[i] <= recent_trend[i+1] for i in range(len(recent_trend)-1))

    # Core formula
    base_diagnostic = hr_stat * 3.7
    if overlap_count > 2 and rising_pattern:
        base_diagnostic *= 1.8
    
    secondary_factor = len(smoothed_neural) % 5
    final_diagnostic = int(base_diagnostic + secondary_factor - drift)

    # Dead code path (never executed due to fixed condition)
    emergency_override = False
    if spike_count > 1000:  # Impossible by input design
        emergency_override = True
        final_diagnostic = -999

    return final_diagnostic

# Simulated patient data (real input)
health_data = {
    'heart_rate': [72, 75, 77, 80, 85, 88, 90, 92, 95, 98, 100, 102, 105, 108, 110],
    'oxygen': [96, 97, 98, 95, 97, 99, 98, 96, 97, 95],
    'neural': [45, 55, 60, 125, 48, 130, 58, 62, 135, 65]
}

thresholds = {
    'hr_baseline': 75,
    'tolerance_margin': 15,
    'o2_threshold': 90,
    'neural_floor': 50
}

# Unused auxiliary data (distractor)
diagnostic_log = [
    {'time': '00:00', 'code': 200},
    {'time': '00:05', 'code': 201},
    {'time': '00:10', 'code': 404}
]

buffer_cache = list(range(50, 60))
circular_shift = buffer_cache[-3:] + buffer_cache[:-3]

# Key execution point
temp_debug = compute_thermal_load([35, 38, 42, 45, 50])
summary_code = generate_summary([1, 2, 3, 5, 8, 13])

final_diagnostic = process_metrics(health_data, thresholds)
print(f"Result: {final_diagnostic}")