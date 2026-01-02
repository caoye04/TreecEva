from collections import defaultdict

# Simulate sensor fusion system with noisy inputs and weighted evaluation
def evaluate_performance(weights, results):
    processed = defaultdict(float)
    temp_buffer = [0] * len(results)
    noise_floor = 0.02
    calibration_offset = 0.1

    # Irrelevant pre-scan (dead code path)
    if len(results) < 5:
        temp_buffer[0] = -999  # Unused

    # Actual processing begins
    total_weight = sum(weights.values())
    normalized_weights = {k: v / total_weight for k, v in weights.items()}

    # Simulate intermediate signal correction (partially relevant)
    corrected_results = {}
    for sensor, value in results.items():
        if value < 0:
            value = abs(value)
        corrected_results[sensor] = value + calibration_offset  # Minor fix

    # Weighted scoring logic (core)
    raw_score = 0.0
    for key in weights:
        if key in corrected_results:
            contribution = normalized_weights[key] * corrected_results[key]
            raw_score += contribution

    # Secondary adjustment using set operations (semi-relevant)
    valid_sensors = set(corrected_results.keys())
    expected_sensors = {'temp', 'pressure', 'flow', 'humidity'}
    missing_count = len(expected_sensors - valid_sensors)
    redundancy_bonus = len(valid_sensors & expected_sensors) > 3  # boolean flag

    adjustment_factor = 1.0
    if missing_count == 0:
        adjustment_factor = 1.15
    elif missing_count == 1:
        adjustment_factor = 0.95
    else:
        adjustment_factor = 0.8

    # Apply adjustment and finalize
    final_score = raw_score * adjustment_factor

    # Distractor: unused aggregation
    outlier_count = 0
    for v in results.values():
        if v > 100 or v < 0:
            outlier_count += 1
    avg_result = sum(results.values()) / len(results) if results else 0  # unused

    return final_score

# Input data
dataset_weights = {
    'temp': 0.4,
    'pressure': 0.3,
    'flow': 0.2,
    'humidity': 0.1
}

raw_data = {
    'temp': 85.0,
    'pressure': 92.5,
    'flow': 76.0,
    'humidity': 88.3
}

# Execute main logic
final_score = evaluate_performance(dataset_weights, raw_data)
print(f"Target result: {final_score}")