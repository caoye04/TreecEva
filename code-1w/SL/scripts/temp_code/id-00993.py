from collections import defaultdict
import math

# Simulated sensor data processing system with performance evaluation

def preprocess_data(raw_input):
    processed = {}
    noise_floor = 0.02
    for k, v in raw_input.items():
        if isinstance(v, list) and len(v) > 0:
            cleaned = [x for x in v if abs(x) > noise_floor]
            if cleaned:
                processed[k] = sum(cleaned) / len(cleaned)
            else:
                processed[k] = 0.0
    return processed

def calculate_entropy(values):
    # Irrelevant helper function - not used in final computation path
    value_counts = defaultdict(int)
    for v in values:
        value_counts[v] += 1
    entropy = 0.0
    total = len(values)
    for count in value_counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return entropy

def filter_outliers(data_dict, threshold=2.5):
    # Dead code path - never called
    filtered = {}
    for k, v in data_dict.items():
        if isinstance(v, float) and v < threshold:
            filtered[k] = v
    return filtered

def accumulate_metrics(base_metrics, adjustments):
    # Merges metrics using weighted combination (red herring: complex but unused)
    result = defaultdict(float)
    for key in set(base_metrics.keys()) | set(adjustments.keys()):
        base_val = base_metrics.get(key, 0.0)
        adj_val = adjustments.get(key, 0.0)
        result[key] = base_val * 0.7 + adj_val * 0.3
    return dict(result)

def validate_calibration(calib_data):
    # Unused validation function - distractor
    if not calib_data:
        return False
    return all(isinstance(x, (int, float)) and x >= 0 for x in calib_data.values())

def compute_derived_features(processed):
    features = {}
    # Real transformation chain
    features['amplitude_ratio'] = abs(processed.get('sensor_a', 0) / (processed.get('sensor_b', 1) + 1e-6))
    features['phase_shift'] = processed.get('sensor_c', 0) ** 2
    features['baseline_drift'] = max(processed.values()) - min(processed.values()) if processed else 0
    return features

def apply_corrections(feature_set, config):
    corrected = {}
    correction_factor = config.get('sensitivity', 1.0)
    for k, v in feature_set.items():
        if k == 'amplitude_ratio':
            corrected[k] = v * correction_factor
        elif k == 'phase_shift':
            corrected[k] = math.sqrt(abs(v) + 1e-6)
        else:
            corrected[k] = v
    return corrected

def evaluate_performance(weights, results):
    score = 0.0
    for metric, weight in weights.items():
        raw_value = results.get(metric, 0)
        # Key logic step: normalize and accumulate weighted scores
        normalized = min(raw_value / (max(1, abs(raw_value))), 1.0)  # Clamp to [-1,1] -> [0,1]
        score += weight * normalized
    return int(score * 1000) / 1000.0  # Round to 3 decimal places

# Main execution block
if __name__ == "__main__":
    
    # Simulated raw sensor readings (real input)
    raw_results = {
        'sensor_a': [0.12, 0.15, -0.03, 0.14],
        'sensor_b': [0.08, 0.09, 0.07],
        'sensor_c': [0.21, -0.18, 0.22],
        'aux_d': [0.01, -0.01, 0.02],  # Below noise floor -> ignored
        'status_codes': [200, 200, 404]  # Non-numeric, ignored
    }

    # Irrelevant auxiliary data (distractor)
    calibration_sequence = {'gain': 1.05, 'offset': 0.01, 'temp': 23}
    validation_thresholds = [0.1, 0.5, 1.0, 2.0]
    debug_trace = []

    # Preprocess raw data
    cleaned_data = preprocess_data(raw_results)
    
    # Extract derived features
    feature_map = compute_derived_features(cleaned_data)
    
    # Apply physical corrections
    system_config = {'sensitivity': 1.2}
    corrected_features = apply_corrections(feature_map, system_config)
    
    # Define weighting scheme for performance scoring
    metric_weights = {
        'amplitude_ratio': 0.4,
        'phase_shift': 0.35,
        'baseline_drift': 0.25
    }
    
    # UNUSED intermediate variables (red herrings)
    temp_analysis = {k: v*2 for k, v in corrected_features.items()}
    aggregation_log = []
    outlier_report = []
    
    # Critical statement: compute final performance score
    final_score = evaluate_performance(metric_weights, corrected_features)
    
    # Print target result
    print(f"Target result: {final_score}")