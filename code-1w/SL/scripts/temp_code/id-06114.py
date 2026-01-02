import math

# Simulated biomedical diagnostic system with noise and red herrings
def preprocess_signals(raw_signals):
    processed = {}
    for k, v in raw_signals.items():
        if len(v) > 0:
            smoothed = sum([x ** 0.5 for x in v if x > 0]) / len(v)
            processed[k] = round(smoothed * 1.7, 3)
    return processed

# Irrelevant helper - distractor
def compute_entropy(data):
    total = 0
    for x in data.values():
        if x > 0:
            total -= x * math.log(x)
    return round(total, 4)

# Unused function - dead code path
def normalize_dataset(dataset):
    mean_val = sum(dataset.values()) / len(dataset)
    return {k: (v - mean_val) for k, v in dataset.items()}

# Core logic disguised among distractions
def evaluate_risk_level(metric, config):
    baseline = config.get('baseline', 10)
    sensitivity = config.get('sensitivity', 0.85)
    adjusted = (metric - baseline) * sensitivity
    if adjusted > 5:
        return "CRITICAL"
    elif adjusted > 2:
        return "ELEVATED"
    else:
        return "NORMAL"

# Decoy analysis function that seems important but isn't used in final chain
def analyze_trend(values):
    diffs = [values[i+1] - values[i] for i in range(len(values)-1)]
    avg_change = sum(diffs) / len(diffs) if diffs else 0
    return 'increasing' if avg_change > 0 else 'decreasing'

# Key transformation with embedded bit manipulation distraction
def transform_indicators(data_dict):
    result = {}
    xor_key = 24
    for key, val in data_dict.items():
        # Bit manipulation red herring
        masked_val = int(val) ^ xor_key
        # Actual relevant computation
        scaled = val * 0.91
        result[key + '_adj'] = round(scaled, 3)
    # Return unmasked real values
    return {k: v for k, v in result.items() if 'adj' in k}

# Main aggregation function that combines multiple concepts
def aggregate_metrics(data_package, criteria):
    temp_store = {}
    
    # Step 1: Extract vital signs
    vitals = data_package.get('vitals', {})
    neuro = data_package.get('neuro', {})
    
    # Distractor: complex-looking but unused calculation
    decoy_score = 0
    for v in vitals.values():
        decoy_score += int(v) & 7  # bitwise AND red herring
    decoy_score = decoy_score << 2  # shift operation - irrelevant
    
    # Step 2: Apply transformations
    processed_vitals = transform_indicators(vitals)
    
    # Step 3: Compute weighted composites
    composite_a = sum(processed_vitals.values()) * 0.33
    composite_b = 0
    if neuro:
        # Real contribution
        raw_sum = sum(neuro.values())
        count = len(neuro)
        composite_b = raw_sum / count * 1.15
    
    # Step 4: Use dictionary operations meaningfully
    all_metrics = {**processed_vitals, 'composite_a': composite_a, 'composite_b': composite_b}
    
    # Step 5: Apply threshold logic (real decision path)
    threshold_a = criteria['t_a']
    threshold_b = criteria['t_b']
    
    flag_count = 0
    for metric_name, value in all_metrics.items():
        if 'adj' in metric_name and value > threshold_a:
            flag_count += 1
        elif 'composite' in metric_name and value > threshold_b:
            flag_count += 2
    
    # Step 6: Final diagnostic score
    base_diagnostic = flag_count * 17
    adjustment = len(all_metrics) % 5
    final_value = base_diagnostic + adjustment
    
    # Misleading intermediate printed (red herring output)
    print(f"Diagnostic trace: {decoy_score}, {flag_count}, {adjustment}")
    
    return int(final_value)

# Simulated input data
raw_biometric_data = {
    'ecg': [8, 12, 9],
    'resp': [15, 14, 16],
    'temp': [37, 38, 36]
}

# Irrelevant transformation result stored in unused var
dummy_features = preprocess_signals(raw_biometric_data)

# Real data flow begins here
health_data = {
    'vitals': {
        'heart_rate': 78,
        'spo2': 96,
        'bp_systolic': 124
    },
    'neuro': {
        'reflex_score': 8,
        'pupil_response': 10
    }
}

thresholds = {
    't_a': 70.0,
    't_b': 8.5
}

# Execution point of interest
final_diagnostic = aggregate_metrics(health_data, thresholds)
print(f"Result: {final_diagnostic}")