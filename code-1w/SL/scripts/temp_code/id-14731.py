from collections import defaultdict

# Simulate sensor data processing with noise filtering and performance scoring
def analyze_sensor_readings(raw_data, threshold):
    counts = defaultdict(int)
    filtered_values = []
    noise_counter = 0

    for val in raw_data:
        if abs(val) < threshold:
            filtered_values.append(val * 0.95)  # Attenuate low-amplitude signals
        else:
            noise_counter += 1
        counts['processed'] += 1

    # Misleading intermediate calculation (not directly used)
    avg_noise_ratio = noise_counter / len(raw_data) if raw_data else 0
    normalized_total = sum(abs(x) for x in filtered_values)

    return filtered_values, normalized_total, counts['processed']


def compute_stability_index(data, weight_factor=1.2):
    if not data:
        return 0
    
    squared_sum = sum(x ** 2 for x in data)
    linear_sum = sum(data)
    size_penalty = len(data) > 50

    # Complex but partially irrelevant stability formula
    instability = (squared_sum / (linear_sum + 1e-8)) * weight_factor
    if size_penalty:
        instability *= 1.1

    return instability if instability < 100 else 99.99


def evaluate_performance(metrics, base):
    adjustment = 0
    if 'amplitude' in metrics:
        adjustment += 10
    if 'consistency' in metrics:
        adjustment -= 5
    
    # Core logic: final score depends on intersection size and base
    valid_keys = {'amplitude', 'timing', 'calibration', 'outlier_rate'}
    metric_set = set(metrics.keys())
    overlap = metric_set & valid_keys
    
    # Distractor: complex branching with limited impact
    secondary_bonus = 0
    if len(overlap) == 4:
        secondary_bonus += 3
    elif len(overlap) >= 2:
        secondary_bonus += 1

    base_score = base * len(overlap)
    final_score = base_score + adjustment + secondary_bonus
    
    return final_score

# Main execution block
sensor_input = [0.1, -0.3, 0.8, 2.1, -1.5, 0.05, 3.2, 0.9, 1.7] * 6  # Extended dataset
sensor_input += [-5.0, 4.8, -3.9]  # Add outliers

processed_data, total_power, count_processed = analyze_sensor_readings(sensor_input, threshold=0.5)
stability = compute_stability_index(processed_data)

# Construct metric dictionary with some red herring keys
metrics = {
    'amplitude': total_power,
    'consistency': stability,
    'timestamp': '2024-05-20',
    'version': 'v2.1',
    'calibration': 'passed',
    'timing': count_processed,
    'debug_mode': False
}

baseline = int(stability // 2)
final_score = evaluate_performance(metrics, baseline)
print(f"Result: {final_score}")