def analyze_system_load(usage_data, threshold=75):
    high_load_periods = [u for u in usage_data if u > threshold]
    normal_load_periods = [u for u in usage_data if u <= threshold]
    load_ratio = len(high_load_periods) / len(usage_data) if usage_data else 0
    return load_ratio * 100


def calculate_entropy(values):
    from math import log2
    total = sum(values)
    probabilities = [(v / total) for v in values if v > 0]
    entropy = -sum(p * log2(p) for p in probabilities)
    return entropy

# Irrelevant utility function (decoy)
def format_timestamps(ts_list):
    formatted = []
    for ts in ts_list:
        hours, rem = divmod(ts, 3600)
        minutes, sec = divmod(rem, 60)
        formatted.append(f'{hours:02}:{minutes:02}:{sec:02}')
    return formatted

# Misleading data structure
temporal_patterns = {
    'morning_peak': [60, 70, 85, 90, 80],
    'afternoon_plateau': [75, 74, 76, 75, 77],
    'night_dip': [30, 25, 20, 35, 40]
}

usage_log = [88, 76, 45, 92, 67, 81, 54, 95, 70, 83]
baseline_ref = 75

# Simulated network packet sizes (irrelevant)
packet_sizes = [128, 256, 512, 64, 1024, 256, 128]
avg_packet_size = sum(packet_sizes) / len(packet_sizes)
size_variance = sum((p - avg_packet_size) ** 2 for p in packet_sizes) / len(packet_sizes)

# Dummy transformation (dead code path)
transformed_log = []
for val in usage_log:
    if val > 80:
        transformed_log.append(val * 0.9)
    elif val < 60:
        transformed_log.append(val * 1.1)
    else:
        transformed_log.append(val)

# Set operations (required Python feature)
unique_usage = set(usage_log)
above_baseline = {u for u in unique_usage if u > baseline_ref}
below_or_equal = {u for u in unique_usage if u <= baseline_ref}
symmetric_diff = above_baseline.symmetric_difference(below_or_equal)
common_with_temporal = above_baseline.intersection(set(temporal_patterns['morning_peak']))

# Red herring calculation with no impact
phantom_metric = len(symmetric_diff) * max(above_baseline) // (min(below_or_equal) + 1)

# Core logic disguised among distractors
def compute_stability_index(data, ref):
    deviations = [abs(x - ref) for x in data]
    mean_dev = sum(deviations) / len(deviations)
    stability = 100 - (mean_dev * 0.8)
    return round(stability, 2)

stability = compute_stability_index(usage_log, baseline_ref)

# Another decoy function that is never called
def predict_failure_risk(score, history):
    risk_levels = ['low', 'medium', 'high']
    if score < 40:
        return risk_levels[2]
    elif score < 70:
        return risk_levels[1]
    else:
        return risk_levels[0]

# Critical data structures for evaluation
metrics = {
    'load_ratio': analyze_system_load(usage_log, baseline_ref),
    'entropy': calculate_entropy(usage_log),
    'stability': stability,
    'peak_count': len([x for x in usage_log if x > 90]),
    'utilization_rate': len([x for x in usage_log if x >= 70]) / len(usage_log)
}

baseline = {
    'load_ratio': 20.0,
    'entropy': 2.8,
    'stability': 85.0,
    'peak_count': 1,
    'utilization_rate': 0.6
}

# Main evaluation logic buried in complexity
def evaluate_performance(met, base):
    weights = {
        'load_ratio': -0.3,   # Negative impact
        'entropy': 0.2,
        'stability': 0.4,
        'peak_count': -0.25,
        'utilization_rate': 0.15
    }
    
    # Normalize differences
    normalized_scores = []
    for key in met:
        if key == 'peak_count':
            diff = base[key] - met[key]  # Inverted logic
        elif key == 'load_ratio':
            diff = base[key] - met[key] if met[key] > base[key] else met[key] - base[key]
        else:
            diff = met[key] - base[key]
        
        # Artificial scaling
        if key in ['entropy', 'stability']:
            diff *= 1.2
        
        normalized_scores.append(diff * weights[key])
    
    # Accumulate final score
    raw_score = sum(normalized_scores)
    
    # Apply non-linear transformation (critical step)
    adjusted_score = (raw_score * 10) + 50
    
    # Clamp to realistic range
    final = max(0, min(100, adjusted_score))
    
    # Distractor: unused transformation
    smoothed = round(final * 0.95, 1)
    ceiling_bump = int(final) + (1 if final % 1 > 0.7 else 0)
    
    return final

# Execution point of interest
final_score = evaluate_performance(metrics, baseline)

# Output requirement
print(f"Target result: {final_score}")