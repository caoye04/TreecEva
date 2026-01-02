import math

# Simulated sensor fusion system for environmental monitoring
def normalize_readings(readings):
    max_val = max(readings)
    min_val = min(readings)
    if max_val == min_val:
        return [0.5 for _ in readings]
    return [(x - min_val) / (max_val - min_val) for x in readings]

def calculate_entropy(data):
    total = sum(data)
    if total == 0:
        return 0.0
    probabilities = [x / total for x in data]
    entropy = -sum(p * math.log2(p) for p in probabilities if p > 0)
    return round(entropy, 6)

def detect_anomalies(values, threshold=0.8):
    # Irrelevant anomaly detection (dead path for main logic)
    anomalies = []
    for i, v in enumerate(values):
        if v > threshold:
            anomalies.append(i)
    return anomalies

def fuse_sensors(sensor_data):
    # Apply normalization
    normalized = {}
    for key, values in sensor_data.items():
        normalized[key] = normalize_readings(values)
    
    # Weighted fusion with arbitrary scaling
    fused = []
    keys = list(normalized.keys())
    weights = [0.4, 0.3, 0.3]  # Hardcoded for simplicity
    
    for i in range(len(normalized[keys[0]])):
        weighted_sum = sum(normalized[keys[j]][i] * weights[j] for j in range(len(keys)))
        fused.append(weighted_sum)
    
    return fused

def compute_reliability_index(fused_signal):
    # Compute signal stability index (distractor metric)
    diffs = [abs(fused_signal[i+1] - fused_signal[i]) for i in range(len(fused_signal)-1)]
    avg_change = sum(diffs) / len(diffs) if diffs else 0
    reliability = 1 / (1 + avg_change)
    return round(reliability, 6)

def derive_calibration_constant(signal):
    # Complex but irrelevant calibration logic
    base = sum(signal) / len(signal)
    fluctuation = math.sin(len(signal)) * math.cos(base)
    adjustment = abs(fluctuation) ** 0.5
    return (base * adjustment) % 0.997

def evaluate_performance(weights_dict, outcomes_list):
    # Core logic begins here
    flat_outcomes = [item for sublist in outcomes_list for item in sublist]  # Flatten
    entropy = calculate_entropy(flat_outcomes)
    
    # Simulate weighted scoring
    weighted_sum = 0.0
    for idx, (k, w) in enumerate(weights_dict.items()):
        if k in ['precision', 'accuracy', 'consistency']:
            # Only these keys matter
            outcome_idx = idx % len(flat_outcomes)
            weighted_sum += w * flat_outcomes[outcome_idx]
    
    # Final transformation
    score = (weighted_sum * 100) + (entropy * 10)
    return int(round(score))  # Deterministic integer result

# === MAIN EXECUTION ===
if __name__ == "__main__":
    # Real sensor inputs (simulated)
    sensor_inputs = {
        'temperature': [23.5, 24.1, 22.9, 25.0, 23.8],
        'humidity': [45, 47, 44, 50, 46],
        'pressure': [1013, 1015, 1012, 1016, 1014]
    }

    # Normalize each sensor stream
    processed = {}
    for sensor, data in sensor_inputs.items():
        processed[sensor] = normalize_readings(data)

    # Fused signal from multiple sensors
    fused_signal = fuse_sensors(sensor_inputs)

    # Distractor variables (not used in final answer)
    reliability_score = compute_reliability_index(fused_signal)
    calibration_const = derive_calibration_constant(fused_signal)
    anomalies_detected = detect_anomalies(fused_signal)
    signal_entropy = calculate_entropy(fused_signal)

    # Prepare evaluation metrics (only weights and outcomes affect final answer)
    metric_weights = {
        'precision': 0.4,
        'accuracy': 0.35,
        'consistency': 0.25,
        'timeliness': 0.1,  # Unused weight (red herring)
        'robustness': 0.05  # Unused weight (red herring)
    }

    raw_outcomes = [
        [0.88, 0.85, 0.91],  # precision-related
        [0.82, 0.87, 0.84],  # accuracy-related
        [0.79, 0.83],       # consistency-related
        [0.90, 0.88]        # timeliness/robustness (ignored)
    ]

    # Key statement
    final_score = evaluate_performance(metric_weights, raw_outcomes)

    print(f"Target result: {final_score}")