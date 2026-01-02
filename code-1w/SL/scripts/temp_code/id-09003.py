import math

def analyze_rhythm(signal):
    if not signal:
        return 0
    magnitude = sum([x ** 2 for x in signal])
    normalized = math.sqrt(magnitude) if magnitude else 0
    return normalized * (1 + (len(signal) > 5))

def evaluate_stability(readings):
    trend = [readings[i+1] - readings[i] for i in range(len(readings)-1)]
    oscillations = sum(1 for i in range(len(trend)-1) if trend[i] * trend[i+1] < 0)
    return oscillations >= 3

def compute_entropy(data):
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = -sum((count / total) * math.log2(count / total) for count in counts.values())
    return round(entropy, 4)

def extract_features(raw_data):
    features = {}
    features['peak'] = max(raw_data, default=0)
    features['trough'] = min(raw_data, default=0)
    features['span'] = features['peak'] - features['trough']
    features['density'] = len(raw_data) / (features['span'] + 1)
    features['complexity'] = compute_entropy([int(x) for x in raw_data])
    return features

def simulate_response(input_level):
    # Irrelevant simulation function (dead path)
    response_curve = []
    for t in range(5):
        response_curve.append(math.sin(t * input_level) * math.exp(-t * 0.3))
    return sum(response_curve)

def validate_consistency(metrics_dict):
    required_keys = {'peak', 'trough', 'span', 'density'}
    return required_keys.issubset(metrics_dict.keys()) and metrics_dict['span'] > 0

def process_metrics(signature, baseline):
    # Core logic begins
    feature_set = extract_features(signature)
    
    # Distractor: unused intermediate calculation
    decoy_analysis = [x * 1.75 for x in baseline if x > 0.5]
    temp_offset = sum(decoy_analysis) / (len(decoy_analysis) + 1) if decoy_analysis else 0.0
    
    rhythm_score = analyze_rhythm(signature)
    stable = evaluate_stability(baseline)
    
    # Conditional expression (required language feature)
    adjustment_factor = 1.25 if rhythm_score > 4.0 else 0.8
    
    # More distractors: irrelevant transformations
    shadow_map = {i: val * adjustment_factor for i, val in enumerate(baseline)}
    aggregate_shadow = sum(shadow_map.values())
    dummy_threshold = aggregate_shadow / (len(shadow_map) or 1)
    
    # Real computation path
    if validate_consistency(feature_set) and feature_set['density'] > 0.8:
        base_metric = feature_set['peak'] * feature_set['complexity']
        # Another conditional expression
        penalty = 10 if not stable else (5 if rhythm_score < 2.0 else 0)
        adjusted_metric = (base_metric * adjustment_factor) - penalty
        secondary_index = abs(feature_set['trough']) + rhythm_score
        final_diagnostic = int(adjusted_metric + secondary_index)
    else:
        final_diagnostic = -1  # fallback (not taken)
    
    # Dead code path (distractor)
    if temp_offset > 100:
        mirror_trace = [math.cos(x) for x in shadow_map.values()]
        final_diagnostic -= sum(mirror_trace)
    
    return final_diagnostic

# Main execution
health_signature = [0.8, 1.2, 3.1, 2.9, 4.5, 4.6, 4.4, 3.0]
baseline_readings = [0.4, 0.6, 0.5, 0.7, 0.6, 0.8, 0.9, 0.7, 0.6]

# Unused variables (red herrings)
diagnostic_log = set()
reference_archive = {'version': '2.1', 'calibrated': True}
calibration_matrix = [[1, 0], [0, 1]]

# Key statement
final_diagnostic = process_metrics(health_signature, baseline_readings)

print(f"Result: {final_diagnostic}")