def analyze_efficiency(data, thresholds):
    efficiency_list = []
    for i, value in enumerate(data):
        if value > thresholds[i % len(thresholds)]:
            efficiency_list.append(value * 0.85)
        else:
            efficiency_list.append(value * 1.15)
    return efficiency_list

# Irrelevant helper function (decoy)
def compute_safety_margin(x, y):
    temp = x ** 2 + y ** 2
    return temp // 7 if temp > 100 else temp * 3

# Another decoy function with dead logic
def validate_calibration(values):
    calibrated = [v * 1.05 for v in values]
    checksum = sum(calibrated) % 17
    if checksum < 5:
        return [c - 0.5 for c in calibrated]
    elif checksum > 10:  # This path is never taken due to fixed input
        return [c + 0.2 for c in calibrated]
    return calibrated

# Misleading intermediate transformation
def transform_features(features):
    encoded = []
    for idx, feat in enumerate(features):
        if idx % 2 == 0:
            encoded.append(feat * 2 + 3)
        else:
            encoded.append(feat * 3 - 1)
    return encoded

# Core computation chain
def normalize_vector(v):
    magnitude = sum(x ** 2 for x in v) ** 0.5
    return [x / magnitude for x in v] if magnitude != 0 else v

def weighted_sum(a, b):
    return sum(x * y for x, y in zip(a, b))

def evaluate_performance(metrics, weights):
    normalized_metrics = normalize_vector(metrics)
    base_score = weighted_sum(normalized_metrics, weights)
    adjustment = 0.0
    for i, (m, w) in enumerate(zip(metrics, weights)):
        if i % 3 == 0 and m > 50:
            adjustment += w * 0.25
        elif i % 3 == 1 and m < 30:
            adjustment -= w * 0.15
    return int(base_score * 100 + adjustment * 50)

# Main execution block
if __name__ == "__main__":
    # Input data
    raw_data = [45, 67, 23, 89, 12, 78]
    config_thresholds = [50, 30, 70]
    feature_set = [10, 20, 30, 40]
    
    # Dead code path — unused result
    safety_val = compute_safety_margin(12, 8)
    
    # Distractor: irrelevant transformation
    transformed_features = transform_features(feature_set)
    recalibrated = validate_calibration(transformed_features)
    
    # Real processing begins
    processed_efficiency = analyze_efficiency(raw_data, config_thresholds)
    
    # Simulate noise filtering
    filtered = []
    for val in processed_efficiency:
        if val > 20 and val < 90:
            filtered.append(val + 5.5)
        else:
            filtered.append(val - 2.3)
    
    # Prepare metrics and weights
    metrics = [int(x) for x in filtered]  # Convert to integers
    weights = [0.1, 0.3, 0.15, 0.25, 0.05, 0.15]
    
    # Introduce red herring variable
    shadow_copy = [m * 0.9 for m in metrics]
    dummy_result = weighted_sum(shadow_copy, weights)
    
    # Key statement
    final_score = evaluate_performance(metrics, weights)
    
    # Output target result
    print(f"Result: {final_score}")