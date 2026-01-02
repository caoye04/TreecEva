import itertools

# System health monitoring simulation with diagnostic aggregation

def analyze_trend(samples, sensitivity):
    if len(samples) < 3:
        return 0
    trend = sum(samples[i] - samples[i-1] for i in range(1, len(samples)))
    return trend * sensitivity

def compute_entropy(data):
    # Irrelevant function - not used in main logic
    from math import log
    freq = {}
    for x in data:
        freq[x] = freq.get(x, 0) + 1
    total = len(data)
    entropy = -sum((count/total) * log(count/total) for count in freq.values())
    return round(entropy, 4)

def validate_bounds(value, lower, upper):
    # Dead code path - never called
    return lower <= value <= upper

def extract_features(signal):
    # Distractor transformation - unused
    features = []
    for i, s in enumerate(signal):
        if i % 3 == 0:
            features.append(s ** 0.5 if s > 0 else 0)
    return features

def aggregate_metrics(trends, config):
    base_score = 0
    modifiers = []
    
    for key, trend_val in trends.items():
        thresh_obj = config.get(key, {})
        critical = thresh_obj.get('critical', 100)
        warning = thresh_obj.get('warning', 50)
        
        if trend_val > critical:
            modifiers.append(3)
        elif trend_val > warning:
            modifiers.append(2)
        else:
            modifiers.append(1)
    
    # Real computation path
    base_multiplier = len([m for m in modifiers if m > 1])
    penalty_factor = sum(modifiers) / (len(modifiers) or 1)
    
    # Misleading intermediate: looks important but unused later
    decoy_score = base_score + (base_multiplier * 17) - (len(trends) % 4)
    
    # Actual result computation
    raw_aggregate = sum(trends.values())
    adjustment = penalty_factor * 0.75
    final_value = raw_aggregate * adjustment
    
    # Additional red herring variables
    temp_buffer = [x * 2 for x in trends.values() if x < 0]
    overflow_flag = len(temp_buffer) > 2
    checksum = sum(itertools.accumulate([len(config), int(adjustment)]))
    
    # Final diagnostic is only based on final_value rounded
    return int(round(final_value))

# Simulated sensor inputs
sensor_a = [10, 12, 15, 14, 18]
sensor_b = [100, 95, 90, 85, 80]
sensor_c = [5, 7, 10, 12]
sensor_d = [20, 20, 20, 20]

# Irrelevant preprocessing (distractor)
denoised_a = [x for x in sensor_a if x > 8]
smoothed_b = list(itertools.accumulate(sensor_b))[:4]

# Generate trend analyses (only these are used)
trend_data = {
    'temporal_flow': analyze_trend(sensor_a, 1.2),
    'degradation_rate': analyze_trend(sensor_b, -0.8),
    'growth_pattern': analyze_trend(sensor_c, 1.5),
    'stability_index': analyze_trend(sensor_d, 0.5)
}

# Threshold configuration map
threshold_map = {
    'temporal_flow': {'warning': 4.0, 'critical': 7.0},
    'degradation_rate': {'warning': -3.0, 'critical': -6.0},
    'growth_pattern': {'warning': 5.0, 'critical': 9.0},
    'stability_index': {'warning': 0.5, 'critical': 1.0}
}

# Unused diagnostic modes (dead code paths)
mode_flags = {
    'deep_analysis': False,
    'legacy_mode': True,
    'debug_trace': False
}

# Secondary irrelevant calculations
entropy_probe = compute_entropy([1, 2, 2, 3, 3, 3])
feature_dump = extract_features([8, 16, 24, 32])

# Core execution
baseline_metric = sum(trend_data.values()) / len(trend_data)
scaling_factor = 1.0 if baseline_metric > 0 else 0.5

# Key statement
final_diagnostic = aggregate_metrics(trend_data, threshold_map)

# Print required output
print(f"Result: {final_diagnostic}")