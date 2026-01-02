import math

# Simulated sensor fusion system for environmental monitoring

def normalize_readings(readings):
    max_val = max(readings)
    min_val = min(readings)
    if max_val == min_val:
        return [0.5 for _ in readings]
    return [(x - min_val) / (max_val - min_val) for x in readings]

def calculate_entropy(data):
    """Irrelevant function - simulates information-theoretic analysis"""
    total = sum(data)
    if total == 0:
        return 0.0
    probabilities = [x / total for x in data]
    return -sum(p * math.log2(p) for p in probabilities if p > 0)

def apply_calibration(signal, factor=1.0, offset=0.0):
    # Distractor: complex-looking calibration with unused parameters
    calibrated = []
    for i, x in enumerate(signal):
        adjusted = x * factor + offset
        noise_floor = 0.01 * math.sin(i * 0.5)
        adjusted += noise_floor  # Irrelevant noise addition
        calibrated.append(adjusted)
    return calibrated

def rolling_average(data, window=3):
    # Dead code path - never actually used in final computation
    if len(data) < window:
        return data
    result = []
    for i in range(len(data)):
        start = max(0, i - window + 1)
        result.append(sum(data[start:i+1]) / (i - start + 1))
    return result

def detect_anomalies(threshold_map, values):
    # Misleading function that appears important but is not used in final logic
    anomalies = {}
    for key, threshold in threshold_map.items():
        if key < len(values) and values[key] > threshold:
            anomalies[key] = values[key]
    return anomalies

def compute_derivatives(series):
    # Unused mathematical transformation
    return [series[i+1] - series[i] for i in range(len(series)-1)] + [0]

def fuse_sensors(sources):
    # Complex-looking fusion with irrelevant operations
    fused = []
    weights = {k: 1/(v+1) for k, v in sources.items()}
    total_weight = sum(weights.values())
    for k, v in sources.items():
        contribution = v * (weights[k] / total_weight)
        fused.append(contribution * 0.9 + 0.1 * math.cos(v))  # Red herring calculation
    return fused

def evaluate_performance(weight_map, results):
    # Core logic buried among distractions
    base_scores = []
    for i, val in enumerate(results):
        weight_key = tuple(w for w in weight_map.keys() if w <= i+1)
        if weight_key:
            effective_weight = weight_map[max(weight_key)]
        else:
            effective_weight = 1.0
        score = val * effective_weight * (1 + 0.1 * math.log(i + 1))
        base_scores.append(score)
    
    # Real computation hidden in middle of irrelevant operations
    temp_offset = sum(math.sin(x) for x in base_scores[:3])  # Looks important, not used
    final_multiplier = 1.0
    for w in weight_map.values():
        final_multiplier *= (1 + w / 10)  # This actually affects result
    
    aggregate = sum(base_scores) * final_multiplier
    
    # Decoy final processing steps
    entropy_check = calculate_entropy(base_scores)  # Computed but ignored
    normalized_aggregate = aggregate / (1 + abs(entropy_check))
    
    # Actual answer determined here
    final_score = int(round(normalized_aggregate))
    
    # Additional red herring variables
    diagnostic_codes = {i: hex(int(x)) for i, x in enumerate(base_scores)}
    consistency_ratio = len(diagnostic_codes) / (aggregate % 100 + 1)
    
    return final_score

# Main execution with extensive distractors
if __name__ == "__main__":
    # Real input data
    raw_sensor_data = [23.4, 45.1, 67.8, 12.5, 89.2, 34.0, 56.7]
    
    # Irrelevant preprocessing chain
    processed_signal = apply_calibration(raw_sensor_data, factor=1.05, offset=-0.5)
    filtered_data = normalize_readings(processed_signal)
    derivatives = compute_derivatives(filtered_data)
    
    # Fake multi-source fusion
    sensor_sources = {k: v for k, v in enumerate(filtered_data)}
    fused_output = fuse_sensors(sensor_sources)
    
    # Create misleading intermediate results
    anomaly_thresholds = {i: x * 0.8 for i, x in enumerate(filtered_data)}
    detected_issues = detect_anomalies(anomaly_thresholds, filtered_data)
    
    # Rolling statistics (unused)
    smoothed = rolling_average(fused_output, window=2)
    
    # ACTUAL RELEVANT DATA STRUCTURES
    metric_weights = {
        1: 0.8,
        3: 1.2,
        5: 1.5
    }
    
    raw_results = [x * 10 for x in filtered_data]  # Basis for real calculation
    
    # Key computation buried in noise
    final_score = evaluate_performance(metric_weights, raw_results)
    
    # Print required output
    print(f"Target result: {final_score}")