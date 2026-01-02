from collections import defaultdict

# Simulate sensor data aggregation with noise filtering and weighted scoring
def aggregate_sensor_readings(raw_data):
    counts = defaultdict(int)
    totals = defaultdict(float)
    noise_floor = 0.5
    adjusted_entries = []
    
    for label, value in raw_data:
        if value < noise_floor:
            continue  # Filter out low-amplitude noise
        counts[label] += 1
        totals[label] += value
        adjusted_entries.append((label, value * 0.9))  # Apply sensitivity correction

    averages = {k: totals[k] / counts[k] for k in totals}
    return averages, adjusted_entries

def apply_calibration(averages):
    calibrated = {}
    calibration_offsets = {'A': 0.1, 'B': -0.05, 'C': 0.2}
    for key, avg in averages.items():
        if key in calibration_offsets:
            calibrated[key] = avg + calibration_offsets[key]
        else:
            calibrated[key] = avg
    
    # Dummy transformation (distraction)
    temp_sum = sum(calibrated.values())
    scaling_factor = 1.0 if temp_sum != 0 else 1.0
    normalized = {k: v * scaling_factor for k, v in calibrated.items()}
    return normalized

def compute_variance_component(calibrated_data):
    mean_val = sum(calibrated_data.values()) / len(calibrated_data)
    squared_diffs = [(v - mean_val) ** 2 for v in calibrated_data.values()]
    variance = sum(squared_diffs) / len(squared_diffs) if squared_diffs else 0
    return variance

def calculate_final_score(data, weights):
    averages, _ = aggregate_sensor_readings(data)
    calibrated = apply_calibration(averages)
    
    # Irrelevant intermediate computation (distractor)
    outlier_count = 0
    for val in averages.values():
        if val > 3.0:
            outlier_count += 1
    adjustment_proxy = outlier_count * 0.05
    
    base_score = 0.0
    for key, val in calibrated.items():
        weight = weights.get(key, 1.0)
        base_score += val * weight
    
    variance_term = compute_variance_component(calibrated)
    penalty = variance_term * 0.3
    final_score = base_score - penalty + adjustment_proxy  # Final formula
    
    # Dead code path (red herring)
    if False:
        fallback = sum(calibrated.values())
        final_score = max(final_score, fallback)
    
    return final_score

# Input data
raw_input = [
    ('A', 1.2), ('B', 2.1), ('A', 0.9), ('C', 1.8),
    ('B', 1.7), ('A', 2.3), ('C', 0.4), ('B', 2.0),
    ('A', 1.1), ('C', 2.2)
]
weights = {'A': 1.5, 'B': 1.2, 'C': 1.0}

# Execute main logic
intermediate_averages, processed_entries = aggregate_sensor_readings(raw_input)
calibrated_results = apply_calibration(intermediate_averages)
variance_component = compute_variance_component(calibrated_results)
final_score = calculate_final_score(raw_input, weights)

print(f"Result: {final_score}")